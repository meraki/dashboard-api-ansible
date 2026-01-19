"""
Test for cisco.meraki.networks_switch_dhcp_v4_servers_seen_info using fixture cisco.meraki.networks_switch_dhcp_v4_servers_seen_info.json
Method: getNetworkSwitchDhcpV4ServersSeen
"""
import jq


def test_cisco_meraki_networks_switch_dhcp_v4_servers_seen_info_getNetworkSwitchDhcpV4ServersSeen(query_data, load_fixture):
    """Test query execution for cisco.meraki.networks_switch_dhcp_v4_servers_seen_info (getNetworkSwitchDhcpV4ServersSeen)."""
    module_fqcn = "cisco.meraki.networks_switch_dhcp_v4_servers_seen_info"
    method_name = "getNetworkSwitchDhcpV4ServersSeen"

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
                "name": "Q234-ABCD-0002",
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-0002"
                },
                "facts": {
                    "device_type": "switch",
                    "dhcp_server_seen": {
                        "mac_address": "00:11:22:33:44:55",
                        "vlan": 100,
                        "ipv4": {
                            "address": "10.0.0.0/24",
                            "subnet": "192.168.1.0/24",
                            "gateway": "1.2.3.5"
                        },
                        "device_name": "My AP"
                    }
                }
            },
            {
                "name": "Q234-ABCD-0001",
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-0001"
                },
                "facts": {
                    "device_type": "switch",
                    "dhcp_server_seen": {
                        "mac_address": "00:11:22:33:44:55",
                        "vlan": 100,
                        "client_id": "k74272e",
                        "type": "device",
                        "ipv4": {
                            "address": "10.0.0.0/24",
                            "subnet": "192.168.1.0/24",
                            "gateway": "1.2.3.5"
                        }
                    }
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
