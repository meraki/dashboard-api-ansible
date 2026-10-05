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
                "name": "wireless-ipv6-Q2FV-DJ6J-4QHD",
                "facts": {
                    "device_type": "wireless_access_point",
                    "infra_type": "private_cloud",
                    "infra_bucket": "networking",
                    "addresses": [
                        {
                            "protocol": "ipv6",
                            "assignment_mode": "static",
                            "address": "2001:db8:3c4d:15::1",
                            "gateway": "fe80:db8:c15:c0:d0c::10ca:1d02",
                            "prefix": "2001:db8:3c4d:15::/64",
                            "nameservers": [
                                "2001:db8:3c4d:15::1",
                                "2001:db8:3c4d:15::1",
                            ],
                        },
                        {
                            "protocol": "ipv6",
                            "assignment_mode": "static",
                            "address": "2001:db8:3c4d:15::2",
                            "gateway": "fe80:db8:c15:c0:d0c::10ca:1d02",
                            "prefix": "2001:db8:3c4d:15::/64",
                            "nameservers": [
                                "2001:db8:3c4d:15::2",
                                "2001:db8:3c4d:15::2",
                            ],
                        },
                    ],
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q2FV-DJ6J-4QHD"
                },
            }
        ]
    ]
    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"


def test_cisco_meraki_devices_wireless_alternate_management_interface_ipv6_missing_nameservers(query_data):
    """Missing nameserver objects do not prevent an IPv6 result from being emitted."""
    module_fqcn = "cisco.meraki.devices_wireless_alternate_management_interface_ipv6"
    response = {
        "invocation": {"module_args": {"serial": "Q234-ABCD-5678"}},
        "meraki_response": {"addresses": [{"address": "2001:db8::1"}]},
    }
    results = jq.compile(query_data[module_fqcn]["query"]).input(response).all()
    expected = [[{
        "name": "wireless-ipv6-Q234-ABCD-5678",
        "facts": {
            "device_type": "wireless_access_point",
            "infra_type": "private_cloud",
            "infra_bucket": "networking",
            "addresses": [{
                "protocol": None,
                "assignment_mode": None,
                "address": "2001:db8::1",
                "gateway": None,
                "prefix": None,
                "nameservers": [],
            }],
        },
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"},
    }]]
    assert results == expected
