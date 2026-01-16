"""
Test for cisco.meraki.networks_switch_routing_multicast_rendezvous_points_info using fixture cisco.meraki.networks_switch_routing_multicast_rendezvous_points_info.json
Method: getNetworkSwitchRoutingMulticastRendezvousPoints
"""
import jq


def test_cisco_meraki_networks_switch_routing_multicast_rendezvous_points_info_getNetworkSwitchRoutingMulticastRendezvousPoints(query_data, load_fixture):
    """Test query execution for cisco.meraki.networks_switch_routing_multicast_rendezvous_points_info (getNetworkSwitchRoutingMulticastRendezvousPoints)."""
    module_fqcn = "cisco.meraki.networks_switch_routing_multicast_rendezvous_points_info"
    method_name = "getNetworkSwitchRoutingMulticastRendezvousPoints"

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
            "name": "rendezvous-point-1234",
            "canonical_facts": {
                "ansible_product_serial": "Q234-ABCD-5678",
                "hostname": "192.168.1.2"
            },
            "facts": {
                "device_type": "switch",
                "multicast_rendezvous_point": {
                    "rendezvous_point_id": "1234",
                    "serial": "Q234-ABCD-5678",
                    "interface_name": "l3_interface_0",
                    "interface_ip": "192.168.1.2",
                    "multicast_group": "Any"
                }
            }
        }
    ]
]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
