"""
Test for cisco.meraki.networks_switch_access_control_lists_info using fixture cisco.meraki.networks_switch_access_control_lists_info.json
Method: getNetworkSwitchAccessControlLists
"""
import jq


def test_cisco_meraki_networks_switch_access_control_lists_info_getNetworkSwitchAccessControlLists(query_data, load_fixture):
    """Test query execution for cisco.meraki.networks_switch_access_control_lists_info (getNetworkSwitchAccessControlLists)."""
    module_fqcn = "cisco.meraki.networks_switch_access_control_lists_info"
    method_name = "getNetworkSwitchAccessControlLists"

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
                "name": "Deny SSH",
                "canonical_facts": {
                    "ansible_machine_id": "172.16.30/24-0"
                },
                "facts": {
                    "device_type": "switch",
                    "acl_rule": {
                        "comment": "Deny SSH",
                        "policy": "deny",
                        "ip_version": "ipv4",
                        "protocol": "tcp",
                        "src_cidr": "10.1.10.0/24",
                        "src_port": "any",
                        "dst_cidr": "172.16.30/24",
                        "dst_port": "22",
                        "vlan": "10",
                        "rule_index": 0
                    }
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
