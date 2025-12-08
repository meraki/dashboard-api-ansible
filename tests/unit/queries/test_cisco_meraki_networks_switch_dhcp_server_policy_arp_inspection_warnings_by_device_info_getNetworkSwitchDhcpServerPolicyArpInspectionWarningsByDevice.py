"""
Test for cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_warnings_by_device_info using fixture cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_warnings_by_device_info.json
Method: getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice
"""

import jq
import pytest


def test_cisco_meraki_networks_switch_dhcp_server_policy_arp_inspection_warnings_by_device_info_getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(
    query_data, load_fixture
):
    """Test query execution for cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_warnings_by_device_info (getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice)."""
    module_fqcn = "cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_warnings_by_device_info"
    method_name = "getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice"

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
                "name": "My switch",
                "canonical_facts": {"ansible_product_serial": "Q234-ABCD-0001"},
                "facts": {
                    "device_type": "switch",
                    "arp_inspection_warning": {
                        "supports_inspection": False,
                        "has_trusted_port": False,
                        "url": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
                    },
                },
            }
        ]
    ]

    # Assert results match expected output
    assert (
        results == expected
    ), f"Query results do not match expected output for {method_name}"
