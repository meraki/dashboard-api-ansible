"""
Test for cisco.meraki.devices_camera_sense_info using fixture cisco.meraki.devices_camera_sense_info.json
Method: getDeviceCameraSense
"""
import jq


def test_cisco_meraki_devices_camera_sense_info_getDeviceCameraSense(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_camera_sense_info (getDeviceCameraSense)."""
    module_fqcn = "cisco.meraki.devices_camera_sense_info"
    method_name = "getDeviceCameraSense"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
        "device_type": "camera",
        "sense_enabled": True,
        "mqtt_broker_id": "broker-001",
        "mqtt_topics": [
                "/merakimv/Q234/raw_detections"
        ],
        "audio_detection_enabled": True,
        "detection_model_id": "model-001"
},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
