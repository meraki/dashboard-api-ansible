"""
Test for cisco.meraki.devices_appliance_uplinks_settings_info using fixture cisco.meraki.devices_appliance_uplinks_settings_info.json
Method: getDeviceApplianceUplinksSettings
"""
import jq


def test_cisco_meraki_devices_appliance_uplinks_settings_info_getDeviceApplianceUplinksSettings(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_appliance_uplinks_settings_info (getDeviceApplianceUplinksSettings)."""
    module_fqcn = "cisco.meraki.devices_appliance_uplinks_settings_info"
    method_name = "getDeviceApplianceUplinksSettings"

    # Load fixture data
    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    # Fixture already contains invocation + meraki_response at top level
    final_response = response

    # Get query from query_data
    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    jq_query = query_data[module_fqcn]["query"]

    # Execute query
    results = jq.compile(jq_query).input(final_response).all()

    # Expected output
    expected = [
        [
            {
                "facts": {
                    "device_type": "appliance",
                    "wan1": {
                        "enabled": True,
                        "vlan_tagging_enabled": False,
                        "vlan_id": 0
                    },
                    "wan2": {
                        "enabled": False,
                        "vlan_tagging_enabled": False,
                        "vlan_id": 0
                    }
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
