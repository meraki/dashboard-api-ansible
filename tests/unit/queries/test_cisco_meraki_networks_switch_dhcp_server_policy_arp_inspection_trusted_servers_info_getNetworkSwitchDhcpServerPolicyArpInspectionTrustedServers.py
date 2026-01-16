"""
Test for cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_trusted_servers_info using fixture cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_trusted_servers_info.json
Method: getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers
"""
import jq


def test_cisco_meraki_networks_switch_dhcp_server_policy_arp_inspection_trusted_servers_info_getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(query_data, load_fixture):
    """Test query execution for cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_trusted_servers_info (getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers)."""
    module_fqcn = "cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_trusted_servers_info"
    method_name = "getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers"

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
            "name": "trusted-server-123",
            "canonical_facts": {
                "ansible_machine_id": "00:11:22:33:44:55",
                "hostname": "1.2.3.4"
            },
            "facts": {
                "device_type": "switch",
                "trusted_server": {
                    "trusted_server_id": "123",
                    "mac_address": "00:11:22:33:44:55",
                    "vlan": 100,
                    "ipv4_address": "1.2.3.4"
                }
            }
        }
    ]
]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
