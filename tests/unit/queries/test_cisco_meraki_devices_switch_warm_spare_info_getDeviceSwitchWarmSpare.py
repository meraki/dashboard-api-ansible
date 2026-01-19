"""
Test for cisco.meraki.devices_switch_warm_spare_info using fixture cisco.meraki.devices_switch_warm_spare_info.json
Method: getDeviceSwitchWarmSpare
"""

import jq


def test_cisco_meraki_devices_switch_warm_spare_info_getDeviceSwitchWarmSpare(
    query_data, load_fixture
):
    """Test query execution for cisco.meraki.devices_switch_warm_spare_info (getDeviceSwitchWarmSpare)."""
    module_fqcn = "cisco.meraki.devices_switch_warm_spare_info"
    method_name = "getDeviceSwitchWarmSpare"

    # Load fixture data
    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    # Prepare response in expected format
    final_response = {"meraki_response": response}

    # Get query from query_data
    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    jq_query = query_data[module_fqcn]["query"]

    # Execute query
    results = jq.compile(jq_query).input(final_response).all()

    # Expected output from query_run.log
    expected = [
        [
            {
                "name": "Q234-ABCD-0001",
                "canonical_facts": {"ansible_product_serial": "Q234-ABCD-0001"},
                "facts": {
                    "device_type": "switch",
                    "warm_spare": {
                        "enabled": True,
                        "role": "primary",
                        "spare_serial": "Q234-ABCD-0002",
                    },
                },
            },
            {
                "name": "Q234-ABCD-0002",
                "canonical_facts": {"ansible_product_serial": "Q234-ABCD-0002"},
                "facts": {
                    "device_type": "switch",
                    "warm_spare": {
                        "enabled": True,
                        "role": "spare",
                        "primary_serial": "Q234-ABCD-0001",
                    },
                },
            },
        ]
    ]

    # Assert results match expected output
    assert (
        results == expected
    ), f"Query results do not match expected output for {method_name}"
