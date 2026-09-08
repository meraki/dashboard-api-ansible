"""
Test for cisco.meraki.devices_cellular_uplinks_bands_masks_update using fixture cisco.meraki.devices_cellular_uplinks_bands_masks_update.json
Method: createDeviceCellularUplinksBandsMasksUpdate
"""
import jq


def test_cisco_meraki_devices_cellular_uplinks_bands_masks_update_createDeviceCellularUplinksBandsMasksUpdate(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_cellular_uplinks_bands_masks_update (createDeviceCellularUplinksBandsMasksUpdate)."""
    module_fqcn = "cisco.meraki.devices_cellular_uplinks_bands_masks_update"
    method_name = "createDeviceCellularUplinksBandsMasksUpdate"

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
                    "by_slot": [
                        {
                            "slot": "sim1",
                            "by_signal_type": [
                                {"type": "lte", "masked": ["B2", "B4"], "enabled": ["B1", "B3"], "supported": ["B1", "B2", "B3", "B4"]},
                                {"type": "5gnr", "masked": [], "enabled": ["n77"], "supported": ["n77"]}
                            ]
                        },
                        {
                            "slot": "sim2",
                            "by_signal_type": [
                                {"type": "lte", "masked": [], "enabled": ["B1", "B2"], "supported": ["B1", "B2"]}
                            ]
                        }
                    ]
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                }
            }
        ]
    ]

    assert results == expected, f"Query results do not match expected output for {method_name}"
