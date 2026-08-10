"""
Test for cisco.meraki.devices_wireless_zigbee_enrollments using fixture cisco.meraki.devices_wireless_zigbee_enrollments.json
Method: createDeviceWirelessZigbeeEnrollment
"""
import jq


def test_cisco_meraki_devices_wireless_zigbee_enrollments_createDeviceWirelessZigbeeEnrollment(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_wireless_zigbee_enrollments (createDeviceWirelessZigbeeEnrollment)."""
    module_fqcn = "cisco.meraki.devices_wireless_zigbee_enrollments"
    method_name = "createDeviceWirelessZigbeeEnrollment"

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
                    "ansible_product_serial": "Q234-ABCD-5678"
                },
                "facts": {
                    "device_type": "wireless",
                    "enrollment_id": "1234",
                    "status": "complete"
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
