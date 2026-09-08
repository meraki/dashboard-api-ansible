"""
Test for cisco.meraki.devices_camera_wireless_profiles using fixture cisco.meraki.devices_camera_wireless_profiles.json
Method: updateDeviceCameraWirelessProfiles
"""
import jq


def test_cisco_meraki_devices_camera_wireless_profiles_updateDeviceCameraWirelessProfiles(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_camera_wireless_profiles (updateDeviceCameraWirelessProfiles)."""
    module_fqcn = "cisco.meraki.devices_camera_wireless_profiles"
    method_name = "updateDeviceCameraWirelessProfiles"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
        "device_type": "camera",
        "primary": "profile-001",
        "secondary": "profile-002",
        "backup": "profile-003"
},
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
