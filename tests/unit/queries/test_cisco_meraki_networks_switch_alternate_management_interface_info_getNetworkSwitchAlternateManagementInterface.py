"""
Test for cisco.meraki.networks_switch_alternate_management_interface_info using fixture cisco.meraki.networks_switch_alternate_management_interface_info.json
Method: getNetworkSwitchAlternateManagementInterface
"""

import jq
import pytest


def test_cisco_meraki_networks_switch_alternate_management_interface_info_getNetworkSwitchAlternateManagementInterface(
    query_data, load_fixture
):
    """Test query execution for cisco.meraki.networks_switch_alternate_management_interface_info (getNetworkSwitchAlternateManagementInterface)."""
    module_fqcn = "cisco.meraki.networks_switch_alternate_management_interface_info"
    method_name = "getNetworkSwitchAlternateManagementInterface"

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
                "name": "Q234-ABCD-5678",
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678",
                    "hostname": "1.2.3.4",
                },
                "facts": {
                    "device_type": "switch",
                    "alternate_management_interface": {
                        "enabled": True,
                        "vlan_id": 100,
                        "protocols": ["radius", "snmp", "syslog"],
                        "alternate_management_ip": "1.2.3.4",
                        "subnet_mask": "255.255.255.0",
                        "gateway": "1.2.3.5",
                    },
                },
            }
        ]
    ]

    # Assert results match expected output
    assert (
        results == expected
    ), f"Query results do not match expected output for {method_name}"
