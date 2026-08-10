"""
Test for cisco.meraki.devices_wireless_zigbee_enrollments_info using fixture cisco.meraki.devices_wireless_zigbee_enrollments_info.json
Method: getDeviceWirelessZigbeeEnrollment
"""
import jq


def test_cisco_meraki_devices_wireless_zigbee_enrollments_info_getDeviceWirelessZigbeeEnrollment(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_wireless_zigbee_enrollments_info (getDeviceWirelessZigbeeEnrollment)."""
    module_fqcn = "cisco.meraki.devices_wireless_zigbee_enrollments_info"
    method_name = "getDeviceWirelessZigbeeEnrollment"

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
                "name": "Door Lock 123",
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                },
                "facts": {
                    "device_type": "wireless",
                    "door_lock_id": "1",
                    "short_id": "ABE123",
                    "eui64": "DL403",
                    "lqi": "1",
                    "rssi": "1",
                    "status": "online",
                    "enrolled_at": "2023-08-14T19:57:06Z",
                    "last_seen_at": "2023-08-14T19:59:01Z",
                    "network": {"id": "N_24329156", "name": "Main Office"},
                    "gateway": {"name": "My AP", "serial": "Q234-ABCD-5678"},
                    "enrollment_id": "1234",
                    "enrollment_status": "complete"
                }
            },
            {
                "name": "Door Lock 456",
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                },
                "facts": {
                    "device_type": "wireless",
                    "door_lock_id": "2",
                    "short_id": "ABE456",
                    "eui64": "DL404",
                    "lqi": "2",
                    "rssi": "2",
                    "status": "online",
                    "enrolled_at": "2023-08-15T10:00:00Z",
                    "last_seen_at": "2023-08-15T10:05:00Z",
                    "network": {"id": "N_24329156", "name": "Main Office"},
                    "gateway": {"name": "My AP", "serial": "Q234-ABCD-5678"},
                    "enrollment_id": "1234",
                    "enrollment_status": "complete"
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
