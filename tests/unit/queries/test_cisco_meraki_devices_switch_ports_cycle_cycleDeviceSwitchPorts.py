"""
Test for cisco.meraki.devices_switch_ports_cycle using fixture cisco.meraki.devices_switch_ports_cycle.json
Method: cycleDeviceSwitchPorts
"""
import jq


def test_cisco_meraki_devices_switch_ports_cycle_cycleDeviceSwitchPorts(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_switch_ports_cycle (cycleDeviceSwitchPorts)."""
    module_fqcn = "cisco.meraki.devices_switch_ports_cycle"
    method_name = "cycleDeviceSwitchPorts"

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
            "name": "port-1",
            "canonical_facts": {
                "ansible_machine_id": "1"
            },
            "facts": {
                "device_type": "switch",
                "port_identifier": "1"
            }
        },
        {
            "name": "port-2-5",
            "canonical_facts": {
                "ansible_machine_id": "2-5"
            },
            "facts": {
                "device_type": "switch",
                "port_identifier": "2-5"
            }
        },
        {
            "name": "port-1_MA-MOD-8X10G_1",
            "canonical_facts": {
                "ansible_machine_id": "1_MA-MOD-8X10G_1"
            },
            "facts": {
                "device_type": "switch",
                "port_identifier": "1_MA-MOD-8X10G_1"
            }
        },
        {
            "name": "port-1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8",
            "canonical_facts": {
                "ansible_machine_id": "1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8"
            },
            "facts": {
                "device_type": "switch",
                "port_identifier": "1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8"
            }
        }
    ]
]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
