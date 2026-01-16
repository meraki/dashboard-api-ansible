"""
Test for cisco.meraki.devices_switch_ports_info using fixture cisco.meraki.devices_switch_ports_info.json
Method: getDeviceSwitchPort
"""
import jq


def test_cisco_meraki_devices_switch_ports_info_getDeviceSwitchPort(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_switch_ports_info (getDeviceSwitchPort)."""
    module_fqcn = "cisco.meraki.devices_switch_ports_info"
    method_name = "getDeviceSwitchPort"

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
                    "vlan_id": 10
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
