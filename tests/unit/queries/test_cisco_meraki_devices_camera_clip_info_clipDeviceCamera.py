"""
Test for cisco.meraki.devices_camera_clip_info using fixture cisco.meraki.devices_camera_clip_info.json
Method: clipDeviceCamera
"""
import jq


def test_cisco_meraki_devices_camera_clip_info_clipDeviceCamera(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_camera_clip_info (clipDeviceCamera)."""
    module_fqcn = "cisco.meraki.devices_camera_clip_info"
    method_name = "clipDeviceCamera"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
        "device_type": "camera",
        "url": "https://example.com/clip.mp4",
        "expiry": "2026-08-18T12:00:00Z"
},
        "canonical_facts": {"ansible_product_serial": "Q2FV-DJ6J-4QHD"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
