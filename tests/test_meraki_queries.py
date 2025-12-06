"""
Pytest tests for Meraki JQ query transformations.

These tests validate that JQ queries correctly transform Meraki API responses
into the standardized IndirectManagedNodeAudit schema format.
"""

import jq
import json
import pytest


class TestMerakiQueries:
    """Test suite for Meraki query transformations."""

    @pytest.mark.parametrize(
        "module_fqcn,method_name",
        [
            ("cisco.meraki.networks_switch_mtu_info", "getNetworkSwitchMtu"),
            ("cisco.meraki.devices_info", "getOrganizationDevices"),
            ("cisco.meraki.devices_switch_ports_info", "getDeviceSwitchPort"),
            ("cisco.meraki.networks_switch_stacks_info", "getNetworkSwitchStack"),
            (
                "cisco.meraki.networks_switch_stacks_routing_interfaces_info",
                "getNetworkSwitchStackRoutingInterfaces",
            ),
            ("cisco.meraki.devices_switch_ports", "updateDeviceSwitchPort"),
            (
                "cisco.meraki.organizations_switch_ports_by_switch_info",
                "getOrganizationSwitchPortsBySwitch",
            ),
            (
                "cisco.meraki.devices_switch_ports_statuses_info",
                "getDeviceSwitchPortsStatuses",
            ),
            (
                "cisco.meraki.networks_switch_access_policies_info",
                "getNetworkSwitchAccessPolicies",
            ),
            (
                "cisco.meraki.networks_switch_settings_info",
                "getNetworkSwitchSettings",
            ),
            (
                "cisco.meraki.networks_switch_access_policies",
                "updateNetworkSwitchAccessPolicy",
            ),
            (
                "cisco.meraki.networks_switch_stacks_routing_interfaces",
                "createNetworkSwitchStackRoutingInterface",
            ),
            (
                "cisco.meraki.networks_switch_stp_info",
                "getNetworkSwitchStp",
            ),
            (
                "cisco.meraki.networks_switch_qos_rules_order",
                "createNetworkSwitchQosRule",
            ),
            (
                "cisco.meraki.devices_switch_ports_cycle",
                "cycleDeviceSwitchPorts",
            ),
            (
                "cisco.meraki.networks_switch_access_control_lists_info",
                "getNetworkSwitchAccessControlLists",
            ),
            (
                "cisco.meraki.networks_switch_stacks",
                "createNetworkSwitchStack",
            ),
            (
                "cisco.meraki.networks_switch_settings",
                "updateNetworkSwitchSettings",
            ),
            (
                "cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp_info",
                "getNetworkSwitchStackRoutingInterfaceDhcp",
            ),
            (
                "cisco.meraki.networks_switch_access_policies",
                "createNetworkSwitchAccessPolicy",
            ),
            (
                "cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp",
                "updateNetworkSwitchStackRoutingInterfaceDhcp",
            ),
            (
                "cisco.meraki.networks_switch_dhcp_server_policy_info",
                "getNetworkSwitchDhcpServerPolicy",
            ),
            (
                "cisco.meraki.networks_switch_stp",
                "updateNetworkSwitchStp",
            ),
            (
                "cisco.meraki.networks_switch_link_aggregations",
                "createNetworkSwitchLinkAggregation",
            ),
            (
                "cisco.meraki.devices_switch_routing_interfaces_info",
                "getDeviceSwitchRoutingInterfaces",
            ),
            (
                "cisco.meraki.devices_switch_routing_interfaces",
                "createDeviceSwitchRoutingInterface",
            ),
            (
                "cisco.meraki.networks_switch_access_control_lists",
                "updateNetworkSwitchAccessControlLists",
            ),
            (
                "cisco.meraki.networks_switch_routing_multicast_info",
                "getNetworkSwitchRoutingMulticast",
            ),
            (
                "cisco.meraki.networks_switch_stacks_routing_interfaces_info",
                "getNetworkSwitchStackRoutingInterface",
            ),
            (
                "cisco.meraki.networks_switch_routing_ospf_info",
                "getNetworkSwitchRoutingOspf",
            ),
            (
                "cisco.meraki.networks_switch_alternate_management_interface_info",
                "getNetworkSwitchAlternateManagementInterface",
            ),
            (
                "cisco.meraki.organizations_config_templates_switch_profiles_info",
                "getOrganizationConfigTemplateSwitchProfiles",
            ),
            (
                "cisco.meraki.networks_switch_routing_ospf",
                "updateNetworkSwitchRoutingOspf",
            ),
            (
                "cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_trusted_servers_info",
                "getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers",
            ),
            (
                "cisco.meraki.networks_switch_dhcp_server_policy_arp_inspection_warnings_by_device_info",
                "getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice",
            ),
            (
                "cisco.meraki.networks_switch_dhcp_v4_servers_seen_info",
                "getNetworkSwitchDhcpV4ServersSeen",
            ),
            (
                "cisco.meraki.networks_switch_link_aggregations_info",
                "getNetworkSwitchLinkAggregations",
            ),
            (
                "cisco.meraki.networks_switch_qos_rules_order_info",
                "getNetworkSwitchQosRule",
            ),
            (
                "cisco.meraki.networks_switch_routing_multicast_rendezvous_points_info",
                "getNetworkSwitchRoutingMulticastRendezvousPoints",
            ),
            (
                "cisco.meraki.devices_switch_routing_static_routes_info",
                "getDeviceSwitchRoutingStaticRoute",
            ),
            (
                "cisco.meraki.networks_switch_stacks_remove",
                "removeNetworkSwitchStack",
            ),
            (
                "cisco.meraki.devices_switch_warm_spare_info",
                "getDeviceSwitchWarmSpare",
            ),
            (
                "cisco.meraki.organizations_summary_top_switches_by_energy_usage_info",
                "getOrganizationSummaryTopSwitchesByEnergyUsage",
            ),
            (
                "cisco.meraki.networks_switch_stacks_add",
                "addNetworkSwitchStack",
            ),
            (
                "cisco.meraki.devices_switch_routing_interfaces_dhcp_info",
                "getDeviceSwitchRoutingInterfaceDhcp",
            ),
            (
                "cisco.meraki.devices_switch_routing_interfaces_dhcp",
                "updateDeviceSwitchRoutingInterfaceDhcp",
            ),
            (
                "cisco.meraki.networks_switch_routing_multicast",
                "updateNetworkSwitchRoutingMulticast",
            ),
        ],
    )
    def test_query_transformation(
        self, module_fqcn, method_name, query_data, load_fixture
    ):
        """
        Test that JQ queries correctly transform Meraki API responses.

        Validates:
        - Query executes without errors
        - Output is always an array
        - Each item has required fields: name, canonical_facts, facts
        - canonical_facts contains valid keys (hostname, ansible_machine_id, ansible_product_serial)
        - facts contains device_type field
        """
        # Skip if fixture file doesn't exist
        fixture_data = load_fixture(module_fqcn)
        if fixture_data is None:
            pytest.skip(f"Fixture file not found for {module_fqcn}")

        # Check if query exists in query_data
        if module_fqcn not in query_data:
            pytest.skip(f"Query not found for {module_fqcn}")

        # Prepare input data
        final_response = {"meraki_response": fixture_data}
        jq_query = query_data[module_fqcn]["query"]

        # Execute query
        try:
            compiled_query = jq.compile(jq_query)
            results = compiled_query.input(final_response).all()
        except Exception as e:
            pytest.fail(
                f"Query execution failed for {module_fqcn} ({method_name}): {str(e)}"
            )

        # Validate output structure
        assert isinstance(
            results, list
        ), f"Output must be a list, got {type(results)} for {module_fqcn}"

        # If results is empty, that's valid (empty array is expected for some cases)
        if len(results) == 0:
            return

        # Validate each item in results
        for idx, item in enumerate(results):
            assert isinstance(
                item, dict
            ), f"Item {idx} must be a dict, got {type(item)} for {module_fqcn}"

            # Check required top-level fields
            assert "name" in item, f"Item {idx} missing 'name' field for {module_fqcn}"
            assert (
                "canonical_facts" in item
            ), f"Item {idx} missing 'canonical_facts' field for {module_fqcn}"
            assert (
                "facts" in item
            ), f"Item {idx} missing 'facts' field for {module_fqcn}"

            # Validate canonical_facts structure
            canonical_facts = item["canonical_facts"]
            assert isinstance(
                canonical_facts, dict
            ), f"canonical_facts must be a dict for item {idx} in {module_fqcn}"

            # Validate canonical_facts keys (should be one of: hostname, ansible_machine_id, ansible_product_serial)
            valid_canonical_keys = {
                "hostname",
                "ansible_machine_id",
                "ansible_product_serial",
            }
            assert (
                len(canonical_facts) > 0
            ), f"canonical_facts cannot be empty for item {idx} in {module_fqcn}"
            for key in canonical_facts.keys():
                assert (
                    key in valid_canonical_keys
                ), f"Invalid canonical_facts key '{key}' for item {idx} in {module_fqcn}. Must be one of: {valid_canonical_keys}"

            # Validate facts structure
            facts = item["facts"]
            assert isinstance(
                facts, dict
            ), f"facts must be a dict for item {idx} in {module_fqcn}"

            # Validate device_type is present in facts
            assert (
                "device_type" in facts
            ), f"facts must contain 'device_type' field for item {idx} in {module_fqcn}"

            # Validate name is a string
            assert isinstance(
                item["name"], str
            ), f"name must be a string for item {idx} in {module_fqcn}, got {type(item['name'])}"

    def test_all_queries_loaded(self, query_data, test_mappings):
        """Test that all queries referenced in test_mappings exist in query_data."""
        missing_queries = []
        for module_fqcn, _ in test_mappings:
            if module_fqcn not in query_data:
                missing_queries.append(module_fqcn)

        if missing_queries:
            pytest.fail(
                f"Missing queries in event_query.yml: {', '.join(missing_queries)}"
            )

    def test_all_fixtures_exist(self, test_mappings, load_fixture):
        """Test that fixture files exist for all test mappings (warns but doesn't fail)."""
        missing_fixtures = []
        for module_fqcn, _ in test_mappings:
            fixture_data = load_fixture(module_fqcn)
            if fixture_data is None:
                missing_fixtures.append(module_fqcn)

        if missing_fixtures:
            pytest.skip(
                f"Missing fixture files (not a failure, but worth noting): {', '.join(missing_fixtures)}"
            )
