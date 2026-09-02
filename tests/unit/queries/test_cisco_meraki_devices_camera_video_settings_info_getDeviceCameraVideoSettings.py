"""
Test for cisco.meraki.devices_camera_video_settings_info using fixture cisco.meraki.devices_camera_video_settings_info.json
Method: getDeviceCameraVideoSettings
"""
import jq


def test_cisco_meraki_devices_camera_video_settings_info_getDeviceCameraVideoSettings(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_camera_video_settings_info (getDeviceCameraVideoSettings)."""
    module_fqcn = "cisco.meraki.devices_camera_video_settings_info"
    method_name = "getDeviceCameraVideoSettings"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
        "device_type": "camera",
        "external_rtsp_enabled": True,
        "rtsp_url": "rtsp://10.0.0.1:9000/live"
},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
