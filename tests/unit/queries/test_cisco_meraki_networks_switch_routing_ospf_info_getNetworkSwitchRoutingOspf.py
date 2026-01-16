"""
Test for cisco.meraki.networks_switch_routing_ospf_info using fixture cisco.meraki.networks_switch_routing_ospf_info.json
Method: getNetworkSwitchRoutingOspf
"""

import jq


def test_cisco_meraki_networks_switch_routing_ospf_info_getNetworkSwitchRoutingOspf(
    query_data, load_fixture
):
    """Test query execution for cisco.meraki.networks_switch_routing_ospf_info (getNetworkSwitchRoutingOspf)."""
    module_fqcn = "cisco.meraki.networks_switch_routing_ospf_info"
    method_name = "getNetworkSwitchRoutingOspf"

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
                "name": "Backbone",
                "canonical_facts": {"ansible_machine_id": "1284392014819"},
                "facts": {
                    "device_type": "switch",
                    "ospf_version": "v2",
                    "ospf_area": {
                        "area_id": "1284392014819",
                        "area_name": "Backbone",
                        "area_type": "normal",
                    },
                    "ospf_config": {
                        "enabled": True,
                        "hello_timer": 10,
                        "dead_timer": 40,
                        "md5_authentication_enabled": True,
                    },
                    "vrf": {"name": "Blue"},
                },
            },
            {
                "name": "V3 Backbone",
                "canonical_facts": {"ansible_machine_id": "v3-1284392014819"},
                "facts": {
                    "device_type": "switch",
                    "ospf_version": "v3",
                    "ospf_area": {
                        "area_id": "1284392014819",
                        "area_name": "V3 Backbone",
                        "area_type": "normal",
                    },
                    "ospf_config": {
                        "enabled": True,
                        "hello_timer": 10,
                        "dead_timer": 40,
                    },
                    "vrf": {"name": "Blue"},
                },
            },
        ]
    ]

    # Assert results match expected output
    assert (
        results == expected
    ), f"Query results do not match expected output for {method_name}"
