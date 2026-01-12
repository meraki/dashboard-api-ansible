"""
Test for cisco.meraki.networks_switch_dhcp_server_policy_info using fixture cisco.meraki.networks_switch_dhcp_server_policy_info.json
Method: getNetworkSwitchDhcpServerPolicy
"""

import jq
import pytest


def test_cisco_meraki_networks_switch_dhcp_server_policy_info_getNetworkSwitchDhcpServerPolicy(
    query_data, load_fixture
):
    """Test query execution for cisco.meraki.networks_switch_dhcp_server_policy_info (getNetworkSwitchDhcpServerPolicy)."""
    module_fqcn = "cisco.meraki.networks_switch_dhcp_server_policy_info"
    method_name = "getNetworkSwitchDhcpServerPolicy"

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
                "name": "blocked-dhcp-server-00:50:56:00:00:03",
                "canonical_facts": {"ansible_machine_id": "00:50:56:00:00:03"},
                "facts": {
                    "device_type": "switch",
                    "dhcp_server_policy": {
                        "status": "blocked",
                        "mac_address": "00:50:56:00:00:03",
                        "default_policy": "block",
                        "arp_inspection_enabled": True,
                    },
                },
            },
            {
                "name": "blocked-dhcp-server-00:50:56:00:00:04",
                "canonical_facts": {"ansible_machine_id": "00:50:56:00:00:04"},
                "facts": {
                    "device_type": "switch",
                    "dhcp_server_policy": {
                        "status": "blocked",
                        "mac_address": "00:50:56:00:00:04",
                        "default_policy": "block",
                        "arp_inspection_enabled": True,
                    },
                },
            },
            {
                "name": "allowed-dhcp-server-00:50:56:00:00:01",
                "canonical_facts": {"ansible_machine_id": "00:50:56:00:00:01"},
                "facts": {
                    "device_type": "switch",
                    "dhcp_server_policy": {
                        "status": "allowed",
                        "mac_address": "00:50:56:00:00:01",
                        "default_policy": "block",
                        "arp_inspection_enabled": True,
                    },
                },
            },
            {
                "name": "allowed-dhcp-server-00:50:56:00:00:02",
                "canonical_facts": {"ansible_machine_id": "00:50:56:00:00:02"},
                "facts": {
                    "device_type": "switch",
                    "dhcp_server_policy": {
                        "status": "allowed",
                        "mac_address": "00:50:56:00:00:02",
                        "default_policy": "block",
                        "arp_inspection_enabled": True,
                    },
                },
            },
        ]
    ]

    # Assert results match expected output
    assert (
        results == expected
    ), f"Query results do not match expected output for {method_name}"
