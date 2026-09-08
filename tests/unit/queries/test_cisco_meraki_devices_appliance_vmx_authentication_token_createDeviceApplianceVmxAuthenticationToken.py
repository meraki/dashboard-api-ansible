"""
Test for cisco.meraki.devices_appliance_vmx_authentication_token using fixture cisco.meraki.devices_appliance_vmx_authentication_token.json
Method: createDeviceApplianceVmxAuthenticationToken
"""
import jq


def test_cisco_meraki_devices_appliance_vmx_authentication_token_createDeviceApplianceVmxAuthenticationToken(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_appliance_vmx_authentication_token (createDeviceApplianceVmxAuthenticationToken)."""
    module_fqcn = "cisco.meraki.devices_appliance_vmx_authentication_token"
    method_name = "createDeviceApplianceVmxAuthenticationToken"

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
                    "device_type": "appliance",
                    "token": "abc123xyz",
                    "expires_at": "2026-08-18T12:00:00Z"
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
