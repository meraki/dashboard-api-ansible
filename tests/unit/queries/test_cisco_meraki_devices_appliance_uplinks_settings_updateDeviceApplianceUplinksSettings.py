"""
Test for cisco.meraki.devices_appliance_uplinks_settings using fixture cisco.meraki.devices_appliance_uplinks_settings.json
Method: updateDeviceApplianceUplinksSettings
"""
import jq


def test_cisco_meraki_devices_appliance_uplinks_settings_updateDeviceApplianceUplinksSettings(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_appliance_uplinks_settings (updateDeviceApplianceUplinksSettings)."""
    module_fqcn = "cisco.meraki.devices_appliance_uplinks_settings"
    method_name = "updateDeviceApplianceUplinksSettings"

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
                "name": "appliance-uplinks-settings-Q234-ABCD-5678",
                "facts": {
                    "device_type": "sd_wan",
                    "infra_type": "private_cloud",
                    "infra_bucket": "networking",
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


def test_cisco_meraki_devices_appliance_uplinks_settings_missing_optional_wan_fields(query_data):
    module_fqcn = "cisco.meraki.devices_appliance_uplinks_settings"
    response = {
        "invocation": {"module_args": {"serial": "Q234-ABCD-5678"}},
        "meraki_response": {"wan1": {"enabled": True}},
    }
    results = jq.compile(query_data[module_fqcn]["query"]).input(response).all()
    expected = [[{
        "name": "appliance-uplinks-settings-Q234-ABCD-5678",
        "facts": {
            "device_type": "sd_wan",
            "infra_type": "private_cloud",
            "infra_bucket": "networking",
            "wan1": {"enabled": True, "vlan_tagging_enabled": False, "vlan_id": None},
            "wan2": {"enabled": False, "vlan_tagging_enabled": False, "vlan_id": None},
        },
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"},
    }]]
    assert results == expected
