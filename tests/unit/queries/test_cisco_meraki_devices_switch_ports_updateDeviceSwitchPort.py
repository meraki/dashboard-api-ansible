"""
Test for cisco.meraki.devices_switch_ports using fixture cisco.meraki.devices_switch_ports.json
Method: updateDeviceSwitchPort
"""
import jq
import pytest


def test_cisco_meraki_devices_switch_ports_updateDeviceSwitchPort(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_switch_ports (updateDeviceSwitchPort)."""
    module_fqcn = "cisco.meraki.devices_switch_ports"
    method_name = "updateDeviceSwitchPort"
    
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
            "name": "My switch port",
            "canonical_facts": {
                "ansible_product_serial": "3_MA-MOD-4X10G"
            },
            "facts": {
                "device_type": "switch",
                "port_id": "1",
                "module": {
                    "model": "MA-MOD-4X10G",
                    "serial": "3_MA-MOD-4X10G",
                    "slot": 1
                }
            }
        }
    ]
]
    
    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
