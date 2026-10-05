"""
Test for cisco.meraki.devices_camera_video_settings using fixture cisco.meraki.devices_camera_video_settings.json
Method: updateDeviceCameraVideoSettings
"""
import jq


def test_cisco_meraki_devices_camera_video_settings_updateDeviceCameraVideoSettings(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_camera_video_settings (updateDeviceCameraVideoSettings)."""
    module_fqcn = "cisco.meraki.devices_camera_video_settings"
    method_name = "updateDeviceCameraVideoSettings"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "name": "camera-video-settings-Q234-ABCD-5678",
        "facts": {
        "device_type": "ip_camera",
        "infra_type": "private_cloud",
        "infra_bucket": "monitoring",
        "external_rtsp_enabled": True,
        "rtsp_url": "rtsp://10.0.0.1:9000/live"
},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
