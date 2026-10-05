"""Validate the required name field for device-scoped audit queries."""

import jq


def test_device_queries_emit_non_empty_unique_names(query_data, load_fixture):
    """Every emitted device resource has a stable top-level name."""
    modules = sorted(
        module_fqcn
        for module_fqcn in query_data
        if module_fqcn.startswith("cisco.meraki.devices_")
    )

    for module_fqcn in modules:
        response = load_fixture(module_fqcn)
        assert response is not None, f"Fixture {module_fqcn}.json not found"
        final_response = (
            response
            if "meraki_response" in response
            else {"meraki_response": response}
        )
        results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

        for result_batch in results:
            assert isinstance(result_batch, list), module_fqcn
            names = [item.get("name") for item in result_batch]
            assert all(names), f"Missing name in {module_fqcn}: {result_batch}"
            assert len(names) == len(set(names)), (
                f"Duplicate names in {module_fqcn}: {names}"
            )


def _query_records(query, response):
    """Return records emitted by an audit query's array result."""
    batches = jq.compile(query).input(response).all()
    return [record for batch in batches if isinstance(batch, list) for record in batch]


def test_serial_scoped_queries_use_invocation_module_args(query_data, load_fixture):
    """Serial-scoped device queries retain the target serial as canonical identity."""
    tested_modules = []

    for module_fqcn, query_config in query_data.items():
        if not module_fqcn.startswith("cisco.meraki.devices_"):
            continue

        response = load_fixture(module_fqcn)
        if not isinstance(response, dict):
            continue

        serial = (
            response.get("invocation", {})
            .get("module_args", {})
            .get("serial")
        )
        if not serial:
            continue

        tested_modules.append(module_fqcn)
        records = _query_records(query_config["query"], response)
        assert records, f"No records emitted for {module_fqcn}"
        assert all(
            record.get("canonical_facts", {}).get("ansible_product_serial")
            == serial
            for record in records
        ), f"Missing canonical serial for {module_fqcn}: {records}"

    assert tested_modules, "No serial-scoped device query fixtures were tested"


def test_vmx_authentication_token_is_not_emitted(query_data, load_fixture):
    """The vMX API token must not be copied into audit records."""
    module_fqcn = "cisco.meraki.devices_appliance_vmx_authentication_token"
    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    records = _query_records(query_data[module_fqcn]["query"], response)
    assert records, f"No records emitted for {module_fqcn}"
    api_token = response["meraki_response"]["token"]
    assert all("token" not in record.get("facts", {}) for record in records)
    assert all(api_token not in str(record) for record in records)
