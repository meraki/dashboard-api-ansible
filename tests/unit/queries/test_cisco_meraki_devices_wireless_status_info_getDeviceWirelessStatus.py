"""
Test for cisco.meraki.devices_wireless_status_info using fixture cisco.meraki.devices_wireless_status_info.json
Method: getDeviceWirelessStatus
"""
import jq


def test_cisco_meraki_devices_wireless_status_info_getDeviceWirelessStatus(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_wireless_status_info (getDeviceWirelessStatus)."""
    module_fqcn = "cisco.meraki.devices_wireless_status_info"
    method_name = "getDeviceWirelessStatus"
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
                "name": "wireless-status-Q234-ABCD-5678",
                "facts": {
                    "device_type": "wireless_access_point",
                    "infra_type": "private_cloud",
                    "infra_bucket": "networking",
                    "basic_service_sets": [
                        {
                            "ssid_number": 0,
                            "ssid_name": "My SSID",
                            "enabled": True,
                            "band": "2.4 GHz",
                            "bssid": "8A:15:04:00:00:00",
                            "channel": 11,
                            "channel_width": "20 MHz",
                            "power": "18 dBm",
                            "visible": True,
                            "broadcasting": True,
                        },
                        {
                            "ssid_number": 0,
                            "ssid_name": "My SSID",
                            "enabled": True,
                            "band": "5 GHz",
                            "bssid": "8A:15:04:00:00:01",
                            "channel": 149,
                            "channel_width": "80 MHz",
                            "power": "20 dBm",
                            "visible": True,
                            "broadcasting": True,
                        },
                    ],
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                },
            }
        ]
    ]
    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"


def test_cisco_meraki_devices_wireless_status_info_empty_service_sets(query_data):
    """Missing basicServiceSets produces one device-level result with an empty list."""
    module_fqcn = "cisco.meraki.devices_wireless_status_info"
    response = {
        "invocation": {"module_args": {"serial": "Q234-ABCD-5678"}},
        "meraki_response": {},
    }
    results = jq.compile(query_data[module_fqcn]["query"]).input(response).all()
    expected = [[{
        "name": "wireless-status-Q234-ABCD-5678",
        "facts": {"device_type": "wireless_access_point", "infra_type": "private_cloud", "infra_bucket": "networking", "basic_service_sets": []},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"},
    }]]
    assert results == expected
