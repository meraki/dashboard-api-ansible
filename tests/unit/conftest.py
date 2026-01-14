"""
Pytest configuration and fixtures for Meraki query tests.
"""

import json
import os
import pytest
import yaml
from pathlib import Path

# Paths
QUERY_FILE = Path(__file__).parent.parent.parent / "extensions" / "audit" / "event_query.yml"
DATA_DIR = Path(__file__).parent / "api_fixtures"


@pytest.fixture(scope="session")
def query_data():
    """Load the event_query.yml file once for all tests."""
    with open(QUERY_FILE) as f:
        return yaml.safe_load(f)


@pytest.fixture
def load_fixture():
    """Fixture factory to load JSON fixture files."""

    def _load_fixture(module_fqcn):
        filepath = DATA_DIR / f"{module_fqcn}.json"
        if filepath.exists():
            with open(filepath, "r") as f:
                return json.load(f)
        return None

    return _load_fixture


@pytest.fixture
def test_mappings():
    """Return the mapping between module_fqcn and method_name."""
    return [
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
    ]
