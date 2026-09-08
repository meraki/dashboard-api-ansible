"""
Test for cisco.meraki.devices_sensor_commands_info using fixture cisco.meraki.devices_sensor_commands_info.json
Method: getDeviceSensorCommands
"""
import jq


def test_cisco_meraki_devices_sensor_commands_info_getDeviceSensorCommands(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_sensor_commands_info (getDeviceSensorCommands)."""
    module_fqcn = "cisco.meraki.devices_sensor_commands_info"
    method_name = "getDeviceSensorCommands"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
            "device_type": "sensor",
            "commands": [
                {"command_id": "cmd-001", "operation": "refreshData", "status": "completed",
                 "created_at": "2026-08-18T10:00:00Z", "completed_at": "2026-08-18T10:00:05Z", "errors": []},
                {"command_id": "cmd-002", "operation": "resetFactory", "status": "pending",
                 "created_at": "2026-08-18T09:00:00Z", "completed_at": None, "errors": []}
            ]
        },
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
