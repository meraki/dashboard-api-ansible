"""
Test for cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp_info using fixture cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp_info.json
Method: getNetworkSwitchStackRoutingInterfaceDhcp
"""
import jq


def test_cisco_meraki_networks_switch_stacks_routing_interfaces_dhcp_info_getNetworkSwitchStackRoutingInterfaceDhcp(query_data, load_fixture):
    """Test query execution for cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp_info (getNetworkSwitchStackRoutingInterfaceDhcp)."""
    module_fqcn = "cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp_info"
    method_name = "getNetworkSwitchStackRoutingInterfaceDhcp"

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
        {            {
            "name": "Cisco Meraki valued client",
            "canonical_facts": {
                "hostname": "192.168.1.12",
                "ansible_machine_id": "22:33:44:55:66:77"
            },
            "facts": {
                "device_type": "switch",
                "fixed_ip_assignment": {
                    "mac": "22:33:44:55:66:77",
                    "ip": "192.168.1.12",
                    "name": "Cisco Meraki valued client"
                }
            }
        }
        ]
]

    # Assert    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
