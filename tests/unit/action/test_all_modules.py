"""
Offline checks for every action plugin of the collection (no API calls).

The Meraki SDK installed in the environment is the reference: every call a
plugin makes is validated against the real SDK method (does it exist, are
its required parameters sent, are the parameters sent accepted by the SDK
or silently dropped). Each plugin's run() is also executed for every state
against a fake API, to catch Python crashes.

Run against the SDK version the collection targets (see README.md):

    pip install "meraki>=4.4.0"
    pytest tests/unit/action/test_all_modules.py -q

Category summary without pytest:

    python tests/unit/action/module_contract.py
"""

import re
from pathlib import Path

import pytest

import module_contract as mc

pytest.importorskip("meraki")

ACTIONS = mc.action_names()

# Harness limitations, not plugin bugs. Keep the reason next to each entry.
KNOWN_FALSE_POSITIVES = {
    # `rules` has no element type in the argspec, so the harness generates a
    # list of strings; the real API always returns a list of dicts.
    ("crash", "networks_appliance_firewall_l3_firewall_rules"),
}

# Generator-wide documentation issues, reported once (see the aggregated
# tests at the bottom) instead of once per module.
GENERATOR_WIDE_DOC_ISSUES = {"headers", "state"}


@pytest.fixture(scope="module")
def reports():
    cache = {}

    def get(name):
        if name not in cache:
            cache[name] = mc.check_plugin(name)
        return cache[name]
    return get


def _min_sdk_from_readme():
    readme = (mc.REPO / "README.md").read_text()
    galaxy, manifest = mc.REPO / "galaxy.yml", mc.REPO / "MANIFEST.json"
    if galaxy.exists():  # source checkout
        version = re.search(r"^version:\s*([\d.]+)", galaxy.read_text(), re.M).group(1)
    else:  # installed collection
        import json
        version = json.loads(manifest.read_text())["collection_info"]["version"]
    row = re.search(r"\|\s*[\d.]+\s*\|\s*%s\s*\|\s*([\d.]+)\s*\|" % re.escape(version), readme)
    return row.group(1) if row else None


def _v(s):
    return tuple(int(x) for x in re.findall(r"\d+", s)[:3])


def test_installed_sdk_meets_collection_minimum():
    import meraki
    minimum = _min_sdk_from_readme()
    if minimum is None:
        pytest.skip("README.md has no compatibility row for this collection version")
    assert _v(meraki.__version__) >= _v(minimum), (
        "meraki SDK %s is installed but this collection needs >= %s (README.md). "
        "Many modules call SDK functions that do not exist in older versions."
        % (meraki.__version__, minimum))


@pytest.mark.parametrize("name", ACTIONS)
def test_plugin_imports(name, reports):
    assert reports(name)["import_error"] is None, reports(name)["import_error"]


@pytest.mark.parametrize("name", ACTIONS)
def test_sdk_functions_exist(name, reports):
    """family/function used by exec_meraki() exist in the installed SDK."""
    missing = reports(name)["missing_sdk"]
    assert not missing, "not found in the SDK: %s" % missing


@pytest.mark.parametrize("name", ACTIONS)
def test_sdk_parameters(name, reports):
    """Required SDK parameters are sent and no parameter is silently dropped."""
    v = [x for x in reports(name)["violations"] if x[0] != "missing_sdk_function"]
    assert not v, v


@pytest.mark.parametrize("name", ACTIONS)
def test_run_does_not_crash(name, reports):
    if ("crash", name) in KNOWN_FALSE_POSITIVES:
        pytest.skip("known harness false positive")
    crashes = reports(name)["crashes"]
    assert not crashes, crashes


@pytest.mark.parametrize("name", ACTIONS)
def test_documentation_matches_argspec(name):
    problems = []
    for p in mc.check_docs(name):
        m = re.match(r"(.*?): \[(.*)\]$", p)
        if m:
            keys = set(re.findall(r"'(\w+)'", m.group(2))) - GENERATOR_WIDE_DOC_ISSUES
            if keys:
                problems.append("%s: %s" % (m.group(1), sorted(keys)))
        else:
            problems.append(p)
    assert not problems, problems


def test_every_module_has_an_action_plugin():
    acts = set(ACTIONS)
    orphans = [m for m in mc.module_names() if m not in acts and not m.startswith("meraki_")]
    assert not orphans, "documented modules with no action plugin (unusable): %s" % orphans


def _doc_issue_count(key, kind):
    hits = []
    for n in ACTIONS:
        for p in mc.check_docs(n):
            if p.startswith(kind) and "'%s'" % key in p:
                hits.append(n)
    return hits


def test_info_modules_do_not_document_unsupported_headers_option():
    hits = _doc_issue_count("headers", "documented but not accepted")
    assert not hits, "%d modules document 'headers' but reject it, e.g. %s" % (len(hits), hits[:5])


def test_state_option_is_documented():
    hits = _doc_issue_count("state", "options not documented")
    assert not hits, "%d modules accept 'state' without documenting it, e.g. %s" % (len(hits), hits[:5])


def test_documented_connection_options_are_accepted():
    """Every meraki_* option documented in the doc fragments must be in
    meraki_argument_spec(); otherwise copying any module EXAMPLE fails with
    'Unsupported parameters'."""
    import importlib
    mc._setup_import_path()
    spec = importlib.import_module(mc.PKG + ".plugins.plugin_utils.meraki").meraki_argument_spec()
    for frag in ("module", "module_info"):
        documented = {o for o in mc.fragment_options(frag) if o.startswith(mc.COMMON_PREFIX)}
        assert documented <= set(spec), (frag, sorted(documented - set(spec)))
        assert set(spec) <= documented, (frag, sorted(set(spec) - documented))
