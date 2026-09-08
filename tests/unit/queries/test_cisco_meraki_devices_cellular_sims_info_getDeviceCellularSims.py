"""
Test for cisco.meraki.devices_cellular_sims_info using fixture cisco.meraki.devices_cellular_sims_info.json
Method: getDeviceCellularSims
"""
import jq


def test_cisco_meraki_devices_cellular_sims_info_getDeviceCellularSims(query_data, load_fixture):
    """Test query execution for cisco.meraki.devices_cellular_sims_info (getDeviceCellularSims)."""
    module_fqcn = "cisco.meraki.devices_cellular_sims_info"
    method_name = "getDeviceCellularSims"

    # Load fixture data
    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    # Fixture already contains invocation + meraki_response at top level
    final_response = response

    # Get query from query_data
    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    jq_query = query_data[module_fqcn]["query"]

    # Execute query
    results = jq.compile(jq_query).input(final_response).all()

    # Expected output
    expected = [
        [
            {
                "facts": {
                    "device_type": "cellular",
                    "sims": [
                        {
                            "slot": "sim1",
                            "iccid": "1234567890",
                            "is_primary": True,
                            "status": "ready"
                        },
                        {
                            "slot": "sim2",
                            "iccid": "0987654321",
                            "is_primary": False,
                            "status": "not connected"
                        }
                    ],
                    "sim_failover_enabled": True,
                    "sim_ordering": ["sim1", "sim2"]
                },
                "canonical_facts": {
                    "ansible_product_serial": "Q234-ABCD-5678"
                }
            }
        ]
    ]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
