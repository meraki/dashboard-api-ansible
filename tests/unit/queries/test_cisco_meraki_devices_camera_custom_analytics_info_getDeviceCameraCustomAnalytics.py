"""
Test for cisco.meraki.devices_camera_custom_analytics_info using fixture cisco.meraki.devices_camera_custom_analytics_info.json
Method: getDeviceCameraCustomAnalytics
"""
import jq


def test_cisco_meraki_devices_camera_custom_analytics_info_getDeviceCameraCustomAnalytics(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_camera_custom_analytics_info (getDeviceCameraCustomAnalytics)."""
    module_fqcn = "cisco.meraki.devices_camera_custom_analytics_info"
    method_name = "getDeviceCameraCustomAnalytics"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
        "device_type": "camera",
        "enabled": True,
        "artifact_id": "artifact-001",
        "parameters": [
                {
                        "name": "threshold",
                        "value": 0.5
                }
        ]
},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
