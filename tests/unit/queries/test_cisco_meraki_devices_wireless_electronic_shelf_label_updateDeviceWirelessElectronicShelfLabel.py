"""
Test for cisco.meraki.devices_wireless_electronic_shelf_label using fixture cisco.meraki.devices_wireless_electronic_shelf_label.json
Method: updateDeviceWirelessElectronicShelfLabel
"""
import jq


def test_cisco_meraki_devices_wireless_electronic_shelf_label_updateDeviceWirelessElectronicShelfLabel(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_wireless_electronic_shelf_label (updateDeviceWirelessElectronicShelfLabel)."""
    module_fqcn = "cisco.meraki.devices_wireless_electronic_shelf_label"
    method_name = "updateDeviceWirelessElectronicShelfLabel"

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
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678",
                    "hostname": "localhost:700"
                },
                "facts": {
                    "device_type": "wireless",
                    "ap_esl_id": 16777216,
                    "channel": "1",
                    "enabled": True,
                    "network_id": "N_24329156",
                    "provider": "imagotag"
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
