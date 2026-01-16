"""
Test for cisco.meraki.networks_switch_routing_multicast using fixture cisco.meraki.networks_switch_routing_multicast.json
Method: updateNetworkSwitchRoutingMulticast
"""

import jq


def test_cisco_meraki_networks_switch_routing_multicast_updateNetworkSwitchRoutingMulticast(
    query_data, load_fixture
):
    """Test query execution for cisco.meraki.networks_switch_routing_multicast (updateNetworkSwitchRoutingMulticast)."""
    module_fqcn = "cisco.meraki.networks_switch_routing_multicast"
    method_name = "updateNetworkSwitchRoutingMulticast"

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
                "name": "Q234-ABCD-0001",
                "canonical_facts": {"ansible_product_serial": "Q234-ABCD-0001"},
                "facts": {
                    "device_type": "switch",
                    "multicast_settings": {
                        "igmp_snooping_enabled": True,
                        "flood_unknown_multicast_traffic_enabled": True,
                    },
                    "default_settings": {
                        "igmp_snooping_enabled": True,
                        "flood_unknown_multicast_traffic_enabled": True,
                    },
                },
            },
            {
                "name": "Q234-ABCD-0002",
                "canonical_facts": {"ansible_product_serial": "Q234-ABCD-0002"},
                "facts": {
                    "device_type": "switch",
                    "multicast_settings": {
                        "igmp_snooping_enabled": True,
                        "flood_unknown_multicast_traffic_enabled": True,
                    },
                    "default_settings": {
                        "igmp_snooping_enabled": True,
                        "flood_unknown_multicast_traffic_enabled": True,
                    },
                },
            },
            {
                "name": "Q234-ABCD-0003",
                "canonical_facts": {"ansible_product_serial": "Q234-ABCD-0003"},
                "facts": {
                    "device_type": "switch",
                    "multicast_settings": {
                        "igmp_snooping_enabled": True,
                        "flood_unknown_multicast_traffic_enabled": True,
                    },
                    "default_settings": {
                        "igmp_snooping_enabled": True,
                        "flood_unknown_multicast_traffic_enabled": True,
                    },
                },
            },
        ]
    ]

    # Assert results match expected output
    assert (
        results == expected
    ), f"Query results do not match expected output for {method_name}"
