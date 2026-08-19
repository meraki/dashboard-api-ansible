"""
Test for cisco.meraki.devices_cellular_gateway_lan_info using fixture cisco.meraki.devices_cellular_gateway_lan_info.json
Method: getDeviceCellularGatewayLan
"""
import jq


def test_cisco_meraki_devices_cellular_gateway_lan_info_getDeviceCellularGatewayLan(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_cellular_gateway_lan_info (getDeviceCellularGatewayLan)."""
    module_fqcn = "cisco.meraki.devices_cellular_gateway_lan_info"
    method_name = "getDeviceCellularGatewayLan"

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
                    "device_name": "My MG",
                    "device_lan_ip": "192.168.0.1",
                    "device_subnet": "192.168.0.0/24",
                    "fixed_ip_assignments": [
                        {
                            "name": "My Device",
                            "ip": "192.168.0.10",
                            "mac": "00:11:22:33:44:55"
                        }
                    ],
                    "reserved_ip_ranges": [
                        {
                            "start": "192.168.0.100",
                            "end": "192.168.0.200",
                            "comment": "Reserved"
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
