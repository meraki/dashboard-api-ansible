"""
Test for cisco.meraki.organizations_switch_ports_by_switch_info using fixture cisco.meraki.organizations_switch_ports_by_switch_info.json
Method: getOrganizationSwitchPortsBySwitch
"""
import jq


def test_cisco_meraki_organizations_switch_ports_by_switch_info_getOrganizationSwitchPortsBySwitch(query_data, load_fixture):
    """Test query execution for cisco.meraki.organizations_switch_ports_by_switch_info (getOrganizationSwitchPortsBySwitch)."""
    module_fqcn = "cisco.meraki.organizations_switch_ports_by_switch_info"
    method_name = "getOrganizationSwitchPortsBySwitch"

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
                "name": "Example Switch",
                "canonical_facts": {
                    "ansible_product_serial": "Q555-5555-5555",
                    "hostname": "01:23:45:67:ab:cd"
                },
                "facts": {
                    "device_type": "switch",
                    "mac_address": "01:23:45:67:ab:cd",
                    "model": "MS120-8",
                    "switch_info": {
                        "network_name": "Example Network",
                        "network_id": "L_12345"
                    }
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
