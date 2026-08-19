"""
Pytest configuration and fixtures for Meraki query tests.
"""

import json
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
        (
            "cisco.meraki.devices_wireless_bluetooth_settings_info",
            "getDeviceWirelessBluetoothSettings",
        ),
        (
            "cisco.meraki.devices_wireless_bluetooth_settings",
            "updateDeviceWirelessBluetoothSettings",
        ),
        (
            "cisco.meraki.devices_wireless_connection_stats_info",
            "getDeviceWirelessConnectionStats",
        ),
        (
            "cisco.meraki.devices_wireless_electronic_shelf_label",
            "updateDeviceWirelessElectronicShelfLabel",
        ),
        (
            "cisco.meraki.devices_wireless_electronic_shelf_label_info",
            "getDeviceWirelessElectronicShelfLabel",
        ),
        (
            "cisco.meraki.devices_wireless_latency_stats_info",
            "getDeviceWirelessLatencyStats",
        ),
        (
            "cisco.meraki.devices_wireless_radio_settings",
            "updateDeviceWirelessRadioSettings",
        ),
        (
            "cisco.meraki.devices_wireless_radio_settings_info",
            "getDeviceWirelessRadioSettings",
        ),
        (
            "cisco.meraki.devices_wireless_status_info",
            "getDeviceWirelessStatus",
        ),
        (
            "cisco.meraki.devices_wireless_zigbee_enrollments",
            "createDeviceWirelessZigbeeEnrollment",
        ),
        (
            "cisco.meraki.devices_wireless_zigbee_enrollments_info",
            "getDeviceWirelessZigbeeEnrollment",
        ),
        (
            "cisco.meraki.devices_wireless_alternate_management_interface_ipv6",
            "updateDeviceWirelessAlternateManagementInterfaceIpv6",
        ),
        (
            "cisco.meraki.devices_appliance_radio_settings_info",
            "getDeviceApplianceRadioSettings",
        ),
        (
            "cisco.meraki.devices_appliance_radio_settings",
            "updateDeviceApplianceRadioSettings",
        ),
        (
            "cisco.meraki.devices_appliance_performance_info",
            "getDeviceAppliancePerformance",
        ),
        (
            "cisco.meraki.devices_appliance_uplinks_settings_info",
            "getDeviceApplianceUplinksSettings",
        ),
        (
            "cisco.meraki.devices_appliance_uplinks_settings",
            "updateDeviceApplianceUplinksSettings",
        ),
        (
            "cisco.meraki.devices_appliance_vmx_authentication_token",
            "createDeviceApplianceVmxAuthenticationToken",
        ),
        (
            "cisco.meraki.devices_cellular_sims_info",
            "getDeviceCellularSims",
        ),
        (
            "cisco.meraki.devices_cellular_sims",
            "updateDeviceCellularSims",
        ),
        (
            "cisco.meraki.devices_cellular_gateway_lan_info",
            "getDeviceCellularGatewayLan",
        ),
        (
            "cisco.meraki.devices_cellular_gateway_lan",
            "updateDeviceCellularGatewayLan",
        ),
        (
            "cisco.meraki.devices_cellular_gateway_port_forwarding_rules_info",
            "getDeviceCellularGatewayPortForwardingRules",
        ),
        (
            "cisco.meraki.devices_cellular_gateway_port_forwarding_rules",
            "updateDeviceCellularGatewayPortForwardingRules",
        ),
        (
            "cisco.meraki.organizations_summary_top_appliances_by_utilization_info",
            "getOrganizationSummaryTopAppliancesByUtilization",
        ),
        (
            "cisco.meraki.organizations_cellular_gateway_uplink_statuses_info",
            "getOrganizationCellularGatewayUplinkStatuses",
        ),
    ]
