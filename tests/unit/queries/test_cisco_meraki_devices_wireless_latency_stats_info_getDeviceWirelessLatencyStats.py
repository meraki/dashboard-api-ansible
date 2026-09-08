"""
Test for cisco.meraki.devices_wireless_latency_stats_info using fixture cisco.meraki.devices_wireless_latency_stats_info.json
Method: getDeviceWirelessLatencyStats
"""
import jq


def test_cisco_meraki_devices_wireless_latency_stats_info_getDeviceWirelessLatencyStats(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_wireless_latency_stats_info (getDeviceWirelessLatencyStats)."""
    module_fqcn = "cisco.meraki.devices_wireless_latency_stats_info"
    method_name = "getDeviceWirelessLatencyStats"

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
                    "ansible_product_serial": "Q2JC-2MJM-FHRD"
                },
                "facts": {
                    "device_type": "wireless",
                    "latency_stats": {
                        "background_traffic_avg": 606.52,
                        "best_effort_traffic_avg": 606.52,
                        "video_traffic_avg": 606.52,
                        "voice_traffic_avg": 606.52
                    }
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
