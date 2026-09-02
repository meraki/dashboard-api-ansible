"""
Test for cisco.meraki.devices_camera_generate_snapshot using fixture cisco.meraki.devices_camera_generate_snapshot.json
Method: generateDeviceCameraSnapshot
"""
import jq


def test_cisco_meraki_devices_camera_generate_snapshot_generateDeviceCameraSnapshot(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_camera_generate_snapshot (generateDeviceCameraSnapshot)."""
    module_fqcn = "cisco.meraki.devices_camera_generate_snapshot"
    method_name = "generateDeviceCameraSnapshot"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
        "device_type": "camera",
        "url": "https://example.com/snapshot.jpg",
        "expiry": "2026-08-18T10:05:00Z"
},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
