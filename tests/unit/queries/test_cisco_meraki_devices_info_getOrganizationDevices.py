"""
Test for cisco.meraki.devices_info using fixture cisco.meraki.devices_info.json
Method: getOrganizationDevices
"""

import jq


def test_cisco_meraki_devices_info_getOrganizationDevices(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_info (getOrganizationDevices)."""
    module_fqcn = "cisco.meraki.devices_info"
    method_name = "getOrganizationDevices"

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
                "name": "My AP",
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678",
                    "hostname": "1.2.3.4",
                },
                "facts": {
                    "device_type": "wireless",
                    "meraki_network_id": "N_24329156",
                    "ansible_hostname": "1.2.3.4",
                    "ansible_product_name": "MR34",
                    "ansible_bios_version": "wireless-25-14",
                    "macaddress": "00:11:22:33:44:55",
                },
            },
            {
                "name": "My AP 2",
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5679",
                    "hostname": "1.2.3.4",
                },
                "facts": {
                    "device_type": "wireless",
                    "meraki_network_id": "N_24329157",
                    "ansible_hostname": "1.2.3.4",
                    "ansible_product_name": "MR34",
                    "ansible_bios_version": "wireless-25-14",
                    "macaddress": "00:11:22:33:44:55",
                },
            },
        ]
    ]

    # Assert results match expected output
    assert (
        results == expected
    ), f"Query results do not match expected output for {method_name}"
