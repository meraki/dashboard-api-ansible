"""
Test for cisco.meraki.devices_camera_video_link_info using fixture cisco.meraki.devices_camera_video_link_info.json
Method: getDeviceCameraVideoLink
"""
import jq


def test_cisco_meraki_devices_camera_video_link_info_getDeviceCameraVideoLink(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_camera_video_link_info (getDeviceCameraVideoLink)."""
    module_fqcn = "cisco.meraki.devices_camera_video_link_info"
    method_name = "getDeviceCameraVideoLink"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
        "device_type": "camera",
        "url": "https://n123.meraki.com/cameras/#uuid=abc123",
        "vision_url": "https://vision.meraki.com/abc123"
},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
