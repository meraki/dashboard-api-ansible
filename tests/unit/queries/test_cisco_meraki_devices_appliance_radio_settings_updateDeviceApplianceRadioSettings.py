"""
Test for cisco.meraki.devices_appliance_radio_settings using fixture cisco.meraki.devices_appliance_radio_settings.json
Method: updateDeviceApplianceRadioSettings
"""
import jq


def test_cisco_meraki_devices_appliance_radio_settings_updateDeviceApplianceRadioSettings(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_appliance_radio_settings (updateDeviceApplianceRadioSettings)."""
    module_fqcn = "cisco.meraki.devices_appliance_radio_settings"
    method_name = "updateDeviceApplianceRadioSettings"

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

    # Expected output
    expected = [
        [
            {
                "name": "appliance-radio-settings-Q234-ABCD-5678",
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                },
                "facts": {
                    "device_type": "sd_wan",
                    "infra_type": "private_cloud",
                    "infra_bucket": "networking",
                    "rf_profile_id": "1234",
                    "two_four_ghz_settings": {
                        "channel": 6,
                        "target_power": 20
                    },
                    "five_ghz_settings": {
                        "channel": 149,
                        "channel_width": 20,
                        "target_power": 15
                    }
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"


def test_cisco_meraki_devices_appliance_radio_settings_missing_band_settings(query_data):
    module_fqcn = "cisco.meraki.devices_appliance_radio_settings"
    response = {"meraki_response": {"serial": "Q234-ABCD-5678"}}
    results = jq.compile(query_data[module_fqcn]["query"]).input(response).all()
    expected = [[{
        "name": "appliance-radio-settings-Q234-ABCD-5678",
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"},
        "facts": {
            "device_type": "sd_wan",
            "infra_type": "private_cloud",
            "infra_bucket": "networking", "rf_profile_id": None,
            "two_four_ghz_settings": {"channel": None, "target_power": None},
            "five_ghz_settings": {"channel": None, "channel_width": None, "target_power": None},
        },
    }]]
    assert results == expected
