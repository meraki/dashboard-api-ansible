"""
Test for cisco.meraki.organizations_cellular_gateway_uplink_statuses_info using fixture cisco.meraki.organizations_cellular_gateway_uplink_statuses_info.json
Method: getOrganizationCellularGatewayUplinkStatuses
"""
import jq


def test_cisco_meraki_organizations_cellular_gateway_uplink_statuses_info_getOrganizationCellularGatewayUplinkStatuses(query_data, load_fixture):
    """Test query execution for cisco.meraki.organizations_cellular_gateway_uplink_statuses_info (getOrganizationCellularGatewayUplinkStatuses)."""
    module_fqcn = "cisco.meraki.organizations_cellular_gateway_uplink_statuses_info"
    method_name = "getOrganizationCellularGatewayUplinkStatuses"

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

    # Expected output
    expected = [
        [
            {
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-0001"
                },
                "facts": {
                    "device_type": "cellular",
                    "model": "MG21",
                    "network_id": "N_123",
                    "last_reported_at": "2026-08-18T10:00:00Z",
                    "uplinks": [
                        {
                            "interface": "wan1",
                            "status": "active",
                            "ip": "1.2.3.4",
                            "provider": "Verizon",
                            "public_ip": "5.6.7.8",
                            "connection_type": "4g",
                            "apn": "internet",
                            "signal_type": "LTE",
                            "iccid": "1234567890"
                        },
                        {
                            "interface": "wan2",
                            "status": "failed",
                            "ip": "",
                            "provider": "AT&T",
                            "public_ip": "",
                            "connection_type": "4g",
                            "apn": "mobile.att.com",
                            "signal_type": "LTE",
                            "iccid": "0987654321"
                        }
                    ]
                }
            },
            {
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-0002"
                },
                "facts": {
                    "device_type": "cellular",
                    "model": "MG29",
                    "network_id": "N_456",
                    "last_reported_at": "2026-08-18T09:30:00Z",
                    "uplinks": [
                        {
                            "interface": "wan1",
                            "status": "active",
                            "ip": "9.10.11.12",
                            "provider": "T-Mobile",
                            "public_ip": "13.14.15.16",
                            "connection_type": "5g",
                            "apn": "fast.t-mobile.com",
                            "signal_type": "NR",
                            "iccid": "1111111111"
                        }
                    ]
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
