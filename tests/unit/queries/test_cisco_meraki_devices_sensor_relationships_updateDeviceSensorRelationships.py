"""
Test for cisco.meraki.devices_sensor_relationships using fixture cisco.meraki.devices_sensor_relationships.json
Method: updateDeviceSensorRelationships
"""
import jq


def test_cisco_meraki_devices_sensor_relationships_updateDeviceSensorRelationships(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_sensor_relationships (updateDeviceSensorRelationships)."""
    module_fqcn = "cisco.meraki.devices_sensor_relationships"
    method_name = "updateDeviceSensorRelationships"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    results = jq.compile(query_data[module_fqcn]["query"]).input(final_response).all()

    expected = [[{
        "facts": {
            "device_type": "sensor",
            "related_devices": [
                {"serial": "Q2GV-ABCD-1111", "product_type": "camera"},
                {"serial": "Q2GV-ABCD-2222", "product_type": "camera"}
            ]
        },
        "canonical_facts": {"ansible_product_serial": "Q234-ABCD-5678"}
    }]]

    assert results == expected, f"Query results do not match expected output for {method_name}"
