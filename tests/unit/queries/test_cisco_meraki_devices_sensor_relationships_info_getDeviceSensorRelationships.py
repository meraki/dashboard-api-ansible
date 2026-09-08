"""
Test for cisco.meraki.devices_sensor_relationships_info using fixture cisco.meraki.devices_sensor_relationships_info.json
Method: getDeviceSensorRelationships
"""
import jq


def test_cisco_meraki_devices_sensor_relationships_info_getDeviceSensorRelationships(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_sensor_relationships_info (getDeviceSensorRelationships)."""
    module_fqcn = "cisco.meraki.devices_sensor_relationships_info"
    method_name = "getDeviceSensorRelationships"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
            "device_type": "sensor",
            "related_devices": [
                {"serial": "Q2GV-ABCD-1111", "product_type": "camera"}
            ]
        },
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
