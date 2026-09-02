"""
Test for cisco.meraki.devices_wireless_alternate_management_interface_ipv6 using fixture cisco.meraki.devices_wireless_alternate_management_interface_ipv6.json
Method: updateDeviceWirelessAlternateManagementInterfaceIpv6
"""
import jq


def test_cisco_meraki_devices_wireless_alternate_management_interface_ipv6_updateDeviceWirelessAlternateManagementInterfaceIpv6(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_wireless_alternate_management_interface_ipv6 (updateDeviceWirelessAlternateManagementInterfaceIpv6)."""
    module_fqcn = "cisco.meraki.devices_wireless_alternate_management_interface_ipv6"
    method_name = "updateDeviceWirelessAlternateManagementInterfaceIpv6"

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
                    "device_type": "wireless",
                    "protocol": "ipv6",
                    "assignment_mode": "static",
                    "address": "2001:db8:3c4d:15::1",
                    "gateway": "fe80:db8:c15:c0:d0c::10ca:1d02",
                    "prefix": "2001:db8:3c4d:15::/64",
                    "nameservers": ["2001:db8:3c4d:15::1", "2001:db8:3c4d:15::1"]
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q2FV-DJ6J-4QHD"
                }
            },
            {
                "facts": {
                    "device_type": "wireless",
                    "protocol": "ipv6",
                    "assignment_mode": "static",
                    "address": "2001:db8:3c4d:15::2",
                    "gateway": "fe80:db8:c15:c0:d0c::10ca:1d02",
                    "prefix": "2001:db8:3c4d:15::/64",
                    "nameservers": ["2001:db8:3c4d:15::2", "2001:db8:3c4d:15::2"]
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q2FV-DJ6J-4QHD"
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
