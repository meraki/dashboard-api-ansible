"""
Test for cisco.meraki.devices_cellular_gateway_port_forwarding_rules_info using fixture cisco.meraki.devices_cellular_gateway_port_forwarding_rules_info.json
Method: getDeviceCellularGatewayPortForwardingRules
"""
import jq


def test_cisco_meraki_devices_cellular_gateway_port_forwarding_rules_info_getDeviceCellularGatewayPortForwardingRules(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_cellular_gateway_port_forwarding_rules_info (getDeviceCellularGatewayPortForwardingRules)."""
    module_fqcn = "cisco.meraki.devices_cellular_gateway_port_forwarding_rules_info"
    method_name = "getDeviceCellularGatewayPortForwardingRules"

    # Load fixture data
    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    # Fixture already contains invocation + meraki_response at top level
    final_response = response

    # Get query from query_data
    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    jq_query = query_data[module_fqcn]["query"]

    # Execute query
    results = jq.compile(jq_query).input(final_response).all()

    # Expected output
    expected = [
        [
            {
                "facts": {
                    "device_type": "cellular",
                    "rules": [
                        {
                            "name": "Rule 1",
                            "lan_ip": "192.168.128.1",
                            "public_port": "8080",
                            "local_port": "80",
                            "protocol": "tcp",
                            "access": "any",
                            "allowed_ips": ["any"]
                        },
                        {
                            "name": "Rule 2",
                            "lan_ip": "192.168.128.2",
                            "public_port": "8443",
                            "local_port": "443",
                            "protocol": "tcp",
                            "access": "any",
                            "allowed_ips": ["any"]
                        }
                    ]
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
