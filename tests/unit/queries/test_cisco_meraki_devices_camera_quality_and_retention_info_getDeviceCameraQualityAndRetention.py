"""
Test for cisco.meraki.devices_camera_quality_and_retention_info using fixture cisco.meraki.devices_camera_quality_and_retention_info.json
Method: getDeviceCameraQualityAndRetention
"""
import jq


def test_cisco_meraki_devices_camera_quality_and_retention_info_getDeviceCameraQualityAndRetention(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_camera_quality_and_retention_info (getDeviceCameraQualityAndRetention)."""
    module_fqcn = "cisco.meraki.devices_camera_quality_and_retention_info"
    method_name = "getDeviceCameraQualityAndRetention"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
        "device_type": "camera",
        "profile_id": "1234",
        "quality": "Enhanced",
        "resolution": "1280x720",
        "motion_based_retention_enabled": True,
        "audio_recording_enabled": False,
        "restricted_bandwidth_mode_enabled": False,
        "motion_detector_version": 2
},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
