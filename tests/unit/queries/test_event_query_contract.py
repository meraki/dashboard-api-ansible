"""
Contract tests for extensions/audit/event_query.yml.

The other tests in this directory are snapshot tests: each one runs a query against a recorded
API fixture and compares the result to output captured from a real run. That verifies the query
still behaves the way it behaved when the fixture was recorded, which is valuable, but it cannot
say whether that behaviour is correct -- the expected value is derived from the output, so it
agrees with the output by construction.

These tests assert the contract instead. Indirect node counting in Ansible Automation Platform
consumes this query file's output, and imposes three requirements on it:

1. A non-null top-level ``name`` on every emitted record. Records without one are discarded.
2. ``infra_type``, ``infra_bucket`` and ``device_type`` are all emitted. Without them a node is
   counted but cannot be bucketed, so it does not appear in any rollup.
3. Taxonomy values are normalized ``lowercase_with_underscores``. ``CellularGateway`` and
   ``cellular_gateway`` would be counted as two distinct device types.

Modules are enumerated from event_query.yml itself, so a newly added module is covered the moment
it is added. The structural checks need no fixture at all; the runtime check uses the recorded
fixture where one exists and skips where it does not.
"""

import re

import jq
import pytest
import yaml

from pathlib import Path

QUERY_FILE = (
    Path(__file__).parent.parent.parent.parent
    / "extensions"
    / "audit"
    / "event_query.yml"
)

TAXONOMY_KEYS = ("infra_type", "infra_bucket", "device_type")

NORMALIZED = re.compile(r"^[a-z0-9]+(_[a-z0-9]+)*$")


def _load_queries():
    with open(QUERY_FILE) as handle:
        document = yaml.safe_load(handle) or {}
    return {
        name: spec["query"]
        for name, spec in document.items()
        if isinstance(spec, dict) and "query" in spec
    }


QUERIES = _load_queries()

MODULES = sorted(QUERIES)


def _brace_blocks(query):
    """Yield (start, end, inner_text) for every balanced {...} block."""
    stack = []
    for index, character in enumerate(query):
        if character == "{":
            stack.append(index)
        elif character == "}" and stack:
            start = stack.pop()
            yield start, index, query[start + 1 : index]


def _emitted_object(query):
    """Inner text of the object the query emits.

    A query may build helper objects before emitting its result, so the first ``{`` is not
    reliably the emitted one. Use the outermost block containing ``canonical_facts``.
    """
    blocks = list(_brace_blocks(query))
    if not blocks:
        return ""
    with_canonical = [block for block in blocks if "canonical_facts" in block[2]]
    return max(with_canonical or blocks, key=lambda block: block[1] - block[0])[2]


def _top_level_keys(query):
    body = _emitted_object(query)
    depth = 0
    top = ""
    for character in body:
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
        elif depth == 0:
            top += character
    return re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\s*:", top)


def _emits_key(query, key):
    """Whether the emitted object assigns ``key`` at all."""
    return re.search(rf"\b{key}\s*:", _emitted_object(query)) is not None


def _records(value):
    """Yield every emitted node record from a query result.

    Queries emit either a single object or an array, and jq's ``.all()`` wraps that again, so the
    result nesting varies by module. Walk it and pick out anything shaped like a node record.
    """
    if isinstance(value, dict):
        if "canonical_facts" in value or "facts" in value:
            yield value
        return
    if isinstance(value, list):
        for item in value:
            yield from _records(item)


def test_query_file_parses():
    assert QUERIES, f"{QUERY_FILE} declares no module queries"


@pytest.mark.parametrize("module_fqcn", MODULES)
def test_query_compiles(module_fqcn):
    jq.compile(QUERIES[module_fqcn])


@pytest.mark.parametrize("module_fqcn", MODULES)
def test_query_emits_top_level_name(module_fqcn):
    keys = _top_level_keys(QUERIES[module_fqcn])
    assert "name" in keys, (
        f"{module_fqcn}: the emitted object has no top-level 'name'. Records without one are "
        f"discarded by the consumer, so this module contributes no node data. "
        f"Emitted top-level keys: {sorted(set(keys))}"
    )


@pytest.mark.parametrize("module_fqcn", MODULES)
def test_query_emits_full_taxonomy(module_fqcn):
    query = QUERIES[module_fqcn]
    missing = [key for key in TAXONOMY_KEYS if not _emits_key(query, key)]
    assert not missing, (
        f"{module_fqcn}: taxonomy keys {missing} are not emitted. Nodes from this module are "
        f"counted but cannot be bucketed, so they are absent from every rollup."
    )


@pytest.mark.parametrize("module_fqcn", MODULES)
def test_emitted_records_satisfy_contract(module_fqcn, load_fixture):
    """Run the query against its recorded fixture and check the contract on real output.

    This is the counterpart to the static checks above. A taxonomy value can be computed at
    runtime -- derived from an API field, or selected by a conditional -- and no amount of reading
    the query text will settle whether the result is normalized. Running it does.

    Unlike the snapshot tests, the expectation here is not taken from the output, so this can fail
    on output that is stable but wrong.
    """
    response = load_fixture(module_fqcn)
    if response is None:
        pytest.skip(f"no recorded fixture for {module_fqcn}")

    results = (
        jq.compile(QUERIES[module_fqcn]).input({"meraki_response": response}).all()
    )
    records = list(_records(results))
    if not records:
        pytest.skip(f"{module_fqcn} emits no records for its recorded fixture")

    for record in records:
        name = record.get("name")
        assert (
            name
        ), f"{module_fqcn}: emitted a record with no usable top-level 'name': {record}"

        facts = record.get("facts") or {}
        missing = [key for key in TAXONOMY_KEYS if not facts.get(key)]
        assert (
            not missing
        ), f"{module_fqcn}: emitted a record missing taxonomy {missing}: {facts}"

        offenders = {
            key: facts[key]
            for key in TAXONOMY_KEYS
            if not NORMALIZED.match(str(facts[key]))
        }
        assert not offenders, (
            f"{module_fqcn}: emitted taxonomy values that are not lowercase_with_underscores: "
            f"{offenders}"
        )


@pytest.mark.parametrize(
    "product_type,expected",
    [
        ("switch", "switch"),
        ("wireless", "wireless"),
        ("appliance", "appliance"),
        ("camera", "camera"),
        ("sensor", "sensor"),
        ("cellularGateway", "cellular_gateway"),
        ("systemsManager", "systems_manager"),
    ],
)
def test_devices_info_normalizes_product_type(product_type, expected):
    """devices_info derives device_type from the API's productType, which is camelCase for some
    families. Normalize it rather than passing it through, so a product family the fixtures do not
    happen to cover cannot leak an unnormalized value into the taxonomy.
    """
    response = {
        "meraki_response": [
            {
                "name": "device-1",
                "serial": "Q234-ABCD-5678",
                "lanIp": "1.2.3.4",
                "model": "MS220-8P",
                "firmware": "switch-11-31",
                "mac": "00:11:22:33:44:55",
                "networkId": "N_24329156",
                "productType": product_type,
            }
        ]
    }
    results = jq.compile(QUERIES["cisco.meraki.devices_info"]).input(response).all()
    assert results[0][0]["facts"]["device_type"] == expected
