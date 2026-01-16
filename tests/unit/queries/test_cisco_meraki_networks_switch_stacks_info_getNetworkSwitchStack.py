"""
Test for cisco.meraki.networks_switch_stacks_info using fixture cisco.meraki.networks_switch_stacks_info.json
Method: getNetworkSwitchStack
"""

import jq


def test_cisco_meraki_networks_switch_stacks_info_getNetworkSwitchStack(
    query_data, load_fixture
):
    """Test query execution for cisco.meraki.networks_switch_stacks_info (getNetworkSwitchStack)."""
    module_fqcn = "cisco.meraki.networks_switch_stacks_info"
    method_name = "getNetworkSwitchStack"

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
                "name": "QBZY-XWVU-TSRQ",
                "canonical_facts": {"ansible_product_serial": "QBZY-XWVU-TSRQ"},
                "facts": {
                    "device_type": "switch",
                    "stack_id": "8473",
                    "stack_name": "A cool stack",
                    "virtual_mac": "00:18:0a:4f:21:19",
                    "is_monitor_only": False,
                },
            },
            {
                "name": "QBAB-CDEF-GHIJ",
                "canonical_facts": {"ansible_product_serial": "QBAB-CDEF-GHIJ"},
                "facts": {
                    "device_type": "switch",
                    "stack_id": "8473",
                    "stack_name": "A cool stack",
                    "virtual_mac": "00:18:0a:4f:21:19",
                    "is_monitor_only": False,
                },
            },
        ]
    ]

    # Assert results match expected output
    assert (
        results == expected
    ), f"Query results do not match expected output for {method_name}"
