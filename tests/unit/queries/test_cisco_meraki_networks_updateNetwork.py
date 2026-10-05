"""Tests for the administrative-network query."""

import jq


def test_cisco_meraki_networks_does_not_emit_a_device_type(query_data, load_fixture):
    """Networks are administrative containers, not countable device nodes."""
    module_fqcn = "cisco.meraki.networks"
    response = load_fixture(module_fqcn)

    results = jq.compile(query_data[module_fqcn]["query"]).input(response).all()

    assert results == [
        [
            {
                "name": "Administrative network",
                "canonical_facts": {"ansible_machine_id": "N_123"},
                "facts": {
                    "infra_type": "private_cloud",
                    "infra_bucket": "networking","meraki_organization_id": "O_123"},
            }
        ]
    ]
