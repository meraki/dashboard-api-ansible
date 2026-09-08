"""
Test for cisco.meraki.devices_cellular_geolocations using fixture cisco.meraki.devices_cellular_geolocations.json
Method: updateDeviceCellularGeolocations
"""
import jq


def test_cisco_meraki_devices_cellular_geolocations_updateDeviceCellularGeolocations(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_cellular_geolocations (updateDeviceCellularGeolocations)."""
    module_fqcn = "cisco.meraki.devices_cellular_geolocations"
    method_name = "updateDeviceCellularGeolocations"

    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    final_response = response  # invocation-based

    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    jq_query = query_data[module_fqcn]["query"]

    results = jq.compile(jq_query).input(final_response).all()

    expected = [
        [
            {
                "facts": {
                    "device_type": "cellular",
                    "enabled": True
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                }
            }
        ]
    ]

    assert results == expected, f"Query results do not match expected output for {method_name}"
