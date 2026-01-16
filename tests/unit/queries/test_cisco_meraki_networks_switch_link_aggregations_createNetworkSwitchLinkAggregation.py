"""
Test for cisco.meraki.networks_switch_link_aggregations using fixture cisco.meraki.networks_switch_link_aggregations.json
Method: createNetworkSwitchLinkAggregation
"""
import jq


def test_cisco_meraki_networks_switch_link_aggregations_createNetworkSwitchLinkAggregation(query_data, load_fixture):
    """Test query execution for cisco.meraki.networks_switch_link_aggregations (createNetworkSwitchLinkAggregation)."""
    module_fqcn = "cisco.meraki.networks_switch_link_aggregations"
    method_name = "createNetworkSwitchLinkAggregation"

    # Load fixture data
    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    # Prepare response in expected format
    final_response = {"meraki_response": response}

    # Get query from query_data
    assert module_fqcn in query_data, f"Query not found for {module_fqcn}"
    jq_query = query_data[module_fqcn]["query"]

    # Execute query
    results = jq.compile(jq_query).input(final_response).all()

    # Expected output from query_run.log
    expected = [
    [
        {
            "name": "Q234-ABCD-0001-port-1",
            "canonical_facts": {
                "ansible_product_serial": "Q234-ABCD-0001"
            },
            "facts": {
                "device_type": "switch",
                "link_aggregation": {
                    "aggregation_id": "NDU2N18yXzM=",
                    "port_id": "1",
                    "serial": "Q234-ABCD-0001"
                }
            }
        }
    ]
]

    # Assert results match expected output
    assert results == expected, f"Query results do not match expected output for {method_name}"
