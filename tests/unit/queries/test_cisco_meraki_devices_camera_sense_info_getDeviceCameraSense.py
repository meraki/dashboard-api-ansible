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
        "name": "camera-sense-Q234-ABCD-5678",
        "facts": {
        "device_type": "ip_camera",
        "infra_type": "private_cloud",
        "infra_bucket": "monitoring",
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


def test_cisco_meraki_devices_camera_sense_info_missing_audio_detection(query_data):
    module_fqcn = "cisco.meraki.devices_camera_sense_info"
    response = {
        "invocation": {"module_args": {"serial": "Q234-ABCD-5678"}},
        "meraki_response": {},
    }
    results = jq.compile(query_data[module_fqcn]["query"]).input(response).all()
    expected = [[{
        "name": "camera-sense-Q234-ABCD-5678",
        "facts": {"device_type": "ip_camera", "infra_type": "private_cloud", "infra_bucket": "monitoring", "sense_enabled": None, "mqtt_broker_id": None, "mqtt_topics": [], "audio_detection_enabled": False, "detection_model_id": None},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"},
    }]]
    assert results == expected
