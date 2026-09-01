"""
Test for cisco.meraki.devices_sensor_commands using fixture cisco.meraki.devices_sensor_commands.json
Method: createDeviceSensorCommand
"""
import jq


def test_cisco_meraki_devices_sensor_commands_createDeviceSensorCommand(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_sensor_commands (createDeviceSensorCommand)."""
    module_fqcn = "cisco.meraki.devices_sensor_commands"
    method_name = "createDeviceSensorCommand"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
            "device_type": "sensor",
            "command_id": "cmd-001",
            "operation": "refreshData",
            "status": "completed",
            "created_at": "2026-08-18T10:00:00Z",
            "completed_at": "2026-08-18T10:00:05Z",
            "errors": []
        },
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
