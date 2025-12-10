"""
Test for cisco.meraki.networks_switch_qos_rules_order_info using fixture cisco.meraki.networks_switch_qos_rules_order_info.json
Method: getNetworkSwitchQosRule
"""
import jq
import pytest


def test_cisco_meraki_networks_switch_qos_rules_order_info_getNetworkSwitchQosRule(query_data, load_fixture):
    """Test query execution for cisco.meraki.networks_switch_qos_rules_order_info (getNetworkSwitchQosRule)."""
    module_fqcn = "cisco.meraki.networks_switch_qos_rules_order_info"
    method_name = "getNetworkSwitchQosRule"
    
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
            "name": "qos-rule-1284392014819",
            "canonical_facts": {
                "ansible_machine_id": "1284392014819"
            },
            "facts": {
                "device_type": "switch",
                "qos_rule": {
                    "id": "1284392014819",
                    "vlan": 100,
                    "protocol": "TCP",
                    "src_port": 2000,
                    "src_port_range": "70-80",
                    "dst_port": 3000,
                    "dst_port_range": "3000-3100",
                    "dscp": 0
                }
            }
        }
    ]
]
    
    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
