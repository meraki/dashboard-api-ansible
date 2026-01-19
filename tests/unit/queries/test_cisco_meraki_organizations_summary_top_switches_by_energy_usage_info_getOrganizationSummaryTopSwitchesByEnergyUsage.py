"""
Test for cisco.meraki.organizations_summary_top_switches_by_energy_usage_info using fixture
    cisco.meraki.organizations_summary_top_switches_by_energy_usage_info.json
Method: getOrganizationSummaryTopSwitchesByEnergyUsage
"""
import jq


def test_cisco_meraki_organizations_summary_top_switches_by_energy_usage_info_getOrganizationSummaryTopSwitchesByEnergyUsage(query_data, load_fixture):
    """Test query execution for cisco.meraki.organizations_summary_top_switches_by_energy_usage_info (getOrganizationSummaryTopSwitchesByEnergyUsage)."""
    module_fqcn = "cisco.meraki.organizations_summary_top_switches_by_energy_usage_info"
    method_name = "getOrganizationSummaryTopSwitchesByEnergyUsage"

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
                "canonical_facts": {
                    "ansible_machine_id": "00:11:22:33:44:55"
                },
                "facts": {
                    "device_type": "switch",
                    "switch_info": {
                        "name": "My switch",
                        "model": "MS",
                        "mac_address": "00:11:22:33:44:55"
                    },
                    "network": {
                        "id": "N_24329156",
                        "name": "Main Office"
                    },
                    "energy_usage": {
                        "total": 800.021
                    }
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
