"""
Test for cisco.meraki.networks_switch_settings using fixture cisco.meraki.networks_switch_settings.json
Method: updateNetworkSwitchSettings
"""

import jq


def test_cisco_meraki_networks_switch_settings_updateNetworkSwitchSettings(
    query_data, load_fixture
):
    """Test query execution for cisco.meraki.networks_switch_settings (updateNetworkSwitchSettings)."""
    module_fqcn = "cisco.meraki.networks_switch_settings"
    method_name = "updateNetworkSwitchSettings"

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
                    "power_exception": {"power_type": "redundant"},
                    "network_settings": {"vlan": 100, "use_combined_power": False},
                },
            }
        ]
    ]

    # Assert results match expected output
    assert (
        results == expected
    ), f"Query results do not match expected output for {method_name}"
