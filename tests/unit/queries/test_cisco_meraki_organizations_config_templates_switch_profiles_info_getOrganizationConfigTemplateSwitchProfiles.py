"""
Test for cisco.meraki.organizations_config_templates_switch_profiles_info using fixture cisco.meraki.organizations_config_templates_switch_profiles_info.json
Method: getOrganizationConfigTemplateSwitchProfiles
"""
import jq


def test_cisco_meraki_organizations_config_templates_switch_profiles_info_getOrganizationConfigTemplateSwitchProfiles(query_data, load_fixture):
    """Test query execution for cisco.meraki.organizations_config_templates_switch_profiles_info (getOrganizationConfigTemplateSwitchProfiles)."""
    module_fqcn = "cisco.meraki.organizations_config_templates_switch_profiles_info"
    method_name = "getOrganizationConfigTemplateSwitchProfiles"

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
                "name": "A Simple Switch Template",
                "canonical_facts": {
                    "ansible_machine_id": "1234"
                },
                "facts": {
                    "device_type": "switch",
                    "switch_profile": {
                        "profile_id": "1234",
                        "name": "A Simple Switch Template",
                        "model": "MS450-24"
                    }
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
