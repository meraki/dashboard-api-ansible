"""
Test for cisco.meraki.organizations_summary_top_appliances_by_utilization_info using fixture cisco.meraki.organizations_summary_top_appliances_by_utilization_info.json
Method: getOrganizationSummaryTopAppliancesByUtilization
"""
import jq


def test_cisco_meraki_organizations_summary_top_appliances_by_utilization_info_getOrganizationSummaryTopAppliancesByUtilization(query_data, load_fixture):
    """Test query execution for cisco.meraki.organizations_summary_top_appliances_by_utilization_info (getOrganizationSummaryTopAppliancesByUtilization)."""
    module_fqcn = "cisco.meraki.organizations_summary_top_appliances_by_utilization_info"
    method_name = "getOrganizationSummaryTopAppliancesByUtilization"

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
                    "device_type": "appliance",
                    "model": "MX68",
                    "mac": "00:11:22:33:44:55",
                    "network": {
                        "id": "N_123",
                        "name": "HQ"
                    },
                    "utilization_avg_percentage": 15.3
                }
            },
            {
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-0002"
                },
                "facts": {
                    "device_type": "appliance",
                    "model": "MX67",
                    "mac": "00:11:22:33:44:66",
                    "network": {
                        "id": "N_456",
                        "name": "Branch"
                    },
                    "utilization_avg_percentage": 8.1
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
