==========================
Cisco.Meraki Release Notes
==========================

.. contents:: Topics

v2.26.0
=======

Minor Changes
-------------

- Collection updated to the Cisco Meraki Dashboard API v1.76.0.
- administered_licensing_subscription_entitlements_info - Added the `subscriptionType` parameter.
- devices_appliance_dhcp_subnets_info - Added new plugin. Return the DHCP subnet information for an appliance.
- devices_appliance_interfaces_ports - Added new plugin. Update configurations for an appliance's specified port.
- devices_appliance_interfaces_ports_update - Added the `profile` parameter.
- devices_appliance_prefixes_delegated_info - Added new plugin. Return current delegated IPv6 prefixes on an appliance.
- devices_appliance_prefixes_delegated_vlan_assignments_info - Added new plugin. Return prefixes assigned to all IPv6 enabled VLANs on an appliance.
- devices_camera_analytics_overview_info - Added new plugin. Returns an overview of aggregate analytics data for a timespan.
- devices_camera_analytics_recent_info - Added new plugin. Returns most recent record for analytics zones.
- devices_camera_analytics_zones_history_info - Added new plugin. Return historical records for analytic zones.
- devices_camera_analytics_zones_info - Added new plugin. Returns all configured analytic zones for this camera.
- devices_camera_sense_object_detection_models_info - Added new plugin. Returns the MV Sense object detection model list for the given camera.
- devices_certificates_revoke - Added new plugin. Revoke a device certificate.
- devices_clients_info - Added new plugin. List the clients of a device, up to a maximum of a month ago.
- devices_live_tools_arp_table - Added the `arpTableId` parameter.
- devices_live_tools_arp_table_info - Added the `arpTableId`, `serial` parameters.
- devices_live_tools_cable_test - Added the `id` parameter.
- devices_live_tools_cable_test_info - Added the `id`, `serial` parameters.
- devices_live_tools_mac_table - Added the `mac` parameter.
- devices_live_tools_route_details - Added new plugin. Enqueue a live tool job to fetch route details from a device.
- devices_live_tools_route_details_info - Added new plugin. Return a route details live tool job for a device.
- devices_live_tools_routing_table_lookups - Added the `vrf` parameter.
- devices_live_tools_throughput_test - Added the `throughputTestId` parameter.
- devices_live_tools_throughput_test_info - Added the `serial`, `throughputTestId` parameters.
- devices_live_tools_wake_on_lan - Added the `wakeOnLanId` parameter.
- devices_live_tools_wake_on_lan_info - Added the `serial`, `wakeOnLanId` parameters.
- devices_loss_and_latency_history_info - Added new plugin. Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for MX, MG and Z devices.
- devices_switch_ports - Added the `fastPoe`, `perpetualPoe` parameters.
- devices_switch_ports_statuses_packets_info - Added new plugin. Return the packet counters for all the ports of a switch.
- devices_switch_routing_interfaces - Added the `bidirectionalForwardingDetection` parameter.
- devices_switch_routing_interfaces_dhcp - Added the `dhcpDefaultRouterIps`, `dhcpDomainName` parameters.
- devices_wireless_radio_overrides - Added new plugin. Update 2.4 GHz, 5 GHz, and 6 GHz radio settings channel, channel width, power, and enable/disable that override RF profiles.
- devices_wireless_radio_overrides_info - Added new plugin. Return the radio overrides of a device.
- networks_appliance_clients_security_events_info - Added new plugin. List the security events for a client.
- networks_appliance_firewall_inbound_cellular_firewall_rules - Added new plugin. Update the inbound cellular firewall rules of an MX network.
- networks_appliance_firewall_inbound_cellular_firewall_rules_info - Added new plugin. Return the inbound cellular firewall rules for an MX network.
- networks_appliance_rf_profiles - Added the `rfProfileId` parameter.
- networks_appliance_rf_profiles_info - Added the `rfProfileId` parameter.
- networks_appliance_security_events_info - Added new plugin. List the security events for a network.
- networks_appliance_security_https_inspection - Added new plugin. Update HTTPS inspection configuration for a network.
- networks_appliance_security_intrusion - Added the `policy` parameter.
- networks_appliance_single_lan - Added the `vrf` parameter.
- networks_appliance_static_routes - Added the `vrf` parameter.
- networks_appliance_traffic_shaping_vpn_exclusions - Added the `applicationCategoryMapping` parameter.
- networks_appliance_uplinks_usage_history_info - Added new plugin. Get the sent and received bytes for each uplink of a network.
- networks_appliance_vpn_bgp - Added the `ipv6`, `localAsNumber`, `priorityRoute`, `tunnelDownTermination` parameters.
- networks_appliance_vpn_site_to_site_vpn - Added the `confirmed`, `natTraversal` parameters.
- networks_bluetooth_clients_info - Added the `direction`, `endingBefore`, `perPage`, `startingAfter`, `t0`, `timespan`, `total_pages` parameters.
- networks_camera_schedules_info - Added new plugin. Returns a list of all camera recording schedules.
- networks_campus_gateway_clusters - Added new plugin. Create a cluster and add campus gateways to it.
- networks_campus_gateway_ssids_mdns - Added new plugin. Update the mDNS gateway settings and rules for a SSID and cluster.
- networks_clients_application_usage_info - Added new plugin. Return the application usage data for clients.
- networks_clients_bandwidth_usage_history_info - Added new plugin. Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.
- networks_clients_traffic_history_info - Added new plugin. Return the client's network traffic data over time.
- networks_clients_usage_histories_info - Added new plugin. Return the usage histories for clients.
- networks_clients_usage_history_info - Added new plugin. Return the client's daily usage history.
- networks_firmware_upgrades - Added the `featureLossAcknowledgements` parameter.
- networks_network_health_channel_utilization_info - Added new plugin. Get the channel utilization over each radio for all APs in a network.
- networks_sm_devices_restrictions_info - Added new plugin. List the restrictions on a device.
- networks_sm_profiles_info - Added the `direction`, `endingBefore`, `perPage`, `startingAfter`, `total_pages` parameters.
- networks_splash_login_attempts_info - Added new plugin. List the splash login attempts for a network.
- networks_switch_settings - Added the `clientTracking` parameter.
- networks_switch_stacks_routing_interfaces - Added the `bidirectionalForwardingDetection` parameter.
- networks_switch_stacks_routing_interfaces_dhcp - Added the `dhcpDefaultRouterIps`, `dhcpDomainName` parameters.
- networks_traffic_info - Added new plugin. Return the traffic analysis data for this network.
- networks_vlan_profiles - Added the `activeVlans` parameter.
- networks_wireless_air_marshal_info - Added new plugin. List Air Marshal scan results from a network.
- networks_wireless_clients_connectivity_events_info - Added new plugin. List the wireless connectivity events for a client within a network in the timespan.
- networks_wireless_clients_latency_history_info - Added new plugin. Return the latency history for a client.
- networks_wireless_devices_latency_stats_info - Added new plugin. Aggregated latency info for this network, grouped by node.
- networks_wireless_rf_profiles - Added the `dot11be` parameter.
- networks_wireless_ssids - Added the `campusGateway`, `dot11k` parameters.
- networks_wireless_ssids_overrides - Added new plugin. Update the overrides for this SSID.
- networks_wireless_ssids_overrides_info - Added new plugin. Display the overrides for this SSID.
- networks_wireless_ssids_owe - Added new plugin. Update the OWE transition pairs for a network.
- organizations_action_batches_info - Added the `direction`, `endingBefore`, `perPage`, `sortOrder`, `startingAfter`, `total_pages` parameters.
- organizations_api_rest_provisioning_pipelines_info - Added new plugin. List pipelines with operation and status metadata, sorted by pipeline ID. Pipeline IDs are assigned in creation order, so newer pipelines are returned first by default; sortOrder controls that ID order.
- organizations_appliance_devices_interfaces_ports_profiles_assignments_info - Added new plugin. Returns MX port profile assignments.
- organizations_appliance_security_events_info - Added new plugin. List the security events for an organization.
- organizations_appliance_security_https_inspection_by_network_info - Added new plugin. List HTTPS inspection status and configuration for appliances in the organization.
- organizations_appliance_security_httpsi_certificates - Added new plugin. Upload an HTTPS Inspection certificate to MX devices in the same organization.
- organizations_appliance_security_httpsi_info - Added new plugin. Retrieve the HTTPS Inspection state for all security appliances in an organization.
- organizations_appliance_security_intrusion_policies - Added new plugin. Create a new intrusion policy for the organization.
- organizations_appliance_security_intrusion_policies_info - Added new plugin. List the intrusion policies configured for an organization along with base policies.
- organizations_appliance_security_intrusion_policies_overviews_info - Added new plugin. List counts for the intrusion and base policies configured for an organization.
- organizations_appliance_security_intrusion_policies_rule_groups_overrides_declare - Added new plugin. Declare the desired rule group overrides for an intrusion policy.
- organizations_appliance_security_intrusion_policies_rules_overrides_declare - Added new plugin. Declare the desired rule overrides for an intrusion policy.
- organizations_appliance_security_intrusion_rule_groups_info - Added new plugin. List the rule groups that belong to a security policy.
- organizations_appliance_security_intrusion_rule_groups_overrides - Added new plugin. Delete a rule group override for an intrusion policy.
- organizations_appliance_security_intrusion_rule_groups_overrides_info - Added new plugin. List the rule group overrides configured for an intrusion policy.
- organizations_appliance_security_intrusion_rule_groups_overviews_info - Added new plugin. List counts for the child rule groups and rules for each rule group in a security policy.
- organizations_appliance_security_intrusion_rules_info - Added new plugin. List the rules that belong to a security policy.
- organizations_appliance_security_intrusion_rules_overrides - Added new plugin. Delete a rule override for an intrusion policy.
- organizations_appliance_security_intrusion_rules_overrides_info - Added new plugin. List the rule overrides configured for an intrusion policy.
- organizations_appliance_uplink_statuses_info - Added new plugin. List the uplink status of every Meraki MX appliance, Z series appliance, and Secure Router in the organization.
- organizations_appliance_vpn_stats_info - Added new plugin. Show VPN history stats for networks in an organization.
- organizations_appliance_vpn_statuses_info - Added new plugin. Show VPN status for networks in an organization.
- organizations_assurance_alerts_profiles - Added new plugin. Create an alert profile.
- organizations_assurance_alerts_profiles_info - Added new plugin. List the alert profiles for this organization.
- organizations_assurance_impacted_device_wireless_by_network_info - Added new plugin. Returns count of impacted wireless devices per network on a given organization and time range.
- organizations_assurance_wireless_experience_successful_connections_by_network_info - Added new plugin. Returns connection and client counts aggregated by network for the requested time window.
- organizations_branding_policies - Added the `appearance` parameter.
- organizations_camera_onboarding_statuses - Added new plugin. Notify that credential handoff to camera has completed.
- organizations_camera_onboarding_statuses_info - Added new plugin. Fetch onboarding status of cameras.
- organizations_camera_roles - Added the `roleId` parameter.
- organizations_camera_roles_info - Added the `roleId` parameter.
- organizations_campus_gateway_clients_usage_by_network_by_cluster_info - Added new plugin. Returns client usage details for campus gateway clusters within an organization.
- organizations_campus_gateway_clusters_failover_targets_by_cluster_info - Added new plugin. List the failover targets of the Campus Gateway clusters, grouped by cluster.
- organizations_campus_gateway_clusters_failover_targets_info - Added new plugin. List the details of a Failover Targets for a Campus Gateway cluster.
- organizations_campus_gateway_clusters_networks_overviews_info - Added new plugin. List networks tunneling through Campus Gateway clusters with their AP, ssids and client counts.
- organizations_campus_gateway_clusters_provision - Added new plugin. Provisions a cluster,adds campus gateways to it and associate/dissociate failover targets.
- organizations_campus_gateway_clusters_ssids_info - Added new plugin. List SSIDs tunneling through Campus Gateway clusters.
- organizations_campus_gateway_clusters_tunnelable_info - Added new plugin. List available campus gateway clusters that can be used for wireless network tunneling.
- organizations_campus_gateway_clusters_tunneling_batch_update - Added new plugin. Update MCG cluster-network tunnel settings for multiple networks.
- organizations_campus_gateway_clusters_tunneling_by_cluster_by_network_info - Added new plugin. List all the MCG cluster-network tunnel settings.
- organizations_campus_gateway_connections_info - Added new plugin. List the details of APs tunneling through the Campus Gateway clusters.
- organizations_campus_gateway_connections_overview_info - Added new plugin. List the count of connections APs with tunneling status up and down through the Campus Gateway clusters.
- organizations_campus_gateway_devices_system_cpu_load_info - Added new plugin. Return the latest CPU load averages reported by Campus Gateway devices.
- organizations_certificates_authorities - Added new plugin. Delete a certificate authority.
- organizations_certificates_authorities_info - Added new plugin. List certificate authorities for an organization.
- organizations_certificates_authorities_jobs_info - Added new plugin. Return the status and result of a certificate authority job.
- organizations_certificates_authorities_revoke - Added new plugin. Revoke a trusted feature certificate authority.
- organizations_certificates_revocation_lists_info - Added new plugin. Return full certificate revocation lists CRLs for the organization's certificate authorities.
- organizations_config_templates_switch_profiles_ports - Added the `fastPoe`, `perpetualPoe` parameters.
- organizations_configuration_changes_info - Added new plugin. View the Change Log for your organization.
- organizations_devices_certificates_info - Added new plugin. List device certificates for the organization.
- organizations_inventory_devices_swaps_bulk - Added new plugin. Swap the devices identified by devices.old with a devices.new, then perform the afterAction on the devices.old.
- organizations_inventory_devices_swaps_bulk_info - Added new plugin. List of device swaps for a given request ID {id} .
- organizations_networks_groups - Added new plugin. Create a network group.
- organizations_networks_groups_bulk_assign - Added new plugin. Add networks to a network group.
- organizations_networks_groups_bulk_unassign - Added new plugin. Remove networks from a network group.
- organizations_networks_groups_info - Added new plugin. List the network groups in an organization.
- organizations_networks_groups_overview_by_group_info - Added new plugin. List the client and status overview information for the network groups in an organization.
- organizations_policies_global_firewall_rulesets_rules - Added the `logging` parameter.
- organizations_policies_global_group_policies_firewall_rulesets_assignments - Added the `staged` parameter.
- organizations_policies_global_group_policies_firewall_rulesets_assignments_commit - Added new plugin. Commit staged Organization-Wide Policy Ruleset Assignments.
- organizations_policies_global_group_policies_networks_assignments_bulk_assign - Added new plugin. Assign Network Enforcement Targets to an Organization-Wide Policy.
- organizations_policies_global_group_policies_networks_assignments_bulk_delete - Added new plugin. Remove Network Enforcement Targets from an Organization-Wide Policy.
- organizations_policies_global_group_policies_networks_assignments_info - Added new plugin. List Network Enforcement Target Assignments for Organization-Wide policies for the specified organization.
- organizations_policies_global_group_policies_networks_info - Added new plugin. List all available Network Enforcement Targets for an Organization and their associated Organization-Wide Policies if applicable.
- organizations_sase_sites_detach - Added the `items` parameter.
- organizations_sm_admins_roles - Added the `roleId` parameter.
- organizations_sm_admins_roles_info - Added the `roleId` parameter.
- organizations_summary_sustainability_daily_consumer_metrics_networks_info - Added new plugin. Lists daily consumer metrics for networks.
- organizations_summary_sustainability_summary_consumer_metrics_device_categories_aggregated_info - Added new plugin. Lists summary consumer metrics aggregated by device category.
- organizations_summary_sustainability_summary_consumer_metrics_device_categories_info - Added new plugin. Lists available device categories for sustainability metrics with their corresponding device types.
- organizations_summary_sustainability_summary_consumer_metrics_devices_info - Added new plugin. Lists summary consumer metrics for devices.
- organizations_summary_sustainability_summary_consumer_metrics_networks_aggregated_info - Added new plugin. Returns aggregated consumer metrics for all networks in the organization.
- organizations_summary_sustainability_summary_consumer_metrics_networks_info - Added new plugin. Lists summary consumer metrics for networks.
- organizations_summary_switch_power_history_info - Added new plugin. Returns the total PoE power draw for all switch ports in the organization over the requested timespan by default the last 24 hours.
- organizations_webhooks_alert_types_info - Added new plugin. Return a list of alert types to be used with managing webhook alerts.
- organizations_wireless_clients_connections_impacted_by_network_by_ssid_info - Added new plugin. Summarize the number of wireless clients impacted by connection failures on network SSIDs, across an organization.
- organizations_wireless_clients_usage_by_network_by_ssid_info - Added new plugin. Returns client usage details for wireless network SSIDs within an organization.
- organizations_wireless_clients_usage_by_network_info - Added new plugin. Returns client usage details for wireless networks within an organization.
- organizations_wireless_clients_usage_by_ssid_info - Added new plugin. Returns client usage details for SSIDs within an organization.
- organizations_wireless_radio_overrides_by_device_info - Added new plugin. Return a list of radio overrides.
- organizations_wireless_ssids_owe_by_network_info - Added new plugin. Returns an array of objects, each containing OWE transition pairs for the corresponding network.
- organizations_wireless_ssids_profiles - Added new plugin. Create a new SSID profile in an organization.
- organizations_wireless_ssids_profiles_assignments - Added new plugin. Assigns an SSID profile to an SSID in the organization.
- organizations_wireless_ssids_profiles_assignments_by_network_info - Added new plugin. List the SSID profile assignments in an organization, grouped by network.
- organizations_wireless_ssids_profiles_assignments_info - Added new plugin. List the SSID profile assignments in an organization.
- organizations_wireless_ssids_profiles_info - Added new plugin. Returns the SSID profiles for an organization.
- organizations_wireless_ssids_profiles_overviews_info - Added new plugin. Returns the SSID profiles' overview information for an organization.
- plugin_utils/meraki - Added the `meraki_caller` connection option (environment variable `MERAKI_PYTHON_SDK_CALLER`) to set the identifier sent to the API for usage tracking; it defaults to `MerakiAnsibleCollection/2.26.0 Cisco`.
- plugin_utils/meraki - Unified `meraki_compare_equality` and `meraki_compare_equality2` into a single comparison used by every module. Fields missing from the API response are now treated as empty values of the requested type, and values that differ only by type (for example `"1"` and `1`) are considered equal, which avoids reporting `changed` when nothing differs. `meraki_compare_equality2` is kept as a deprecated alias.

Breaking Changes / Porting Guide
--------------------------------

- networks_wireless_clients_connection_stats_info - Removed the `vlan` parameter, which is no longer supported by the Dashboard API.
- networks_wireless_connection_stats_info - Removed the `vlan` parameter, which is no longer supported by the Dashboard API.
- networks_wireless_devices_connection_stats_info - Removed the `vlan` parameter, which is no longer supported by the Dashboard API.
- networks_wireless_failed_connections_info - Removed the `vlan` parameter, which is no longer supported by the Dashboard API.
- networks_wireless_location_scanning - Removed the `ruleId` parameter, which is no longer supported by the Dashboard API.
- organizations_inventory_onboarding_cloud_monitoring_prepare - Removed the module documentation; the cloud monitoring onboarding endpoints were removed from the Dashboard API.
- organizations_sase_sites_attach - Removed the `callback` parameter, which is no longer supported by the Dashboard API.

Bugfixes
--------

- cellular gateway, campus gateway and wireless controller modules - Fixed the SDK family names (`cellulargateway`, `cellular_gateway`, `campusgateway`, `campus_gateway`, `wireless_controller` to `cellularGateway`, `campusGateway`, `wirelessController`). Every `networks_cellular_gateway_*`, `organizations_cellular_gateway_*`, `networks_campus_gateway_*`, `organizations_campus_gateway_*` and `organizations_wireless_controller_*` module failed with an AttributeError before calling the API.
- devices_live_tools_cable_test, devices_live_tools_ping, devices_live_tools_ping_device, devices_live_tools_ports_cycle, devices_live_tools_routing_table_lookups, devices_live_tools_routing_table_summaries, networks_sensor_alerts_profiles, organizations_adaptive_policy_groups, organizations_adaptive_policy_policies, organizations_inventory_devices_swaps_bulk, organizations_splash_assets - The lookup of an existing object by id omitted the required path parameter (`serial`, `networkId` or `organizationId`), so it always failed silently and a new object was created on every run.
- doc_fragments - Corrected the module notes, which referred to the Cisco DNAC SDK and `dnac_` parameters instead of the Cisco Meraki SDK and `meraki_` parameters.
- networks_vlan_profiles - The lookup by `iname` now sends the required `networkId`, and `iname` (the profile identifier) takes precedence over the display `name` when finding an existing profile.
- networks_vlan_profiles_info - Fixed an AttributeError (missing `get_object` method) when `iname` is provided.
- organizations_appliance_routing_vrfs_settings, organizations_appliance_security_intrusion, organizations_appliance_vpn_site_to_site_ipsec_peers_slas, organizations_appliance_vpn_third_party_vpn_peers, organizations_branding_policies_priorities, organizations_login_security, organizations_saml, organizations_wireless_mqtt_settings - state=present always failed with "Object does not exists, plugin only has update" because the current settings were never read; these organization-wide singleton resources now use `organizationId` as their identifier.
- organizations_appliance_vpn_third_party_vpn_peers, organizations_appliance_vpn_third_party_vpn_peers_info - Fixed the SDK method names (`getOrganizationApplianceVpnThirdPartyVPNPeers`, `updateOrganizationApplianceVpnThirdPartyVPNPeers`); the previous `...Vpnpeers` names do not exist in any SDK version.

Known Issues
------------

- devices_certificates_revoke, devices_live_tools_route_details, devices_live_tools_route_details_info, organizations_assurance_wireless_experience_successful_connections_by_network_info, organizations_certificates_authorities, organizations_certificates_authorities_info, organizations_certificates_authorities_jobs_info, organizations_certificates_authorities_revoke, organizations_certificates_revocation_lists_info, organizations_devices_certificates_info - These endpoints were added in Dashboard API v1.76.0 and are not yet available in any released Meraki Python SDK (the latest, 4.7.0, covers API v1.75.1). The modules fail until an SDK release that includes them is installed.
- organizations_inventory_onboarding_cloud_monitoring_export_events, organizations_inventory_onboarding_cloud_monitoring_imports, organizations_inventory_onboarding_cloud_monitoring_imports_info, organizations_inventory_onboarding_cloud_monitoring_networks_info, organizations_inventory_onboarding_cloud_monitoring_prepare, organizations_sase_connectors_batch_create - The corresponding endpoints were removed from the Dashboard API (present in v1.69.0, absent since v1.72.0), so these modules can no longer succeed.

v2.26.0
=======

Minor Changes
-------------

- Collection updated to the Cisco Meraki Dashboard API v1.76.0.
- administered_licensing_subscription_entitlements_info - Added the `subscriptionType` parameter.
- devices_appliance_dhcp_subnets_info - Added new plugin. Return the DHCP subnet information for an appliance.
- devices_appliance_interfaces_ports - Added new plugin. Update configurations for an appliance's specified port.
- devices_appliance_interfaces_ports_update - Added the `profile` parameter.
- devices_appliance_prefixes_delegated_info - Added new plugin. Return current delegated IPv6 prefixes on an appliance.
- devices_appliance_prefixes_delegated_vlan_assignments_info - Added new plugin. Return prefixes assigned to all IPv6 enabled VLANs on an appliance.
- devices_camera_analytics_overview_info - Added new plugin. Returns an overview of aggregate analytics data for a timespan.
- devices_camera_analytics_recent_info - Added new plugin. Returns most recent record for analytics zones.
- devices_camera_analytics_zones_history_info - Added new plugin. Return historical records for analytic zones.
- devices_camera_analytics_zones_info - Added new plugin. Returns all configured analytic zones for this camera.
- devices_camera_sense_object_detection_models_info - Added new plugin. Returns the MV Sense object detection model list for the given camera.
- devices_certificates_revoke - Added new plugin. Revoke a device certificate.
- devices_clients_info - Added new plugin. List the clients of a device, up to a maximum of a month ago.
- devices_live_tools_arp_table - Added the `arpTableId` parameter.
- devices_live_tools_arp_table_info - Added the `arpTableId`, `serial` parameters.
- devices_live_tools_cable_test - Added the `id` parameter.
- devices_live_tools_cable_test_info - Added the `id`, `serial` parameters.
- devices_live_tools_mac_table - Added the `mac` parameter.
- devices_live_tools_route_details - Added new plugin. Enqueue a live tool job to fetch route details from a device.
- devices_live_tools_route_details_info - Added new plugin. Return a route details live tool job for a device.
- devices_live_tools_routing_table_lookups - Added the `vrf` parameter.
- devices_live_tools_throughput_test - Added the `throughputTestId` parameter.
- devices_live_tools_throughput_test_info - Added the `serial`, `throughputTestId` parameters.
- devices_live_tools_wake_on_lan - Added the `wakeOnLanId` parameter.
- devices_live_tools_wake_on_lan_info - Added the `serial`, `wakeOnLanId` parameters.
- devices_loss_and_latency_history_info - Added new plugin. Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for MX, MG and Z devices.
- devices_switch_ports - Added the `fastPoe`, `perpetualPoe` parameters.
- devices_switch_ports_statuses_packets_info - Added new plugin. Return the packet counters for all the ports of a switch.
- devices_switch_routing_interfaces - Added the `bidirectionalForwardingDetection` parameter.
- devices_switch_routing_interfaces_dhcp - Added the `dhcpDefaultRouterIps`, `dhcpDomainName` parameters.
- devices_wireless_radio_overrides - Added new plugin. Update 2.4 GHz, 5 GHz, and 6 GHz radio settings channel, channel width, power, and enable/disable that override RF profiles.
- devices_wireless_radio_overrides_info - Added new plugin. Return the radio overrides of a device.
- event_query - `facts.device_type` now uses the normalized AAP indirect node counting taxonomy required by ansible-lint: `resource` for `cisco.meraki.devices` and `cisco.meraki.devices_info`, and `organizational_unit` for `cisco.meraki.networks_info`. The Meraki product type is kept in the new `meraki_product_type` fact.
- networks_appliance_clients_security_events_info - Added new plugin. List the security events for a client.
- networks_appliance_firewall_inbound_cellular_firewall_rules - Added new plugin. Update the inbound cellular firewall rules of an MX network.
- networks_appliance_firewall_inbound_cellular_firewall_rules_info - Added new plugin. Return the inbound cellular firewall rules for an MX network.
- networks_appliance_rf_profiles - Added the `rfProfileId` parameter.
- networks_appliance_rf_profiles_info - Added the `rfProfileId` parameter.
- networks_appliance_security_events_info - Added new plugin. List the security events for a network.
- networks_appliance_security_https_inspection - Added new plugin. Update HTTPS inspection configuration for a network.
- networks_appliance_security_intrusion - Added the `policy` parameter.
- networks_appliance_single_lan - Added the `vrf` parameter.
- networks_appliance_static_routes - Added the `vrf` parameter.
- networks_appliance_traffic_shaping_vpn_exclusions - Added the `applicationCategoryMapping` parameter.
- networks_appliance_uplinks_usage_history_info - Added new plugin. Get the sent and received bytes for each uplink of a network.
- networks_appliance_vpn_bgp - Added the `ipv6`, `localAsNumber`, `priorityRoute`, `tunnelDownTermination` parameters.
- networks_appliance_vpn_site_to_site_vpn - Added the `confirmed`, `natTraversal` parameters.
- networks_bluetooth_clients_info - Added the `direction`, `endingBefore`, `perPage`, `startingAfter`, `t0`, `timespan`, `total_pages` parameters.
- networks_camera_schedules_info - Added new plugin. Returns a list of all camera recording schedules.
- networks_campus_gateway_clusters - Added new plugin. Create a cluster and add campus gateways to it.
- networks_campus_gateway_ssids_mdns - Added new plugin. Update the mDNS gateway settings and rules for a SSID and cluster.
- networks_clients_application_usage_info - Added new plugin. Return the application usage data for clients.
- networks_clients_bandwidth_usage_history_info - Added new plugin. Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.
- networks_clients_traffic_history_info - Added new plugin. Return the client's network traffic data over time.
- networks_clients_usage_histories_info - Added new plugin. Return the usage histories for clients.
- networks_clients_usage_history_info - Added new plugin. Return the client's daily usage history.
- networks_firmware_upgrades - Added the `featureLossAcknowledgements` parameter.
- networks_network_health_channel_utilization_info - Added new plugin. Get the channel utilization over each radio for all APs in a network.
- networks_sm_devices_restrictions_info - Added new plugin. List the restrictions on a device.
- networks_sm_profiles_info - Added the `direction`, `endingBefore`, `perPage`, `startingAfter`, `total_pages` parameters.
- networks_splash_login_attempts_info - Added new plugin. List the splash login attempts for a network.
- networks_switch_settings - Added the `clientTracking` parameter.
- networks_switch_stacks_routing_interfaces - Added the `bidirectionalForwardingDetection` parameter.
- networks_switch_stacks_routing_interfaces_dhcp - Added the `dhcpDefaultRouterIps`, `dhcpDomainName` parameters.
- networks_traffic_info - Added new plugin. Return the traffic analysis data for this network.
- networks_vlan_profiles - Added the `activeVlans` parameter.
- networks_wireless_air_marshal_info - Added new plugin. List Air Marshal scan results from a network.
- networks_wireless_clients_connectivity_events_info - Added new plugin. List the wireless connectivity events for a client within a network in the timespan.
- networks_wireless_clients_latency_history_info - Added new plugin. Return the latency history for a client.
- networks_wireless_devices_latency_stats_info - Added new plugin. Aggregated latency info for this network, grouped by node.
- networks_wireless_rf_profiles - Added the `dot11be` parameter.
- networks_wireless_ssids - Added the `campusGateway`, `dot11k` parameters.
- networks_wireless_ssids_overrides - Added new plugin. Update the overrides for this SSID.
- networks_wireless_ssids_overrides_info - Added new plugin. Display the overrides for this SSID.
- networks_wireless_ssids_owe - Added new plugin. Update the OWE transition pairs for a network.
- organizations_action_batches_info - Added the `direction`, `endingBefore`, `perPage`, `sortOrder`, `startingAfter`, `total_pages` parameters.
- organizations_api_rest_provisioning_pipelines_info - Added new plugin. List pipelines with operation and status metadata, sorted by pipeline ID. Pipeline IDs are assigned in creation order, so newer pipelines are returned first by default; sortOrder controls that ID order.
- organizations_appliance_devices_interfaces_ports_profiles_assignments_info - Added new plugin. Returns MX port profile assignments.
- organizations_appliance_security_events_info - Added new plugin. List the security events for an organization.
- organizations_appliance_security_https_inspection_by_network_info - Added new plugin. List HTTPS inspection status and configuration for appliances in the organization.
- organizations_appliance_security_httpsi_certificates - Added new plugin. Upload an HTTPS Inspection certificate to MX devices in the same organization.
- organizations_appliance_security_httpsi_info - Added new plugin. Retrieve the HTTPS Inspection state for all security appliances in an organization.
- organizations_appliance_security_intrusion_policies - Added new plugin. Create a new intrusion policy for the organization.
- organizations_appliance_security_intrusion_policies_info - Added new plugin. List the intrusion policies configured for an organization along with base policies.
- organizations_appliance_security_intrusion_policies_overviews_info - Added new plugin. List counts for the intrusion and base policies configured for an organization.
- organizations_appliance_security_intrusion_policies_rule_groups_overrides_declare - Added new plugin. Declare the desired rule group overrides for an intrusion policy.
- organizations_appliance_security_intrusion_policies_rules_overrides_declare - Added new plugin. Declare the desired rule overrides for an intrusion policy.
- organizations_appliance_security_intrusion_rule_groups_info - Added new plugin. List the rule groups that belong to a security policy.
- organizations_appliance_security_intrusion_rule_groups_overrides - Added new plugin. Delete a rule group override for an intrusion policy.
- organizations_appliance_security_intrusion_rule_groups_overrides_info - Added new plugin. List the rule group overrides configured for an intrusion policy.
- organizations_appliance_security_intrusion_rule_groups_overviews_info - Added new plugin. List counts for the child rule groups and rules for each rule group in a security policy.
- organizations_appliance_security_intrusion_rules_info - Added new plugin. List the rules that belong to a security policy.
- organizations_appliance_security_intrusion_rules_overrides - Added new plugin. Delete a rule override for an intrusion policy.
- organizations_appliance_security_intrusion_rules_overrides_info - Added new plugin. List the rule overrides configured for an intrusion policy.
- organizations_appliance_uplink_statuses_info - Added new plugin. List the uplink status of every Meraki MX appliance, Z series appliance, and Secure Router in the organization.
- organizations_appliance_vpn_stats_info - Added new plugin. Show VPN history stats for networks in an organization.
- organizations_appliance_vpn_statuses_info - Added new plugin. Show VPN status for networks in an organization.
- organizations_assurance_alerts_profiles - Added new plugin. Create an alert profile.
- organizations_assurance_alerts_profiles_info - Added new plugin. List the alert profiles for this organization.
- organizations_assurance_impacted_device_wireless_by_network_info - Added new plugin. Returns count of impacted wireless devices per network on a given organization and time range.
- organizations_assurance_wireless_experience_successful_connections_by_network_info - Added new plugin. Returns connection and client counts aggregated by network for the requested time window.
- organizations_branding_policies - Added the `appearance` parameter.
- organizations_camera_onboarding_statuses - Added new plugin. Notify that credential handoff to camera has completed.
- organizations_camera_onboarding_statuses_info - Added new plugin. Fetch onboarding status of cameras.
- organizations_camera_roles - Added the `roleId` parameter.
- organizations_camera_roles_info - Added the `roleId` parameter.
- organizations_campus_gateway_clients_usage_by_network_by_cluster_info - Added new plugin. Returns client usage details for campus gateway clusters within an organization.
- organizations_campus_gateway_clusters_failover_targets_by_cluster_info - Added new plugin. List the failover targets of the Campus Gateway clusters, grouped by cluster.
- organizations_campus_gateway_clusters_failover_targets_info - Added new plugin. List the details of a Failover Targets for a Campus Gateway cluster.
- organizations_campus_gateway_clusters_networks_overviews_info - Added new plugin. List networks tunneling through Campus Gateway clusters with their AP, ssids and client counts.
- organizations_campus_gateway_clusters_provision - Added new plugin. Provisions a cluster,adds campus gateways to it and associate/dissociate failover targets.
- organizations_campus_gateway_clusters_ssids_info - Added new plugin. List SSIDs tunneling through Campus Gateway clusters.
- organizations_campus_gateway_clusters_tunnelable_info - Added new plugin. List available campus gateway clusters that can be used for wireless network tunneling.
- organizations_campus_gateway_clusters_tunneling_batch_update - Added new plugin. Update MCG cluster-network tunnel settings for multiple networks.
- organizations_campus_gateway_clusters_tunneling_by_cluster_by_network_info - Added new plugin. List all the MCG cluster-network tunnel settings.
- organizations_campus_gateway_connections_info - Added new plugin. List the details of APs tunneling through the Campus Gateway clusters.
- organizations_campus_gateway_connections_overview_info - Added new plugin. List the count of connections APs with tunneling status up and down through the Campus Gateway clusters.
- organizations_campus_gateway_devices_system_cpu_load_info - Added new plugin. Return the latest CPU load averages reported by Campus Gateway devices.
- organizations_certificates_authorities - Added new plugin. Delete a certificate authority.
- organizations_certificates_authorities_info - Added new plugin. List certificate authorities for an organization.
- organizations_certificates_authorities_jobs_info - Added new plugin. Return the status and result of a certificate authority job.
- organizations_certificates_authorities_revoke - Added new plugin. Revoke a trusted feature certificate authority.
- organizations_certificates_revocation_lists_info - Added new plugin. Return full certificate revocation lists CRLs for the organization's certificate authorities.
- organizations_config_templates_switch_profiles_ports - Added the `fastPoe`, `perpetualPoe` parameters.
- organizations_configuration_changes_info - Added new plugin. View the Change Log for your organization.
- organizations_devices_certificates_info - Added new plugin. List device certificates for the organization.
- organizations_inventory_devices_swaps_bulk - Added new plugin. Swap the devices identified by devices.old with a devices.new, then perform the afterAction on the devices.old.
- organizations_inventory_devices_swaps_bulk_info - Added new plugin. List of device swaps for a given request ID {id} .
- organizations_networks_groups - Added new plugin. Create a network group.
- organizations_networks_groups_bulk_assign - Added new plugin. Add networks to a network group.
- organizations_networks_groups_bulk_unassign - Added new plugin. Remove networks from a network group.
- organizations_networks_groups_info - Added new plugin. List the network groups in an organization.
- organizations_networks_groups_overview_by_group_info - Added new plugin. List the client and status overview information for the network groups in an organization.
- organizations_policies_global_firewall_rulesets_rules - Added the `logging` parameter.
- organizations_policies_global_group_policies_firewall_rulesets_assignments - Added the `staged` parameter.
- organizations_policies_global_group_policies_firewall_rulesets_assignments_commit - Added new plugin. Commit staged Organization-Wide Policy Ruleset Assignments.
- organizations_policies_global_group_policies_networks_assignments_bulk_assign - Added new plugin. Assign Network Enforcement Targets to an Organization-Wide Policy.
- organizations_policies_global_group_policies_networks_assignments_bulk_delete - Added new plugin. Remove Network Enforcement Targets from an Organization-Wide Policy.
- organizations_policies_global_group_policies_networks_assignments_info - Added new plugin. List Network Enforcement Target Assignments for Organization-Wide policies for the specified organization.
- organizations_policies_global_group_policies_networks_info - Added new plugin. List all available Network Enforcement Targets for an Organization and their associated Organization-Wide Policies if applicable.
- organizations_sase_sites_detach - Added the `items` parameter.
- organizations_sm_admins_roles - Added the `roleId` parameter.
- organizations_sm_admins_roles_info - Added the `roleId` parameter.
- organizations_summary_sustainability_daily_consumer_metrics_networks_info - Added new plugin. Lists daily consumer metrics for networks.
- organizations_summary_sustainability_summary_consumer_metrics_device_categories_aggregated_info - Added new plugin. Lists summary consumer metrics aggregated by device category.
- organizations_summary_sustainability_summary_consumer_metrics_device_categories_info - Added new plugin. Lists available device categories for sustainability metrics with their corresponding device types.
- organizations_summary_sustainability_summary_consumer_metrics_devices_info - Added new plugin. Lists summary consumer metrics for devices.
- organizations_summary_sustainability_summary_consumer_metrics_networks_aggregated_info - Added new plugin. Returns aggregated consumer metrics for all networks in the organization.
- organizations_summary_sustainability_summary_consumer_metrics_networks_info - Added new plugin. Lists summary consumer metrics for networks.
- organizations_summary_switch_power_history_info - Added new plugin. Returns the total PoE power draw for all switch ports in the organization over the requested timespan by default the last 24 hours.
- organizations_webhooks_alert_types_info - Added new plugin. Return a list of alert types to be used with managing webhook alerts.
- organizations_wireless_clients_connections_impacted_by_network_by_ssid_info - Added new plugin. Summarize the number of wireless clients impacted by connection failures on network SSIDs, across an organization.
- organizations_wireless_clients_usage_by_network_by_ssid_info - Added new plugin. Returns client usage details for wireless network SSIDs within an organization.
- organizations_wireless_clients_usage_by_network_info - Added new plugin. Returns client usage details for wireless networks within an organization.
- organizations_wireless_clients_usage_by_ssid_info - Added new plugin. Returns client usage details for SSIDs within an organization.
- organizations_wireless_radio_overrides_by_device_info - Added new plugin. Return a list of radio overrides.
- organizations_wireless_ssids_owe_by_network_info - Added new plugin. Returns an array of objects, each containing OWE transition pairs for the corresponding network.
- organizations_wireless_ssids_profiles - Added new plugin. Create a new SSID profile in an organization.
- organizations_wireless_ssids_profiles_assignments - Added new plugin. Assigns an SSID profile to an SSID in the organization.
- organizations_wireless_ssids_profiles_assignments_by_network_info - Added new plugin. List the SSID profile assignments in an organization, grouped by network.
- organizations_wireless_ssids_profiles_assignments_info - Added new plugin. List the SSID profile assignments in an organization.
- organizations_wireless_ssids_profiles_info - Added new plugin. Returns the SSID profiles for an organization.
- organizations_wireless_ssids_profiles_overviews_info - Added new plugin. Returns the SSID profiles' overview information for an organization.
- plugin_utils/meraki - Added the `meraki_caller` connection option (environment variable `MERAKI_PYTHON_SDK_CALLER`) to set the identifier sent to the API for usage tracking; it defaults to `MerakiAnsibleCollection/2.26.0 Cisco`.
- plugin_utils/meraki - Unified `meraki_compare_equality` and `meraki_compare_equality2` into a single comparison used by every module. Fields missing from the API response are now treated as empty values of the requested type, and values that differ only by type (for example `"1"` and `1`) are considered equal, which avoids reporting `changed` when nothing differs. `meraki_compare_equality2` is kept as a deprecated alias.

Breaking Changes / Porting Guide
--------------------------------

- networks_wireless_clients_connection_stats_info - Removed the `vlan` parameter, which is no longer supported by the Dashboard API.
- networks_wireless_connection_stats_info - Removed the `vlan` parameter, which is no longer supported by the Dashboard API.
- networks_wireless_devices_connection_stats_info - Removed the `vlan` parameter, which is no longer supported by the Dashboard API.
- networks_wireless_failed_connections_info - Removed the `vlan` parameter, which is no longer supported by the Dashboard API.
- networks_wireless_location_scanning - Removed the `ruleId` parameter, which is no longer supported by the Dashboard API.
- organizations_inventory_onboarding_cloud_monitoring_prepare - Removed the module documentation; the cloud monitoring onboarding endpoints were removed from the Dashboard API.
- organizations_sase_sites_attach - Removed the `callback` parameter, which is no longer supported by the Dashboard API.

Bugfixes
--------

- cellular gateway, campus gateway and wireless controller modules - Fixed the SDK family names (`cellulargateway`, `cellular_gateway`, `campusgateway`, `campus_gateway`, `wireless_controller` to `cellularGateway`, `campusGateway`, `wirelessController`). Every `networks_cellular_gateway_*`, `organizations_cellular_gateway_*`, `networks_campus_gateway_*`, `organizations_campus_gateway_*` and `organizations_wireless_controller_*` module failed with an AttributeError before calling the API.
- devices_live_tools_cable_test, devices_live_tools_ping, devices_live_tools_ping_device, devices_live_tools_ports_cycle, devices_live_tools_routing_table_lookups, devices_live_tools_routing_table_summaries, networks_sensor_alerts_profiles, organizations_adaptive_policy_groups, organizations_adaptive_policy_policies, organizations_inventory_devices_swaps_bulk, organizations_splash_assets - The lookup of an existing object by id omitted the required path parameter (`serial`, `networkId` or `organizationId`), so it always failed silently and a new object was created on every run.
- doc_fragments - Corrected the module notes, which referred to the Cisco DNAC SDK and `dnac_` parameters instead of the Cisco Meraki SDK and `meraki_` parameters.
- meraki_action_batch, meraki_syslog, meraki_webhook - Fixed malformed DOCUMENTATION blocks (option descriptions split across lines with invalid indentation) that could not be parsed by ansible-doc.
- networks_vlan_profiles - The lookup by `iname` now sends the required `networkId`, and `iname` (the profile identifier) takes precedence over the display `name` when finding an existing profile.
- networks_vlan_profiles_info - Fixed an AttributeError (missing `get_object` method) when `iname` is provided.
- networks_wireless_ssids, organizations_appliance_security_httpsi_certificates - Fixed EXAMPLES that contained unterminated or generator-placeholder certificate strings.
- organizations_appliance_routing_vrfs_settings, organizations_appliance_security_intrusion, organizations_appliance_vpn_site_to_site_ipsec_peers_slas, organizations_appliance_vpn_third_party_vpn_peers, organizations_branding_policies_priorities, organizations_login_security, organizations_saml, organizations_wireless_mqtt_settings - state=present always failed with "Object does not exists, plugin only has update" because the current settings were never read; these organization-wide singleton resources now use `organizationId` as their identifier.
- organizations_appliance_vpn_third_party_vpn_peers, organizations_appliance_vpn_third_party_vpn_peers_info - Fixed the SDK method names (`getOrganizationApplianceVpnThirdPartyVPNPeers`, `updateOrganizationApplianceVpnThirdPartyVPNPeers`); the previous `...Vpnpeers` names do not exist in any SDK version.

Known Issues
------------

- devices_certificates_revoke, devices_live_tools_route_details, devices_live_tools_route_details_info, organizations_assurance_wireless_experience_successful_connections_by_network_info, organizations_certificates_authorities, organizations_certificates_authorities_info, organizations_certificates_authorities_jobs_info, organizations_certificates_authorities_revoke, organizations_certificates_revocation_lists_info, organizations_devices_certificates_info - These endpoints were added in Dashboard API v1.76.0 and are not yet available in any released Meraki Python SDK (the latest, 4.7.0, covers API v1.75.1). The modules fail until an SDK release that includes them is installed.
- organizations_inventory_onboarding_cloud_monitoring_export_events, organizations_inventory_onboarding_cloud_monitoring_imports, organizations_inventory_onboarding_cloud_monitoring_imports_info, organizations_inventory_onboarding_cloud_monitoring_networks_info, organizations_inventory_onboarding_cloud_monitoring_prepare, organizations_sase_connectors_batch_create - The corresponding endpoints were removed from the Dashboard API (present in v1.69.0, absent since v1.72.0), so these modules can no longer succeed.

v2.25.1
=======

Bugfixes
--------

- devices_management_interface - Removed the erroneous mapping of the create operation to rebootDevice; state=present now always updates the management
  interface, since it is a resource that always pre-exists and has no create operation.
- devices_management_interface - Removed the bare exception handler in get_object_by_name() that swallowed API read failures (including the module's own
  fail_json) and misreported them as the object not existing.
- plugin_utils/meraki - exec_meraki() now fails the task when a write operation's API response explicitly reports "success": false (as rebootDevice and
  similar fire-and-forget endpoints do on rejection), instead of letting the calling module report changed=true/failed=false. Responses without a "success"
  key, and read operations, are unaffected.

v2.25.0
=======

Minor Changes
-------------

- devices_appliance_interfaces_ports_update - Added new plugin to update appliance interface port settings on a device.
- devices_appliance_performance_info - Updated documentation terminology from `MX` to `Secure Appliance or Secure Router`.
- devices_appliance_uplinks_settings - Updated documentation terminology from `MX appliance` to `secure router or security appliance`.
- devices_camera_clip_info - Clarified the `imagerId` parameter documentation for multi-imager cameras.
- devices_cellular_geolocations - Added new plugin to update cellular geolocation settings on a device.
- devices_cellular_uplinks_bands_masks_update - Added new plugin to update cellular uplink band masks on a device.
- devices_live_tools_ports_cycle - Added new plugin to request a live port cycle on a device.
- devices_live_tools_ports_cycle_info - Added new plugin to retrieve the results of a live port cycle request.
- devices_live_tools_ports_status - Added new plugin to request live port status information for a device.
- devices_live_tools_ports_status_info - Added new plugin to retrieve the results of a live port status request.
- devices_live_tools_power_usage - Added new plugin to request live power usage information for a device.
- devices_live_tools_power_usage_info - Added new plugin to retrieve the results of a live power usage request.
- devices_live_tools_routing_table_lookups - Added new plugin to request a live routing table lookup on a device.
- devices_live_tools_routing_table_lookups_info - Added new plugin to retrieve the results of a routing table lookup request.
- devices_live_tools_routing_table_summaries - Added new plugin to request a live routing table summary on a device.
- devices_live_tools_routing_table_summaries_info - Added new plugin to retrieve the results of a routing table summary request.
- devices_switch_ports_cycle - Clarified that this module targets non-Catalyst MS devices; use devices_live_tools_ports_cycle for Catalyst support.
- devices_switch_routing_interfaces - Added support for the new `mtu` parameter on switch routing interfaces.
- networks_appliance_devices_redundancy - Added new plugin to manage appliance device redundancy settings.
- networks_appliance_devices_redundancy_swap - Added new plugin to swap the primary and warm spare appliance in a redundant pair.
- networks_appliance_firewall_l7_firewall_rules - Documented the `rules.value` shape per rule type, including the new allowedCountries/blockedCountries values and their backward-compatible whitelistedCountries/blacklistedCountries aliases.
- networks_appliance_interfaces_l3 - Added new plugin to manage layer 3 appliance interfaces.
- networks_appliance_ports - Added support for the new `sgt` (Security Group Tag) parameter.
- networks_appliance_prefixes_delegated_statics - Clarified that the `interfaces` suboption is required when the prefix origin type is `internet`.
- networks_appliance_umbrella_domains_exclusions - Added new plugin to manage Cisco Umbrella domain exclusions.
- networks_appliance_umbrella_policies_add - Added new plugin to add Cisco Umbrella protection policies.
- networks_appliance_umbrella_policies_remove - Added new plugin to remove Cisco Umbrella protection policies.
- networks_appliance_umbrella_protection - Added new plugin to manage Cisco Umbrella protection settings.
- networks_appliance_vlans - Added support for the new `sgt` (Security Group Tag) and `vrf` configuration options on VLANs.
- networks_appliance_vpn_bgp - Clarified that the `asNumber` setting is only configurable for Auto VPN BGP networks.
- networks_appliance_vpn_site_to_site_vpn - Added support for the new `sgt` (Security Group Tag) parameter for site-to-site VPN peers.
- networks_camera_quality_retention_profiles - Added quality and retention support for additional camera models (MV14, MV24, MV34, MV44X, MV54N, MV64, MV74, MV94) and documented the new `axisVideoQuality` response field.
- networks_devices_syslog_servers - Added new plugin to update network device syslog server settings.
- networks_snmp - Added support for the new `authentication` and `privacy` SNMPv3 parameters.
- networks_switch_settings - Added support for the new `portChannelFallback` parameter.
- networks_switch_stacks - Added support for the new `members` parameter to manage switch stack membership.
- networks_switch_stacks_routing_interfaces - Added support for the new `mtu` parameter on switch stack routing interfaces.
- networks_syslog_servers - Documented that this plugin is deprecated in favor of networks_devices_syslog_servers.
- networks_syslog_servers_info - Documented that this plugin is deprecated in favor of organizations_devices_syslog_servers_by_network_info.
- networks_webhooks_http_servers - Documented the new built-in Push payload template (`wpt_00008`).
- networks_wireless_rf_profiles - Added support for the new 320 MHz channel width option on the 6 GHz radio band.
- networks_wireless_ssids - Added support for the new `security` parameter, including WPA3 encryption settings (`akms` and `ciphers`).
- networks_wireless_ssids_info - Documented additional read-only SSID response fields, including `psk`, `dot11w`, `dot11r`, RADIUS server `id`/`radsecEnabled`, and the new `security` block.
- networks_wireless_ssids_splash_settings - Added support for the new `userConsent` parameter (consent message and required flag).
- organizations - Added support for the new `privacy` parameter.
- organizations_api_rest_provisioning_pipelines_jobs_overviews_by_pipeline_info - Documented the new `byJobOperation` breakdown in the pipeline jobs overview response.
- organizations_appliance_devices_interfaces_l3_info - Added new plugin to retrieve layer 3 appliance interfaces across an organization.
- organizations_appliance_devices_interfaces_ports_by_device_info - Added new plugin to retrieve appliance interface ports by device across an organization.
- organizations_appliance_devices_ports_transceivers_readings_history_by_device_info - Added new plugin to retrieve appliance port transceiver reading history by device.
- organizations_appliance_devices_redundancy_by_network_info - Added new plugin to retrieve appliance device redundancy status by network.
- organizations_appliance_interfaces_packets_overviews_by_device_info - Added new plugin to retrieve appliance interface packet overviews by device.
- organizations_appliance_routing_vrfs_settings - Added new plugin to manage appliance VRF routing settings.
- organizations_appliance_routing_vrfs_settings_info - Added new plugin to retrieve appliance VRF routing settings.
- organizations_appliance_vpn_third_party_vpn_peers - Added the new umbrella_short_lived and secure IPsec policy presets, and documented the new BGP `receiveLimit` field.
- organizations_assurance_alerts_dismiss - Clarified that missing or inaccessible alert IDs return a 404.
- organizations_assurance_alerts_overview_by_type_info - Added the new `includeDeviceTags` and `includeNetworks` query parameters and documented the expanded alert overview response fields.
- organizations_assurance_alerts_restore - Clarified that missing or inaccessible alert IDs return a 404.
- organizations_devices_cellular_data_devices_info - Added new plugin to retrieve devices eligible for cellular data plans.
- organizations_devices_cellular_data_profiles - Added new plugin to manage cellular data profiles.
- organizations_devices_cellular_data_profiles_assignments_batch_create - Added new plugin to batch create cellular data profile assignments.
- organizations_devices_cellular_data_profiles_assignments_bulk_delete - Added new plugin to bulk delete cellular data profile assignments.
- organizations_devices_cellular_data_profiles_assignments_info - Added new plugin to retrieve cellular data profile assignments.
- organizations_devices_cellular_data_profiles_info - Added new plugin to retrieve cellular data profiles.
- organizations_devices_cellular_data_usage_by_device_info - Added new plugin to retrieve current cellular data usage by device.
- organizations_devices_cellular_data_usage_history_by_device_by_interval_info - Added new plugin to retrieve historical cellular data usage by device and interval.
- organizations_devices_cellular_geolocations_info - Added new plugin to retrieve the latest cellular geolocation for devices.
- organizations_devices_cellular_uplinks_bands_by_device_info - Added new plugin to retrieve cellular uplink bands by device.
- organizations_devices_cellular_uplinks_towers_by_device_info - Added new plugin to retrieve cellular uplink tower information by device.
- organizations_devices_syslog_servers_by_network_info - Added new plugin to retrieve device syslog servers by network.
- organizations_devices_syslog_servers_roles_by_network_info - Added new plugin to retrieve device syslog server roles by network.
- organizations_inventory_orders_preview - Documented the new `resolution` field in the inventory order preview response.
- organizations_login_security - Added support for the new `enforceLockedIpSessions` parameter.
- organizations_policy_objects - Documented that the `ipAndMask` policy object type is deprecated in favor of `cidr`.
- organizations_sase_integrations - Added new plugin to manage SASE integrations.
- organizations_sase_integrations_info - Added new plugin to retrieve SASE integrations.

Bugfixes
--------

- devices - Renamed `organization_id` to `organizationId` in the request object and dropped the `serial`/`organizationId` entries from the update-comparison logic.
- devices_cellular_sims - Corrected the eSIM documentation, replacing the fixed reference to `sim3` with guidance to use the device's actual raw eSIM slot (e.g., sim2 or sim3).
- devices_live_tools_leds_blink - Renamed `leds_blink_id` to `ledsBlinkId` and removed the `ledsBlinkId` entry from the update-comparison logic.
- devices_live_tools_mac_table - Renamed `mac_table_id` to `macTableId` and removed it from the update-comparison logic.
- devices_live_tools_multicast_routing - Fixed the internal `multicastRoutingId` key mapping (previously stored as `multicast_routing_id`) and removed it from the update-comparison logic.
- devices_live_tools_ping - Removed the `id` entry from the update-comparison logic.
- devices_live_tools_ping_device - Removed the `id` entry from the update-comparison logic.
- devices_sensor_commands - Renamed `command_id` to `commandId` and removed the `commandId` entry from the update-comparison logic.
- devices_switch_ports - Renamed `port_id` to `portId` and removed the `portId` entry from the update-comparison logic.
- devices_switch_routing_interfaces - Removed the erroneous `interfaceId` entry from the update-comparison logic.
- devices_switch_routing_interfaces_dhcp - Renamed `interface_id` to `interfaceId` and removed the `interfaceId` entry from the update-comparison logic.
- devices_switch_routing_static_routes - Removed the `staticRouteId` entry from the update-comparison logic.
- devices_wireless_bluetooth_settings - Fixed a malformed UUID in the module's EXAMPLES block.
- devices_wireless_zigbee_enrollments - Fixed the internal `enrollmentId` key mapping (previously stored as `enrollment_id`) and removed it from the update-comparison logic.
- networks_appliance_content_filtering_categories_info - Corrected the RETURN type from `dict` to `list`.
- networks_appliance_firewall_cellular_firewall_rules_info - Corrected the RETURN type from `dict` to `list`.
- networks_appliance_firewall_firewalled_services - Removed the `service` entry from the update-comparison logic.
- networks_appliance_firewall_l3_firewall_rules_info - Corrected the RETURN type from `dict` to `list`.
- networks_appliance_firewall_l7_firewall_rules_info - Corrected the RETURN type from `dict` to `list`.
- networks_appliance_firewall_one_to_many_nat_rules_info - Corrected the RETURN type from `dict` to `list`.
- networks_appliance_firewall_one_to_one_nat_rules_info - Corrected the RETURN type from `dict` to `list`.
- networks_appliance_ports - Fixed the internal `portId` parameter key mapping (previously stored as `port_id`) and removed it from the update-comparison logic since it is a path identifier.
- networks_appliance_prefixes_delegated_statics - Removed the `staticDelegatedPrefixId` entry from the update-comparison logic.
- networks_appliance_ssids - Removed the `number` entry from the update-comparison logic.
- networks_appliance_static_routes - Corrected the `gatewayVlanId` argument type from `str` to `int`, and removed the path-identifier `staticRouteId` field from the update-comparison logic.
- networks_appliance_traffic_shaping_custom_performance_classes - Fixed the internal `customPerformanceClassId` key mapping and removed it from the update-comparison logic since it is a path identifier.
- networks_appliance_vlans - Removed `vlanId` from the update-comparison logic since it is the path identifier, not a body field to compare.
- networks_camera_wireless_profiles - Removed the `wirelessProfileId` entry from the update-comparison logic.
- networks_clients_policy - Renamed `client_id` to `clientId` and removed the `clientId` entry from the update-comparison logic.
- networks_clients_splash_authorization_status - Renamed `client_id` to `clientId` and removed the `clientId` entry from the update-comparison logic.
- networks_firmware_upgrades_staged_groups - Removed the `groupId` entry from the update-comparison logic.
- networks_floor_plans - Removed the `floorPlanId` entry from the update-comparison logic.
- networks_group_policies - Removed the `groupPolicyId` entry from the update-comparison logic.
- networks_meraki_auth_users - Removed the `merakiAuthUserId` entry from the update-comparison logic.
- networks_sensor_alerts_profiles - Removed the `id` entry from the update-comparison logic.
- networks_sensor_mqtt_brokers - Renamed `mqtt_broker_id` to `mqttBrokerId` and removed the `mqttBrokerId` entry from the update-comparison logic.
- networks_sm_bypass_activation_lock_attempts - Fixed the internal `networkId`/`attemptId` key mapping and removed `attemptId` from the update-comparison logic.
- networks_sm_target_groups - Removed the `targetGroupId` entry from the update-comparison logic.
- networks_sm_user_access_devices_delete - Renamed `user_access_device_id` to `userAccessDeviceId` in the request object.
- networks_switch_access_policies - Removed the `accessPolicyNumber` entry from the update-comparison logic.
- networks_switch_dhcp_server_policy_arp_inspection_trusted_servers - Removed the `trustedServerId` entry from the update-comparison logic.
- networks_switch_link_aggregations - Removed `linkAggregationId` from the update-comparison logic since it is a path identifier.
- networks_switch_port_schedules - Removed the `portScheduleId` entry from the update-comparison logic.
- networks_switch_qos_rules_order - Removed the `qosRuleId` entry from the update-comparison logic and deleted the line that force-overwrote `current_obj["networkId"]` before comparison.
- networks_switch_routing_multicast_rendezvous_points - Removed the `rendezvousPointId` entry from the update-comparison logic.
- networks_switch_stacks - Fixed `update()` so switch stack updates are now actually sent via updateNetworkSwitchStack instead of silently returning the unmodified previous object, and corrected a lowercase `switchstackid` key typo in `delete()`.
- networks_switch_stacks_add - Renamed `switch_stack_id` to `switchStackId` in the request object.
- networks_switch_stacks_remove - Renamed `switch_stack_id` to `switchStackId` in the request object.
- networks_switch_stacks_routing_interfaces - Removed `switchStackId` and `interfaceId` from the update-comparison logic since they are path identifiers, not body fields.
- networks_switch_stacks_routing_interfaces_dhcp - Fixed the internal `switchStackId`/`interfaceId` key mapping and removed them from the update-comparison logic.
- networks_switch_stacks_routing_static_routes - Removed the `switchStackId` and `staticRouteId` entries from the update-comparison logic.
- networks_traffic_shaping_application_categories_info - Corrected the RETURN type from `dict` to `list`.
- networks_webhooks_http_servers - Removed the `httpServerId` entry from the update-comparison logic.
- networks_webhooks_payload_templates - Fixed an invalid `headers` argument type declaration (`"['array', 'null']"` corrected to `list`) and removed the `payloadTemplateId` entry from the update-comparison logic.
- networks_wireless_air_marshal_rules - Renamed `rule_id` to `ruleId` and removed the `ruleId` entry from the update-comparison logic.
- networks_wireless_bluetooth_settings - Fixed a malformed UUID in the module's EXAMPLES block.
- networks_wireless_ethernet_ports_profiles - Fixed the internal `networkId`/`profileId` key mapping and removed `profileId` from the update-comparison logic.
- networks_wireless_location_scanning - Renamed `network_id` to `networkId` in the request object.
- networks_wireless_rf_profiles - Removed the `rfProfileId` entry from the update-comparison logic.
- networks_wireless_ssids - Corrected "RADSEC" casing to "RadSec" throughout the RADIUS accounting/authentication and RadSec tunnel documentation.
- networks_wireless_ssids_bonjour_forwarding - Removed the `number` entry from the update-comparison logic.
- networks_wireless_ssids_device_type_group_policies - Removed the `number` entry from the update-comparison logic.
- networks_wireless_ssids_eap_override - Removed the `number` entry from the update-comparison logic.
- networks_wireless_ssids_firewall_l3_firewall_rules - Removed the `number` entry from the update-comparison logic.
- networks_wireless_ssids_firewall_l7_firewall_rules - Removed the `number` entry from the update-comparison logic.
- networks_wireless_ssids_hotspot20 - Removed the `number` entry from the update-comparison logic.
- networks_wireless_ssids_identity_psks - Removed the `number` and `identityPskId` entries from the update-comparison logic.
- networks_wireless_ssids_schedules - Removed the `number` entry from the update-comparison logic.
- networks_wireless_ssids_traffic_shaping_rules - Removed the `number` entry from the update-comparison logic.
- networks_wireless_ssids_vpn - Removed the `number` entry from the update-comparison logic.
- organizations - Removed `organizationId` from the update-comparison logic since it is a path identifier.
- organizations_action_batches - Removed the `organizationId` and `actionBatchId` entries from the update-comparison logic.
- organizations_adaptive_policy_acls - Removed the `aclId` entry from the update-comparison logic.
- organizations_adaptive_policy_groups - Removed the `id` entry from the update-comparison logic.
- organizations_adaptive_policy_policies - Removed the `id` entry from the update-comparison logic.
- organizations_admins - Removed the `adminId` entry from the update-comparison logic.
- organizations_alerts_profiles - Fixed the internal `organizationId`/`alertConfigId` key mapping and removed them from the update-comparison logic.
- organizations_appliance_dns_local_profiles - Removed the `organizationId` and `profileId` entries from the update-comparison logic.
- organizations_appliance_dns_local_records - Removed the `organizationId` and `recordId` entries from the update-comparison logic.
- organizations_appliance_dns_split_profiles - Removed the `organizationId` and `profileId` entries from the update-comparison logic.
- organizations_appliance_security_intrusion - Removed the `organizationId` entry from the update-comparison logic.
- organizations_appliance_vpn_site_to_site_ipsec_peers_slas - Renamed `organization_id` to `organizationId` and removed the `organizationId` entry from the update-comparison logic.
- organizations_appliance_vpn_third_party_vpn_peers - Removed the `organizationId` entry from the update-comparison logic.
- organizations_appliance_vpn_vpn_firewall_rules - Removed the `organizationId` entry from the update-comparison logic.
- organizations_branding_policies - Removed the `brandingPolicyId` entry from the update-comparison logic.
- organizations_camera_custom_analytics_artifacts - Renamed `artifact_id` to `artifactId` and removed the `artifactId` entry from the update-comparison logic.
- organizations_cellular_gateway_esims_inventory - Renamed `organization_id` to `organizationId` and removed the `id` entry from the update-comparison logic.
- organizations_cellular_gateway_esims_service_providers_accounts - Fixed a duplicate `accountId` keyword argument that caused a Python syntax error and prevented the plugin from loading, and removed the redundant `id` entry from the update-comparison logic.
- organizations_config_templates_switch_profiles_ports - Fixed the internal `configTemplateId`/`profileId`/`portId` key mapping and removed `profileId`/`portId` from the update-comparison logic.
- organizations_devices_controller_migrations - Removed the `organizationId` entry from the update-comparison logic.
- organizations_devices_packet_capture_captures - Fixed the internal `organizationId`/`captureId` key mapping and removed them from the update-comparison logic.
- organizations_devices_packet_capture_captures_download_url_generate - Renamed `capture_id` to `captureId` in the request object.
- organizations_devices_packet_capture_captures_stop - Renamed `capture_id` to `captureId` in the request object.
- organizations_devices_packet_capture_schedules - Removed the `organizationId` and `scheduleId` entries from the update-comparison logic.
- organizations_early_access_features_opt_ins - Removed the `optInId` entry from the update-comparison logic.
- organizations_inventory_onboarding_cloud_monitoring_imports - Removed the `organizationId` entry from the update-comparison logic.
- organizations_insight_monitored_media_servers - Removed `monitoredMediaServerId` from the update-comparison logic since it is a path identifier.
- organizations_licenses - Fixed the internal `organizationId`/`licenseId` key mapping and removed them from the update-comparison logic.
- organizations_networks_moves - Removed the `organizationId` entry from the update-comparison logic.
- organizations_policies_global_firewall_rulesets - Removed the `organizationId` and `rulesetId` entries from the update-comparison logic.
- organizations_policies_global_firewall_rulesets_rules - Removed the `organizationId` and `ruleId` entries from the update-comparison logic.
- organizations_policies_global_group_policies - Removed the `organizationId` and `policyId` entries from the update-comparison logic.
- organizations_policies_global_group_policies_firewall_rulesets_assignments - Removed the `organizationId` and `assignmentId` entries from the update-comparison logic.
- organizations_policy_objects - Removed the `policyObjectId` entry from the update-comparison logic.
- organizations_policy_objects_groups - Removed the `policyObjectGroupId` entry from the update-comparison logic.
- organizations_saml_idps - Removed the `idpId` entry from the update-comparison logic.
- organizations_saml_roles - Removed the `samlRoleId` entry from the update-comparison logic.
- organizations_sase_sites - Fixed a duplicate `siteId` keyword argument in the request object that caused a Python syntax error and prevented the plugin from loading.
- organizations_sm_admins_roles - Removed the `organizationId` entry from the update-comparison logic.
- organizations_splash_assets - Fixed the internal `organizationId` key mapping and removed the erroneous `id` comparison from the update-comparison logic.
- organizations_splash_themes - Removed the `id` entry from the update-comparison logic.
- organizations_splash_themes_assets - Renamed `theme_identifier` to `themeIdentifier` in the request object.
- organizations_switch_ports_by_switch_info - Corrected the RETURN type from `dict` to `list` to accurately reflect that the API returns one entry per switch.
- organizations_webhooks_logs_info - Corrected the documented maximum lookback/timespan window from 90/31 days to the actual 30-day limit.
- organizations_wireless_devices_provisioning_deployments - Removed the `organizationId` and `deploymentId` entries from the update-comparison logic.
- organizations_wireless_devices_radsec_certificates_authorities - Corrected "RADSEC" casing to "RadSec" in the module description.
- organizations_wireless_devices_radsec_certificates_authorities - Removed the `organizationId` entry from the update-comparison logic.
- organizations_wireless_location_scanning_receivers - Removed the `organizationId` and `receiverId` entries from the update-comparison logic.
- organizations_wireless_mqtt_settings - Renamed `organization_id` to `organizationId` and removed the `organizationId` entry from the update-comparison logic.
- organizations_wireless_ssids_firewall_isolation_allowlist_entries - Removed the `organizationId` and `entryId` entries from the update-comparison logic.
- organizations_wireless_zigbee_devices - Renamed `organization_id` to `organizationId` and removed the `organizationId` and `id` entries from the update-comparison logic.
- organizations_wireless_zigbee_disenrollments - Fixed the internal `organizationId`/`disenrollmentId` key mapping and removed them from the update-comparison logic.
- organizations_wireless_zigbee_door_locks - Fixed the internal `organizationId`/`doorLockId` key mapping and removed them from the update-comparison logic.

v2.24.2
=======

Bugfixes
--------

- Invocation parameter added to the result.

v2.24.1
=======

Minor Changes
-------------

- Fixed problem with networks_wireless_ssids module.

v2.24.0
=======

Minor Changes
-------------

- devices_camera_clip_info - Added new plugin to retrieve camera clip information.
- networks_appliance_uplinks_nat - Added new plugin to manage appliance uplink NAT settings.
- organizations_api_rest_provisioning_pipelines_jobs_info - Added new plugin to retrieve REST API provisioning pipeline job information.
- organizations_api_rest_provisioning_pipelines_jobs_overviews_by_pipeline_info - Added new plugin to retrieve pipeline job overviews grouped by pipeline.
- organizations_appliance_uplinks_nat_by_network_info - Added new plugin to retrieve appliance uplink NAT settings by network.
- organizations_policies_global_firewall_application_categories_info - Added new plugin to retrieve global firewall application categories.
- organizations_policies_global_firewall_rulesets - Added new plugin to manage global firewall rulesets.
- organizations_policies_global_firewall_rulesets_info - Added new plugin to retrieve global firewall rulesets.
- organizations_policies_global_firewall_rulesets_rules - Added new plugin to manage global firewall ruleset rules.
- organizations_policies_global_firewall_rulesets_rules_info - Added new plugin to retrieve global firewall ruleset rules.
- organizations_policies_global_group_policies - Added new plugin to manage global group policies.
- organizations_policies_global_group_policies_adaptive_policy_groups_assign - Added new plugin to assign adaptive policy groups to global group policies.
- organizations_policies_global_group_policies_adaptive_policy_groups_assignments_info - Added new plugin to retrieve adaptive policy group assignments.
- organizations_policies_global_group_policies_adaptive_policy_groups_remove - Added new plugin to remove adaptive policy groups from global group policies.
- organizations_policies_global_group_policies_appliance_vlans_assign - Added new plugin to assign appliance VLANs to global group policies.
- organizations_policies_global_group_policies_appliance_vlans_assignments_by_vlan_info - Added new plugin to retrieve appliance VLAN assignments grouped by VLAN.
- organizations_policies_global_group_policies_appliance_vlans_assignments_info - Added new plugin to retrieve appliance VLAN assignments for global group policies.
- organizations_policies_global_group_policies_appliance_vlans_remove - Added new plugin to remove appliance VLANs from global group policies.
- organizations_policies_global_group_policies_firewall_rulesets_assignments - Added new plugin to manage firewall ruleset assignments for global group policies.
- organizations_policies_global_group_policies_firewall_rulesets_assignments_info - Added new plugin to retrieve firewall ruleset assignments for global group policies.
- organizations_policies_global_group_policies_info - Added new plugin to retrieve global group policies.
- organizations_sase_connectors_batch_create - Added new plugin to batch create SASE connectors.
- organizations_sase_connectors_batch_delete - Added new plugin to batch delete SASE connectors.
- organizations_sase_connectors_info - Added new plugin to retrieve SASE connector information.
- organizations_sase_regions_info - Added new plugin to retrieve SASE region information.
- organizations_sase_sites - Added new plugin to manage SASE sites.
- organizations_sase_sites_attach - Added new plugin to attach networks to SASE sites.
- organizations_sase_sites_connectivity_history_by_site_info - Added new plugin to retrieve SASE site connectivity history.
- organizations_sase_sites_connectivity_overview_info - Added new plugin to retrieve SASE site connectivity overview.
- organizations_sase_sites_detach - Added new plugin to detach networks from SASE sites.
- organizations_sase_sites_info - Added new plugin to retrieve SASE site information.

Maintenance
-----------

- Applied autopep8 formatting (PEP8 compliance) across all action and module plugins.

v2.23.2
=======

Bugfixes
--------

- devices_switch_ports - Fixed AttributeError crash in ``update()`` caused by ``get_object_by_name`` returning the full port list instead of ``None`` when no port matched by name. Added ``isinstance(prev_obj_name, dict)`` guard to prevent calling ``.get()`` on a list.
- devices_switch_ports - Fixed idempotency regression where the module always reported ``changed`` due to ``serial`` (a path parameter absent from the API response) and ``portId`` (int/string type mismatch) being incorrectly included in the ``requires_update`` comparison.
- networks_appliance_static_routes - Added new plugin.
- networks_appliance_static_routes_info - Added new plugin.

v2.23.1
=======

Bugfixes
--------

- Fixing problem of naming in organizations_appliance_vpn_third_party_vpnpeers_info.
- Restructuring README.md file.

v2.23.0
=======

Minor Changes
-------------

- Added new modules and action plugins for Cisco Umbrella account connect/disconnect, Wireless AutoRF (RRM) settings, third-party VPN peers, organization integrations, inventory EoX overview, network moves, SASE eligible networks, and wireless device provisioning deployments.
- networks_wireless_settings: added multicast-to-unicast conversion support.
- organizations_inventory_devices_info: added eoxStatuses filtering and included EoX fields in returned inventory device data.

v2.22.1
=======

Bugfixes
--------

- Fix parameter naming in organizations_inventory_claim.py to use camelCase for consistency with existing code.

v2.22.0
=======

Minor Changes
-------------

- Updated with v1.66.0 dashboard API, adding new plugins and fixing bugs.

v2.21.9
=======

Bugfixes
--------

- administered_licensing_subscription_subscriptions_bind - Fixed parameter naming from 'subscription_id' to 'subscriptionId' for proper API compatibility
- networks_appliance_content_filtering - Enhanced idempotency by extracting category IDs from blockedUrlCategories before comparison
- meraki.py plugin utils - Added type checking in has_diff_elem2 function to prevent errors when comparing lists of non-dictionary elements

v2.21.8
=======

Bugfixes
--------

- "networks_switch_qos_rules_order: extend object lookup to include srcPortRange and dstPortRange when matching existing QoS rules to improve idempotency"

v2.21.7
=======

Bugfixes
--------

- "Enhanced networks_switch_qos_rules_order object lookup logic to properly match QoS rules by vlan, protocol, srcPort, and dstPort parameters"
- "Fixed parameter handling in networks_switch_switch_qos_rules_order to use qosRuleId instead of id for object identification"
- "Improved meraki_compare_equality2 function to handle None value comparisons more accurately"
- "Updated networks_switch_qos_rules_order playbook with corrected parameter values and VLAN configuration"

v2.21.6
=======

Bugfixes
--------

- "Fixed function name typo in organizations_appliance_vpn_third_party_vpnpeers - changed 'getOrganizationApplianceVpnThirdPartyVpnpeers' to 'getOrganizationApplianceVpnThirdPartyVPNPeers'"
- "Fixed function name typo in organizations_appliance_vpn_third_party_vpnpeers - changed 'updateOrganizationApplianceVpnThirdPartyVpnpeers' to 'updateOrganizationApplianceVpnThirdPartyVPNPeers'"
- "Fixed comparison function call in networks_switch_dscp_to_cos_mappings - changed 'meraki_compare_equality2' to 'meraki_compare_equality'"
- "Fixed VLAN parameter handling in networks_switch_qos_rules_order - changed name parameter to vlan parameter for proper object lookup"
- "Improved dictionary comparison logic in meraki.py plugin utils to handle nested dictionaries correctly"

Features
--------
- "Added new organizations_appliance_vpn_stats_info module and action plugin for retrieving VPN history statistics for networks in an organization"
- "Added new playbook for networks_switch_dscp_to_cos_mappings configuration"
- "Added new playbook for organizations_appliance_vpn_third_party_vpnpeers configuration"
- "Enhanced networks_switch_qos_rules_order with improved VLAN handling and debugging capabilities"


v2.21.5
=======

Bugfixes
--------

- cisco.meraki.devices_appliance_uplinks_settings - fix idempotency error.

v2.21.4
=======

Bugfixes
--------

- cisco.meraki.networks_appliance_traffic_shaping_uplink_bandwidth - fix idempotency error.

v2.21.3
=======

Bugfixes
--------

- cisco.meraki.devices_cellular_sims - fix idempotency error.

v2.21.2

Bugfixes
--------

- cisco.meraki.networks_appliance_firewall_l7_firewall_rules - fix idempotency error.

v2.21.1
=======

Bugfixes
--------

- cisco.meraki.devices_switch_ports - fix get_object_by_name method.

v2.21.0
=======

Minor Changes
-------------

- plugins/action/devices_sensor_commands - new plugin.
- plugins/action/devices_sensor_commands_info - new plugin.
- plugins/action/networks_appliance_firewall_multicast_forwarding - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles_assignments_bulk_create - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles_assignments_bulk_delete - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles_assignments_info - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles_info - new plugin.
- plugins/action/organizations_appliance_dns_local_records - new plugin.
- plugins/action/organizations_appliance_dns_local_records_info - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles_assignments_bulk_create - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles_assignments_bulk_delete - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles_assignments_info - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles_info - new plugin.
- plugins/action/organizations_appliance_firewall_multicast_forwarding_by_network_info - new plugin.
- plugins/action/organizations_devices_controller_migrations - new plugin.
- plugins/action/organizations_devices_controller_migrations_info - new plugin.
- plugins/action/organizations_devices_system_memory_usage_history_by_interval_info - new plugin.
- plugins/action/organizations_integrations_xdr_networks_disable - new plugin.
- plugins/action/organizations_integrations_xdr_networks_enable - new plugin.
- plugins/action/organizations_integrations_xdr_networks_info - new plugin.
- plugins/action/organizations_switch_ports_usage_history_by_device_by_interval_info - new plugin.
- plugins/action/organizations_wireless_devices_power_mode_history_info - new plugin.
- plugins/action/organizations_wireless_devices_system_cpu_load_history_info - new plugin.
- plugins/action/organizations_wireless_ssids_firewall_isolation_allowlist_entries - new plugin.
- plugins/action/organizations_wireless_ssids_firewall_isolation_allowlist_entries_info - new plugin.

v2.20.10
========

Bugfixes
--------

- cisco.meraki.networks_wireless_ssids refactor parameter handling to avoid None values

v2.20.9
=======

Bugfixes
--------

- Fixed parameter handling for `update_by_id_params` in cisco.meraki.networks_wireless_ssids to correctly map the following parameters
  - `perClientBandwidthLimitDown`
  - `perClientBandwidthLimitUp`
  - `perSsidBandwidthLimitDown`
  - `perSsidBandwidthLimitUp`
  - `defaultVlanId`
  - `radiusAccountingInterimInterval`
  - `radiusGuestVlanId`
  - `vlanId`
  - `radiusServerAttemptsLimit`
  - `radiusServerTimeout`
- Added validation for `radiusServerAttemptsLimit` with choices `[1, 2, 3, 4, 5]`.
- Added validation for `radiusServerTimeout` with a range of valid values `[1-10]`.
- cisco.meraki.devices_wireless_radio_settings changed compare equality method to use `meraki_compare_equality`

v2.20.8
=======

Bugfixes
--------

- cisco.meraki.organizations_login_security module update organization security settings.

v2.20.7
=======

Bugfixes
--------

- cisco.meraki.networks_appliance_traffic_shaping_rules Always Pushes Configuration Even When Unchanged.
- Changes at compare equality function.
- Unable to create Syslog Server Object. Action module manually fixing.

v2.20.6
=======

Bugfixes
--------

- cisco.meraki.devices_switch_ports idempotency error fixed.

v2.20.5
=======

Bugfixes
--------

- cisco.meraki.networks_devices_claim failed with error unexpected keyword argument 'add_atomically' - bad naming solved.
- cisco.meraki.networks_appliance_firewall_l3_firewall_rules fails with "Unexpected failure during module execution 'rules' - specific 'rules' extraction has been removed.
- cisco.meraki.networks_appliance_vlans_settings fails with "msg" "Object does not exists, plugin only has update" - specific 'vlansEnabled' extraction has been removed.

v2.20.4
=======

Bugfixes
--------

- Issue fixes for workflow-ansible-lint.
- Change alias 'message' to 'message_rule' due is a reserved ansible word in meraki_mx_intrusion_prevention module.
- Old playbook tests removed.

v2.20.3
=======

Bugfixes
--------

- README fixes.

v2.20.2
=======

Bugfixes
--------

- runtime updated requires_ansible from 2.14.0 to '>=2.15.0'.

v2.20.1
=======

Minor Changes
-------------

- Sanity and CI fixes.

v2.20.0
=======

Minor Changes
-------------

- administered_identities_me_api_keys_info - new plugin.
- administered_identities_me_api_keys_revoke - new plugin.
- devices_live_tools_leds_blink - new plugin.
- devices_wireless_electronic_shelf_label - new plugin.
- devices_wireless_electronic_shelf_label_info - new plugin.
- networks_appliance_sdwan_internet_policies - new plugin.
- networks_cancel - new plugin.
- networks_floor_plans_auto_locate_jobs_batch - new plugin.
- networks_floor_plans_devices_batch_update - new plugin.
- networks_publish - new plugin.
- networks_recalculate - new plugin.
- networks_wireless_air_marshal_rules - new plugin.
- networks_wireless_air_marshal_rules_delete - new plugin.
- networks_wireless_air_marshal_rules_update - new plugin.
- networks_wireless_air_marshal_settings - new plugin.
- networks_wireless_electronic_shelf_label - new plugin.
- organizations_assets - new plugin.
- organizations_assurance_alerts_info - new plugin.
- organizations_assurance_alerts_overview_by_network_info - new plugin.
- organizations_assurance_alerts_overview_by_type_info - new plugin.
- organizations_assurance_alerts_overview_historical_info - new plugin.
- organizations_assurance_alerts_overview_info - new plugin.
- organizations_assurance_alerts_restore - new plugin.
- organizations_cellular_gateway_esims_inventory_info - new plugin.
- organizations_cellular_gateway_esims_service_providers_accounts - new plugin.
- organizations_cellular_gateway_esims_service_providers_accounts_communication_plans_info - new plugin.
- organizations_cellular_gateway_esims_service_providers_accounts_info - new plugin.
- organizations_cellular_gateway_esims_service_providers_accounts_rate_plans_info - new plugin.
- organizations_cellular_gateway_esims_service_providers_info - new plugin.
- organizations_cellular_gateway_esims_swap - new plugin.
- organizations_devices_details_bulk_update - new plugin.
- organizations_devices_overview_by_model_info - new plugin.
- organizations_floor_plans_auto_locate_devices_info - new plugin.
- organizations_floor_plans_auto_locate_statuses_info - new plugin.
- organizations_splash_themes - new plugin.
- organizations_splash_themes_info - new plugin.
- organizations_summary_top_applications_by_usage_info - new plugin.
- organizations_summary_top_applications_categories_by_usage_info - new plugin.
- organizations_switch_ports_clients_overview_by_device_info - new plugin.
- organizations_switch_ports_overview_info - new plugin.
- organizations_switch_ports_statuses_by_switch_info - new plugin.
- organizations_switch_ports_topology_discovery_by_device_info - new plugin.
- organizations_wireless_air_marshal_rules_info - new plugin.
- organizations_wireless_air_marshal_settings_by_network_info - new plugin.
- organizations_wireless_clients_overview_by_device_info - new plugin.
- organizations_wireless_controller_clients_overview_history_by_device_by_interval_info - new plugin.
- organizations_wireless_controller_connections_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l2_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l2_statuses_change_history_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l2_usage_history_by_interval_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l3_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l3_statuses_change_history_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l3_usage_history_by_interval_info - new plugin.
- organizations_wireless_controller_devices_interfaces_packets_overview_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_usage_history_by_interval_info - new plugin.
- organizations_wireless_controller_devices_redundancy_failover_history_info - new plugin.
- organizations_wireless_controller_devices_redundancy_statuses_info - new plugin.
- organizations_wireless_controller_devices_system_utilization_history_by_interval_info - new plugin.
- organizations_wireless_controller_overview_by_device_info - new plugin.
- organizations_wireless_devices_wireless_controllers_by_device_info - new plugin.
- organizations_wireless_radio_auto_rf_channels_recalculate - new plugin.
- organizations_wireless_rf_profiles_assignments_by_device_info - new plugin.
- organizations_wireless_ssids_statuses_by_device_info - new plugin.

v2.19.0
=======

Bugfixes
--------

- Ansible utils requirements updated.
- cisco.meraki.networks_switch_stacks delete stack not working, fixing path parameters.
- cisco.meraki.networks_clients_info - incorrect API endpoint, fixing info module.

v2.18.2
=======

Minor Changes
-------------

- Include networks_appliance_traffic_shaping_custom_performance_classes_info plugin.

v2.18.1
=======

Minor Changes
-------------

- The `id` parameter is now required for `networks_appliance_vlans` module.
- The `id` parameter is change type to an `integer` in `networks_appliance_vlans` module.
- Fixing problem of naming in `organizations_appliance_vpn_third_party_vpnpeers_info`.
- Removing `state` from allowed parameters for `networks_syslog_servers` module.

v2.18.0
=======

Minor Changes
-------------

- Ansible collection now support v1.44.1 of Dashboard Api.
- administered_licensing_subscription_entitlements_info - new plugin.
- administered_licensing_subscription_subscriptions_bind - new plugin.
- administered_licensing_subscription_subscriptions_claim_key_validate - new plugin.
- administered_licensing_subscription_subscriptions_claim - new plugin.
- administered_licensing_subscription_subscriptions_compliance_statuses_info - new plugin.
- administered_licensing_subscription_subscriptions_info - new plugin.
- devices_appliance_radio_settings_info - new plugin.
- devices_appliance_radio_settings - new plugin.
- devices_live_tools_arp_table_info - new plugin.
- devices_live_tools_arp_table - new plugin.
- devices_live_tools_cable_test_info - new plugin.
- devices_live_tools_cable_test - new plugin.
- devices_live_tools_throughput_test_info - new plugin.
- devices_live_tools_throughput_test - new plugin.
- devices_live_tools_wake_on_lan_info - new plugin.
- devices_live_tools_wake_on_lan - new plugin.
- devices_wireless_alternate_management_interface_ipv6 - new plugin.
- networks_appliance_rf_profiles_info - new plugin.
- networks_appliance_rf_profiles - new plugin.
- networks_appliance_traffic_shaping_vpn_exclusions - new plugin.
- networks_sm_devices_install_apps - new plugin.
- networks_sm_devices_reboot - new plugin.
- networks_sm_devices_shutdown - new plugin.
- networks_sm_devices_uninstall_apps - new plugin.
- networks_vlan_profiles_assignments_by_device_info - new plugin.
- networks_vlan_profiles_assignments_reassign - new plugin.
- networks_vlan_profiles_info - new plugin.
- networks_vlan_profiles - new plugin.
- networks_wireless_ethernet_ports_profiles_assign - new plugin.
- networks_wireless_ethernet_ports_profiles_info - new plugin.
- networks_wireless_ethernet_ports_profiles_set_default - new plugin.
- networks_wireless_ethernet_ports_profiles - new plugin.
- organizations_appliance_traffic_shaping_vpn_exclusions_by_network_info - new plugin.
- organizations_appliance_uplinks_statuses_overview_info - new plugin.
- organizations_appliance_uplinks_usage_by_network_info - new plugin.
- organizations_camera_boundaries_areas_by_device_info - new plugin.
- organizations_camera_boundaries_lines_by_device_info - new plugin.
- organizations_camera_detections_history_by_boundary_by_interval_info - new plugin.
- organizations_camera_permissions_info - new plugin.
- organizations_camera_roles_info - new plugin.
- organizations_camera_roles - new plugin.
- organizations_devices_availabilities_change_history_info - new plugin.
- organizations_devices_boots_history_info - new plugin.
- organizations_sm_admins_roles_info - new plugin.
- organizations_sm_admins_roles - new plugin.
- organizations_sm_sentry_policies_assignments_by_network_info - new plugin.
- organizations_sm_sentry_policies_assignments - new plugin.
- organizations_summary_top_networks_by_status_info - new plugin.
- organizations_webhooks_callbacks_statuses_info - new plugin.
- organizations_wireless_devices_channel_utilization_by_device_info - new plugin.
- organizations_wireless_devices_channel_utilization_by_network_info - new plugin.
- organizations_wireless_devices_channel_utilization_history_by_device_by_interval_info - new plugin.
- organizations_wireless_devices_channel_utilization_history_by_network_by_interval_info - new plugin.
- organizations_wireless_devices_packet_loss_by_client_info - new plugin.
- organizations_wireless_devices_packet_loss_by_device_info - new plugin.
- organizations_wireless_devices_packet_loss_by_network_info - new plugin.

v2.17.2
=======

Bugfixes
--------

- Adding `smartquotes = False` to `conf.py` and romoving `'` from rst files.

v2.17.1
=======

Bugfixes
--------

- Adding build_ignore property to galaxy file.

v2.17.0
=======

Minor Changes
-------------

- Adding support to ansible.utils ">=2.0.0, <4.00".

v2.16.17
========

Bugfixes
--------

- Adding support to ansible.utils >=3.0

v2.16.16
========

Bugfixes
--------

- Idempotency bugs fixed in devices_switch_ports.
- Adding `product_types` for update request on networks.
- networks_syslog_servers is now just an Update action to API.
- Parameter`organization_id` change to `organizationId` organizations_claim.
- Parameter`organization_id` change to `organizationId` organizations_clone.
- Parameter`organization_id` change to `organizationId` organizations_inventory_claim.
- Parameter`organization_id` change to `organizationId` organizations_inventory_onboarding_cloud_monitoring_export_events.
- Parameter`organization_id` change to `organizationId` organizations_inventory_onboarding_cloud_monitoring_prepare.
- Parameter`organization_id` change to `organizationId` organizations_inventory_release.
- Parameter`organization_id` change to `organizationId` organizations_licenses_assign_seats.
- Parameter`organization_id` change to `organizationId` organizations_licenses_move.
- Parameter`organization_id` change to `organizationId` organizations_licenses_move_seats.
- Parameter`organization_id` change to `organizationId` organizations_licenses_renew_seats.
- Parameter`organization_id` change to `organizationId` organizations_licensing_coterm_licenses_move.
- Parameter`organization_id` change to `organizationId` organizations_networks_combine.
- Parameter`organization_id` change to `organizationId` organizations_switch_devices_clone.
- Parameter`organization_id` change to `organizationId` organizations_users.
- Removing logs in meraki.py.

v2.16.15
========

Bugfixes
--------

- Adding `network_clients_info` and `network_client_info`.
- Adding `platform_meraki.rst` to docs.

v2.16.14
========

Bugfixes
--------

- Adding condition to avoid error on exists on devices.

v2.16.13
=======

Bugfixes
--------

- Meraki Compare Equality 2 added.

v2.16.12
=======

Bugfixes
-------------

- New condition added to Meraki Compare Equality.
- Devices module documentation fixed.

v2.16.11
=======

Bugfixes
-------------

- Bad naming `networkId` parameter in `networks_appliance_traffic_shaping_custom_performance_classes`.
- Bad naming `networkId` parameter in `networks_appliance_warm_spare_swap`.
- Bad naming `networkId` parameter in `networks_bind`.
- Bad naming `networkId` parameter in `networks_clients_provision`.
- Bad naming `networkId` parameter in `networks_firmware_upgrades_rollbacks`.
- Bad naming `networkId` parameter in `networks_firmware_upgrades_staged_events_rollbacks`.
- Bad naming `networkId` parameter in `networks_mqtt_brokers`.
- Bad naming `networkId` parameter in `networks_pii_requests_delete`.
- Bad naming `networkId` parameter in `networks_sm_devices_checkin`.
- Bad naming `networkId` parameter in `networks_sm_devices_lock`.
- Bad naming `networkId` parameter in `networks_sm_devices_modify_tags`.
- Bad naming `networkId` parameter in `networks_sm_devices_move`.
- Bad naming `networkId` parameter in `networks_sm_devices_refresh_details`.
- Bad naming `networkId` parameter in `networks_sm_devices_unenroll`.
- Bad naming `networkId` parameter in `networks_sm_devices_wipe`.
- Bad naming `networkId` parameter in `networks_sm_user_access_devices_delete`.
- Bad naming `networkId` parameter in `networks_split`.
- Bad naming `networkId` parameter in `networks_switch_stacks_add`.
- Bad naming `networkId` parameter in `networks_switch_stacks_remove`.
- Bad naming `networkId` parameter in `networks_unbind`.
- Bad naming `networkId` parameter in `networks_sm_devices_fields`.

v2.16.10
=======

Bugfixes
-------------

- Returning requires_ansible to >=2.14.0
- Bad naming `networkId` parameter in `networks_devices_remove` and `networks_devices_claim_vmx`

v2.16.5
=======

Bugfixes
-------------

- cisco.meraki.organizations_login_security module will not update org api authentication - fixing for look at organizations_login_security.

v2.16.4
=======

Bugfixes
-------------

- cisco.meraki.networks_devices_claim - got an unexpected keyword argument 'network_id', bug with parameter naming.

v2.16.3
=======

Bugfixes
-------------

- Removing ignores.

v2.16.2
=======

Bugfixes
-------------

- Updating documentation, yml fixes - Documentation Broken.

v2.16.1
=======

Bugfixes
-------------

- Updating collection docs link.

v2.16.0
=======

Minor Changes
-------------

- administered_identities_me_info - new plugin.
- devices_appliance_performance_info - new plugin.
- devices_appliance_uplinks_settings_info - new plugin.
- devices_appliance_uplinks_settings - new plugin.
- devices_appliance_vmx_authentication_token - new plugin.
- devices_blink_leds - new plugin.
- devices_camera_analytics_live_info - new plugin.
- devices_camera_custom_analytics_info - new plugin.
- devices_camera_custom_analytics - new plugin.
- devices_camera_generate_snapshot - new plugin.
- devices_camera_quality_and_retention_info - new plugin.
- devices_camera_quality_and_retention - new plugin.
- devices_camera_sense_info - new plugin.
- devices_camera_sense - new plugin.
- devices_camera_video_link_info - new plugin.
- devices_camera_video_settings_info - new plugin.
- devices_camera_video_settings - new plugin.
- devices_camera_wireless_profiles_info - new plugin.
- devices_camera_wireless_profiles - new plugin.
- devices_cellular_gateway_lan_info - new plugin.
- devices_cellular_gateway_lan - new plugin.
- devices_cellular_gateway_port_forwarding_rules_info - new plugin.
- devices_cellular_gateway_port_forwarding_rules - new plugin.
- devices_cellular_sims_info - new plugin.
- devices_cellular_sims - new plugin.
- devices_info - new plugin.
- devices_live_tools_ping_device_info - new plugin.
- devices_live_tools_ping_device - new plugin.
- devices_live_tools_ping_info - new plugin.
- devices_live_tools_ping - new plugin.
- devices_lldp_cdp_info - new plugin.
- devices_management_interface_info - new plugin.
- devices_management_interface - new plugin.
- devices_sensor_relationships_info - new plugin.
- devices_sensor_relationships - new plugin.
- devices_switch_ports_cycle - new plugin.
- devices_switch_ports_info - new plugin.
- devices_switch_ports_statuses_info - new plugin.
- devices_switch_ports - new plugin.
- devices_switch_routing_interfaces_dhcp_info - new plugin.
- devices_switch_routing_interfaces_dhcp - new plugin.
- devices_switch_routing_interfaces_info - new plugin.
- devices_switch_routing_interfaces - new plugin.
- devices_switch_routing_static_routes_info - new plugin.
- devices_switch_routing_static_routes - new plugin.
- devices_switch_warm_spare_info - new plugin.
- devices_switch_warm_spare - new plugin.
- devices_wireless_bluetooth_settings_info - new plugin.
- devices_wireless_bluetooth_settings - new plugin.
- devices_wireless_connection_stats_info - new plugin.
- devices_wireless_latency_stats_info - new plugin.
- devices_wireless_radio_settings_info - new plugin.
- devices_wireless_radio_settings - new plugin.
- devices_wireless_status_info - new plugin.
- devices - new plugin.
- networks_alerts_history_info - new plugin.
- networks_alerts_settings_info - new plugin.
- networks_alerts_settings - new plugin.
- networks_appliance_connectivity_monitoring_destinations_info - new plugin.
- networks_appliance_connectivity_monitoring_destinations - new plugin.
- networks_appliance_content_filtering_categories_info - new plugin.
- networks_appliance_content_filtering_info - new plugin.
- networks_appliance_content_filtering - new plugin.
- networks_appliance_firewall_cellular_firewall_rules_info - new plugin.
- networks_appliance_firewall_cellular_firewall_rules - new plugin.
- networks_appliance_firewall_firewalled_services_info - new plugin.
- networks_appliance_firewall_firewalled_services - new plugin.
- networks_appliance_firewall_inbound_firewall_rules_info - new plugin.
- networks_appliance_firewall_inbound_firewall_rules - new plugin.
- networks_appliance_firewall_l3_firewall_rules_info - new plugin.
- networks_appliance_firewall_l3_firewall_rules - new plugin.
- networks_appliance_firewall_l7_firewall_rules_application_categories_info - new plugin.
- networks_appliance_firewall_l7_firewall_rules_info - new plugin.
- networks_appliance_firewall_l7_firewall_rules - new plugin.
- networks_appliance_firewall_one_to_many_nat_rules_info - new plugin.
- networks_appliance_firewall_one_to_many_nat_rules - new plugin.
- networks_appliance_firewall_one_to_one_nat_rules_info - new plugin.
- networks_appliance_firewall_one_to_one_nat_rules - new plugin.
- networks_appliance_firewall_port_forwarding_rules_info - new plugin.
- networks_appliance_firewall_port_forwarding_rules - new plugin.
- networks_appliance_firewall_settings_info - new plugin.
- networks_appliance_firewall_settings - new plugin.
- networks_appliance_ports_info - new plugin.
- networks_appliance_ports - new plugin.
- networks_appliance_prefixes_delegated_statics_info - new plugin.
- networks_appliance_prefixes_delegated_statics - new plugin.
- networks_appliance_security_intrusion_info - new plugin.
- networks_appliance_security_intrusion - new plugin.
- networks_appliance_security_malware_info - new plugin.
- networks_appliance_security_malware - new plugin.
- networks_appliance_settings_info - new plugin.
- networks_appliance_settings - new plugin.
- networks_appliance_single_lan_info - new plugin.
- networks_appliance_single_lan - new plugin.
- networks_appliance_ssids_info - new plugin.
- networks_appliance_ssids - new plugin.
- networks_appliance_traffic_shaping_custom_performance_classes - new plugin.
- networks_appliance_traffic_shaping_info - new plugin.
- networks_appliance_traffic_shaping_rules_info - new plugin.
- networks_appliance_traffic_shaping_rules - new plugin.
- networks_appliance_traffic_shaping_uplink_bandwidth_info - new plugin.
- networks_appliance_traffic_shaping_uplink_bandwidth - new plugin.
- networks_appliance_traffic_shaping_uplink_selection_info - new plugin.
- networks_appliance_traffic_shaping_uplink_selection - new plugin.
- networks_appliance_traffic_shaping - new plugin.
- networks_appliance_vlans_info - new plugin.
- networks_appliance_vlans_settings_info - new plugin.
- networks_appliance_vlans_settings - new plugin.
- networks_appliance_vlans - new plugin.
- networks_appliance_vpn_bgp_info - new plugin.
- networks_appliance_vpn_bgp - new plugin.
- networks_appliance_vpn_site_to_site_vpn_info - new plugin.
- networks_appliance_vpn_site_to_site_vpn - new plugin.
- networks_appliance_warm_spare_info - new plugin.
- networks_appliance_warm_spare_swap - new plugin.
- networks_appliance_warm_spare - new plugin.
- networks_bind - new plugin.
- networks_bluetooth_clients_info - new plugin.
- networks_camera_quality_retention_profiles_info - new plugin.
- networks_camera_quality_retention_profiles - new plugin.
- networks_camera_wireless_profiles_info - new plugin.
- networks_camera_wireless_profiles - new plugin.
- networks_cellular_gateway_connectivity_monitoring_destinations_info - new plugin.
- networks_cellular_gateway_connectivity_monitoring_destinations - new plugin.
- networks_cellular_gateway_dhcp_info - new plugin.
- networks_cellular_gateway_dhcp - new plugin.
- networks_cellular_gateway_subnet_pool_info - new plugin.
- networks_cellular_gateway_subnet_pool - new plugin.
- networks_cellular_gateway_uplink_info - new plugin.
- networks_cellular_gateway_uplink - new plugin.
- networks_clients_info - new plugin.
- networks_clients_overview_info - new plugin.
- networks_clients_policy_info - new plugin.
- networks_clients_policy - new plugin.
- networks_clients_provision - new plugin.
- networks_clients_splash_authorization_status_info - new plugin.
- networks_clients_splash_authorization_status - new plugin.
- networks_devices_claim_vmx - new plugin.
- networks_devices_claim - new plugin.
- networks_devices_remove - new plugin.
- networks_events_event_types_info - new plugin.
- networks_events_info - new plugin.
- networks_firmware_upgrades_info - new plugin.
- networks_firmware_upgrades_rollbacks - new plugin.
- networks_firmware_upgrades_staged_events_defer - new plugin.
- networks_firmware_upgrades_staged_events_info - new plugin.
- networks_firmware_upgrades_staged_events_rollbacks - new plugin.
- networks_firmware_upgrades_staged_events - new plugin.
- networks_firmware_upgrades_staged_groups_info - new plugin.
- networks_firmware_upgrades_staged_groups - new plugin.
- networks_firmware_upgrades_staged_stages_info - new plugin.
- networks_firmware_upgrades_staged_stages - new plugin.
- networks_firmware_upgrades - new plugin.
- networks_floor_plans_info - new plugin.
- networks_floor_plans - new plugin.
- networks_group_policies_info - new plugin.
- networks_group_policies - new plugin.
- networks_health_alerts_info - new plugin.
- networks_info - new plugin.
- networks_insight_applications_health_by_time_info - new plugin.
- networks_meraki_auth_users_info - new plugin.
- networks_meraki_auth_users - new plugin.
- networks_mqtt_brokers - new plugin.
- networks_netflow_info - new plugin.
- networks_netflow - new plugin.
- networks_pii_pii_keys_info - new plugin.
- networks_pii_requests_delete - new plugin.
- networks_pii_requests_info - new plugin.
- networks_pii_sm_devices_for_key_info - new plugin.
- networks_pii_sm_owners_for_key_info - new plugin.
- networks_policies_by_client_info - new plugin.
- networks_sensor_alerts_current_overview_by_metric_info - new plugin.
- networks_sensor_alerts_overview_by_metric_info - new plugin.
- networks_sensor_alerts_profiles_info - new plugin.
- networks_sensor_alerts_profiles - new plugin.
- networks_sensor_mqtt_brokers_info - new plugin.
- networks_sensor_mqtt_brokers - new plugin.
- networks_sensor_relationships_info - new plugin.
- networks_settings_info - new plugin.
- networks_settings - new plugin.
- networks_sm_bypass_activation_lock_attempts_info - new plugin.
- networks_sm_bypass_activation_lock_attempts - new plugin.
- networks_sm_devices_cellular_usage_history_info - new plugin.
- networks_sm_devices_certs_info - new plugin.
- networks_sm_devices_checkin - new plugin.
- networks_sm_devices_connectivity_info - new plugin.
- networks_sm_devices_desktop_logs_info - new plugin.
- networks_sm_devices_device_command_logs_info - new plugin.
- networks_sm_devices_device_profiles_info - new plugin.
- networks_sm_devices_fields - new plugin.
- networks_sm_devices_info - new plugin.
- networks_sm_devices_lock - new plugin.
- networks_sm_devices_modify_tags - new plugin.
- networks_sm_devices_move - new plugin.
- networks_sm_devices_network_adapters_info - new plugin.
- networks_sm_devices_performance_history_info - new plugin.
- networks_sm_devices_refresh_details - new plugin.
- networks_sm_devices_security_centers_info - new plugin.
- networks_sm_devices_unenroll - new plugin.
- networks_sm_devices_wipe - new plugin.
- networks_sm_devices_wlan_lists_info - new plugin.
- networks_sm_profiles_info - new plugin.
- networks_sm_target_groups_info - new plugin.
- networks_sm_target_groups - new plugin.
- networks_sm_trusted_access_configs_info - new plugin.
- networks_sm_user_access_devices_delete - new plugin.
- networks_sm_user_access_devices_info - new plugin.
- networks_sm_users_device_profiles_info - new plugin.
- networks_sm_users_info - new plugin.
- networks_sm_users_softwares_info - new plugin.
- networks_snmp_info - new plugin.
- networks_snmp - new plugin.
- networks_split - new plugin.
- networks_switch_access_control_lists_info - new plugin.
- networks_switch_access_control_lists - new plugin.
- networks_switch_access_policies_info - new plugin.
- networks_switch_access_policies - new plugin.
- networks_switch_alternate_management_interface_info - new plugin.
- networks_switch_alternate_management_interface - new plugin.
- networks_switch_dhcp_server_policy_arp_inspection_trusted_servers_info - new plugin.
- networks_switch_dhcp_server_policy_arp_inspection_trusted_servers - new plugin.
- networks_switch_dhcp_server_policy_arp_inspection_warnings_by_device_info - new plugin.
- networks_switch_dhcp_server_policy_info - new plugin.
- networks_switch_dhcp_server_policy - new plugin.
- networks_switch_dhcp_v4_servers_seen_info - new plugin.
- networks_switch_dscp_to_cos_mappings_info - new plugin.
- networks_switch_dscp_to_cos_mappings - new plugin.
- networks_switch_link_aggregations_info - new plugin.
- networks_switch_link_aggregations - new plugin.
- networks_switch_mtu_info - new plugin.
- networks_switch_mtu - new plugin.
- networks_switch_port_schedules_info - new plugin.
- networks_switch_port_schedules - new plugin.
- networks_switch_qos_rules_order_info - new plugin.
- networks_switch_qos_rules_order - new plugin.
- networks_switch_routing_multicast_info - new plugin.
- networks_switch_routing_multicast_rendezvous_points_info - new plugin.
- networks_switch_routing_multicast_rendezvous_points - new plugin.
- networks_switch_routing_multicast - new plugin.
- networks_switch_routing_ospf_info - new plugin.
- networks_switch_routing_ospf - new plugin.
- networks_switch_settings_info - new plugin.
- networks_switch_settings - new plugin.
- networks_switch_stacks_add - new plugin.
- networks_switch_stacks_info - new plugin.
- networks_switch_stacks_remove - new plugin.
- networks_switch_stacks_routing_interfaces_dhcp_info - new plugin.
- networks_switch_stacks_routing_interfaces_dhcp - new plugin.
- networks_switch_stacks_routing_interfaces_info - new plugin.
- networks_switch_stacks_routing_interfaces - new plugin.
- networks_switch_stacks_routing_static_routes_info - new plugin.
- networks_switch_stacks_routing_static_routes - new plugin.
- networks_switch_stacks - new plugin.
- networks_switch_storm_control_info - new plugin.
- networks_switch_storm_control - new plugin.
- networks_switch_stp_info - new plugin.
- networks_switch_stp - new plugin.
- networks_syslog_servers_info - new plugin.
- networks_syslog_servers - new plugin.
- networks_topology_link_layer_info - new plugin.
- networks_traffic_analysis_info - new plugin.
- networks_traffic_analysis - new plugin.
- networks_traffic_shaping_application_categories_info - new plugin.
- networks_traffic_shaping_dscp_tagging_options_info - new plugin.
- networks_unbind - new plugin.
- networks_webhooks_http_servers_info - new plugin.
- networks_webhooks_http_servers - new plugin.
- networks_webhooks_payload_templates_info - new plugin.
- networks_webhooks_payload_templates - new plugin.
- networks_webhooks_webhook_tests_info - new plugin.
- networks_wireless_alternate_management_interface_info - new plugin.
- networks_wireless_alternate_management_interface - new plugin.
- networks_wireless_billing_info - new plugin.
- networks_wireless_billing - new plugin.
- networks_wireless_bluetooth_settings_info - new plugin.
- networks_wireless_bluetooth_settings - new plugin.
- networks_wireless_channel_utilization_history_info - new plugin.
- networks_wireless_client_count_history_info - new plugin.
- networks_wireless_clients_connection_stats_info - new plugin.
- networks_wireless_clients_latency_stats_info - new plugin.
- networks_wireless_connection_stats_info - new plugin.
- networks_wireless_data_rate_history_info - new plugin.
- networks_wireless_devices_connection_stats_info - new plugin.
- networks_wireless_failed_connections_info - new plugin.
- networks_wireless_latency_history_info - new plugin.
- networks_wireless_latency_stats_info - new plugin.
- networks_wireless_mesh_statuses_info - new plugin.
- networks_wireless_rf_profiles_info - new plugin.
- networks_wireless_rf_profiles - new plugin.
- networks_wireless_settings_info - new plugin.
- networks_wireless_settings - new plugin.
- networks_wireless_signal_quality_history_info - new plugin.
- networks_wireless_ssids_bonjour_forwarding_info - new plugin.
- networks_wireless_ssids_bonjour_forwarding - new plugin.
- networks_wireless_ssids_device_type_group_policies_info - new plugin.
- networks_wireless_ssids_device_type_group_policies - new plugin.
- networks_wireless_ssids_eap_override_info - new plugin.
- networks_wireless_ssids_eap_override - new plugin.
- networks_wireless_ssids_firewall_l3_firewall_rules_info - new plugin.
- networks_wireless_ssids_firewall_l3_firewall_rules - new plugin.
- networks_wireless_ssids_firewall_l7_firewall_rules_info - new plugin.
- networks_wireless_ssids_firewall_l7_firewall_rules - new plugin.
- networks_wireless_ssids_hotspot20_info - new plugin.
- networks_wireless_ssids_hotspot20 - new plugin.
- networks_wireless_ssids_identity_psks_info - new plugin.
- networks_wireless_ssids_identity_psks - new plugin.
- networks_wireless_ssids_info - new plugin.
- networks_wireless_ssids_schedules_info - new plugin.
- networks_wireless_ssids_schedules - new plugin.
- networks_wireless_ssids_splash_settings_info - new plugin.
- networks_wireless_ssids_splash_settings - new plugin.
- networks_wireless_ssids_traffic_shaping_rules_info - new plugin.
- networks_wireless_ssids_traffic_shaping_rules - new plugin.
- networks_wireless_ssids_vpn_info - new plugin.
- networks_wireless_ssids_vpn - new plugin.
- networks_wireless_ssids - new plugin.
- networks_wireless_usage_history_info - new plugin.
- networks - new plugin.
- organizations_action_batches_info - new plugin.
- organizations_action_batches - new plugin.
- organizations_adaptive_policy_acls_info - new plugin.
- organizations_adaptive_policy_acls - new plugin.
- organizations_adaptive_policy_groups_info - new plugin.
- organizations_adaptive_policy_groups - new plugin.
- organizations_adaptive_policy_overview_info - new plugin.
- organizations_adaptive_policy_policies_info - new plugin.
- organizations_adaptive_policy_policies - new plugin.
- organizations_adaptive_policy_settings_info - new plugin.
- organizations_adaptive_policy_settings - new plugin.
- organizations_admins_info - new plugin.
- organizations_admins - new plugin.
- organizations_alerts_profiles - new plugin.
- organizations_api_requests_info - new plugin.
- organizations_api_requests_overview_info - new plugin.
- organizations_api_requests_overview_response_codes_by_interval_info - new plugin.
- organizations_appliance_security_intrusion_info - new plugin.
- organizations_appliance_security_intrusion - new plugin.
- organizations_appliance_vpn_third_party_vpnpeers_info - new plugin.
- organizations_appliance_vpn_third_party_vpnpeers - new plugin.
- organizations_appliance_vpn_vpn_firewall_rules_info - new plugin.
- organizations_appliance_vpn_vpn_firewall_rules - new plugin.
- organizations_branding_policies_info - new plugin.
- organizations_branding_policies_priorities_info - new plugin.
- organizations_branding_policies_priorities - new plugin.
- organizations_branding_policies - new plugin.
- organizations_camera_custom_analytics_artifacts_info - new plugin.
- organizations_camera_custom_analytics_artifacts - new plugin.
- organizations_cellular_gateway_uplink_statuses_info - new plugin.
- organizations_claim - new plugin.
- organizations_clients_bandwidth_usage_history_info - new plugin.
- organizations_clients_overview_info - new plugin.
- organizations_clients_search_info - new plugin.
- organizations_clone - new plugin.
- organizations_config_templates_info - new plugin.
- organizations_config_templates_switch_profiles_info - new plugin.
- organizations_config_templates_switch_profiles_ports_info - new plugin.
- organizations_config_templates_switch_profiles_ports - new plugin.
- organizations_config_templates - new plugin.
- organizations_devices_availabilities_info - new plugin.
- organizations_devices_info - new plugin.
- organizations_devices_power_modules_statuses_by_device_info - new plugin.
- organizations_devices_provisioning_statuses_info - new plugin.
- organizations_devices_statuses_info - new plugin.
- organizations_devices_statuses_overview_info - new plugin.
- organizations_devices_uplinks_addresses_by_device_info - new plugin.
- organizations_devices_uplinks_loss_and_latency_info - new plugin.
- organizations_early_access_features_info - new plugin.
- organizations_early_access_features_opt_ins_info - new plugin.
- organizations_early_access_features_opt_ins - new plugin.
- organizations_firmware_upgrades_by_device_info - new plugin.
- organizations_firmware_upgrades_info - new plugin.
- organizations_info - new plugin.
- organizations_insight_applications_info - new plugin.
- organizations_insight_monitored_media_servers_info - new plugin.
- organizations_insight_monitored_media_servers - new plugin.
- organizations_inventory_claim - new plugin.
- organizations_inventory_devices_info - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_export_events - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_imports_info - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_imports - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_networks_info - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_prepare - new plugin.
- organizations_inventory_release - new plugin.
- organizations_licenses_assign_seats - new plugin.
- organizations_licenses_info - new plugin.
- organizations_licenses_move_seats - new plugin.
- organizations_licenses_move - new plugin.
- organizations_licenses_overview_info - new plugin.
- organizations_licenses_renew_seats - new plugin.
- organizations_licenses - new plugin.
- organizations_licensing_coterm_licenses_info - new plugin.
- organizations_licensing_coterm_licenses_move - new plugin.
- organizations_login_security_info - new plugin.
- organizations_login_security - new plugin.
- organizations_networks_combine - new plugin.
- organizations_openapi_spec_info - new plugin.
- organizations_policy_objects_groups_info - new plugin.
- organizations_policy_objects_groups - new plugin.
- organizations_policy_objects_info - new plugin.
- organizations_policy_objects - new plugin.
- organizations_saml_idps_info - new plugin.
- organizations_saml_idps - new plugin.
- organizations_saml_info - new plugin.
- organizations_saml_roles_info - new plugin.
- organizations_saml_roles - new plugin.
- organizations_saml - new plugin.
- organizations_sensor_readings_history_info - new plugin.
- organizations_sensor_readings_latest_info - new plugin.
- organizations_sm_apns_cert_info - new plugin.
- organizations_sm_vpp_accounts_info - new plugin.
- organizations_snmp_info - new plugin.
- organizations_snmp - new plugin.
- organizations_summary_top_appliances_by_utilization_info - new plugin.
- organizations_summary_top_clients_by_usage_info - new plugin.
- organizations_summary_top_clients_manufacturers_by_usage_info - new plugin.
- organizations_summary_top_devices_by_usage_info - new plugin.
- organizations_summary_top_devices_models_by_usage_info - new plugin.
- organizations_summary_top_ssids_by_usage_info - new plugin.
- organizations_summary_top_switches_by_energy_usage_info - new plugin.
- organizations_switch_devices_clone - new plugin.
- organizations_switch_ports_by_switch_info - new plugin.
- organizations_uplinks_statuses_info - new plugin.
- organizations_users - new plugin.
- organizations_webhooks_logs_info - new plugin.
- organizations_wireless_devices_ethernet_statuses_info - new plugin.
- organizations - new plugin.

v2.15.3
=======

Bugfixes
--------

- meraki_devices - Fix endpoints due to breaking change in Meraki API v1.33

v2.15.2
=======

Minor Changes
-------------

- meraki_mx_site_to_site_firewall - Fix updating VPN rules per issue 302.

Bugfixes
--------

- Resolved the issue with link negotation at meraki_ms_switchport

v2.15.1
=======

Bugfixes
--------

- Corrects constraints applied to local and remote status page settings to align with API behaviour (https://github.com/CiscoDevNet/ansible-meraki/issues/437)
- Enables meraki_network query by net_id (https://github.com/CiscoDevNet/ansible-meraki/issues/441)
- Resolved an issue where an empty response from the API triggered an exception in module meraki_webhook (https://github.com/CiscoDevNet/ansible-meraki/issues/433)
- Resolves issues with meraki_webhook shared_secret defaulting to null; (https://github.com/CiscoDevNet/ansible-meraki/issues/439); Also adds Test Coverage for shared secret idempotency and resolves test file lint issues.

v2.15.0
=======

Minor Changes
-------------

- New module - meraki_network_settings - Configure detailed settings of a network.

Bugfixes
--------

- Resolved issue
- Update pipeline to use newer version of action to detect changed files.
- meraki_alert - Fix situation where specifying emails may crash.
- meraki_mx_site_to_site_vpn - Check mode should no longer apply changes when enabled.

Known Issues
------------

- meraki_network - Updated documentation for `local_status_page_enabled` and `remote_status_page_enabled` as these no longer work.

v2.14.0
=======

Minor Changes
-------------

- meraki_webhook - Add payload template parameter

Bugfixes
--------

- Fix checkmode on merak webhook payload template update
- meraki_webhook - First error when updating URL in a webhook

v2.13.0
=======

Major Changes
-------------

- meraki_mr_l7_firewall - New module

v2.12.0
=======

Major Changes
-------------

- meraki_webhook_payload_template - New module

Bugfixes
--------

- Update defaults in documentation for new sanity tests
- meraki_device - Fix URL for LLDP and CDP lookups

v2.11.0
=======

Minor Changes
-------------

- Add GPLv3 license. Always was GPLv3, but didn't have the file.
- Change shebang in Sublime utils to point to env instead of direct to the path
- meraki_alert - Change type for opbject to alert_type in examples
- meraki_ms_access_policies - New module to create, delete, update Access Policies in the Switch settings
- meraki_ssid - Add support for `ap_availability_tags`.
- meraki_ssid - Add support for `available_on_all_aps`
- meraki_ssid - Add support for `lan_isolation_enabled`.
- meraki_ssid - Add support for `visible`.

v2.10.1
=======

Minor Changes
-------------

- Change shebang in Sublime utils to point to env instead of direct to the path

v2.10.0
=======

Minor Changes
-------------

- meraki_network - Add support for `copy_from_network_id`.

v2.9.0
======

Bugfixes
--------

- meraki_switchport - Setting VLAN to 0 on trunk port clears the VLAN.

v2.8.0
======

Minor Changes
-------------

- meraki_action_batch - New module for CRUD operations on Meraki Action Batches
- meraki_switchport - Add support for flexible stacking

v2.7.0
======

Minor Changes
-------------

- meraki_mx_network_vlan_settings - New module to enable or disable VLANs on a network
- meraki_mx_third_party_vpn_peers - New module for managing third party VPM peers

Bugfixes
--------

- meraki_mx_static_route - Add support for gateway_vlan_id otherwise requests could error

v2.6.2
======

Minor Changes
-------------

- Add execution-environment.yml in meta as the base to a Meraki ee
- meraki_network - Add Products to net_type list

Bugfixes
--------

- meraki_alert - Updates now properly set default destination webhook
- meraki_syslog -  Fix crash due to incorrect dictionary reference

v2.6.1
======

Minor Changes
-------------

- meraki_ssid - Add support for enterprise_admin_access and splash_guest_sponsor_domains with the latter required for creating a sponsor portal.

Bugfixes
--------

- meraki_mr_rf_profile - Fix issue with idempotency and creation of RF Profiles by name only
- meraki_syslog - Improve reliability for multiple roles or capitalization.

v2.6.0
======

Major Changes
-------------

- meraki_mr_radio - New module

Minor Changes
-------------

- meraki_mx_l7_firewall - Allow passing an empty ruleset to delete all rules
- meraki_utils - Add debugging output for failed socket connections

Bugfixes
--------

- meraki_mr_ssid - Fix issue with SSID removal idempotency when ID doesn't exist

v2.5.0
======

Minor Changes
-------------

- meraki_mr_l3_firewall - Return each MR L3 firewall rule's values in lowercase.
- meraki_mr_ssid - Add support for radius_proxy_enabled SSID setting.
- meraki_mx_l3_firewall - Return each MX L3 firewall rule's values in lowercase.
- meraki_mx_vlan - Fix dhcp_boot_options_enabled parameter

v2.4.2
======

Bugfixes
--------

- Fix some flake8 sanity errors as reported by Ansible Galaxy. Should be no functional change.

v2.4.0
======

Minor Changes
-------------

- meraki_mx_switchport - Improve documentation for response

Bugfixes
--------

- Allow a state of absent in voice vlan to allow the value to be nulled out(https://github.com/CiscoDevNet/ansible-meraki/issues/238)

v2.3.1
======

Bugfixes
--------

- meraki_ms_switchport - link_negotiation choice for 100 Megabit Auto is incorrect causing failures. (https://github.com/CiscoDevNet/ansible-meraki/issues/235).

v2.3.0
======

Minor Changes
-------------

- meraki_ms_switchport - Adding additional functionality to support the access_policy_types "MAC allow list" and "Sticky MAC allow list" port security configuration options. (https://github.com/CiscoDevNet/ansible-meraki/issues/227).
- meraki_mx_intrusion_prevention - Rename message to rule_message to avoid conflicts with internal Ansible variables.

Bugfixes
--------

- meraki_ms_switchport - access_policy_types choices are incorrect causing failures. (https://github.com/CiscoDevNet/ansible-meraki/issues/227).

v2.2.1
======

Bugfixes
--------

- meraki_mx_content_filtering - Fix crash with idempotent condition due to improper sorting

v2.2.0
======

Minor Changes
-------------

- meraki_network - Update documentation to show querying of local or remote settings.
- meraki_ssid - Add Cisco ISE as a splash page option.

Bugfixes
--------

- meraki_network - Fix bug where local or remote settings always show changed.

v2.1.3
======

Bugfixes
--------

- meraki_device - Support pagination. This allows for more than 1,000 devices to be listed at a time.
- meraki_network - Support pagination. This allows for more than 1,000 networks to be listed at a time.

v2.1.2
======

Bugfixes
--------

- Remove test output as it made the collection, and Ansible, huge.

v2.1.1
======

Bugfixes
--------

- meraki_management_interface - Fix crash when modifying a non-MX management interface.

v2.1.0
======

New Modules
-----------

- meraki_alert - Manage alerts in the Meraki cloud
- meraki_mx_l2_interface - Configure MX layer 2 interfaces

v2.0.0
======

Major Changes
-------------

- Rewrite requests method for version 1.0 API and improved readability
- meraki_mr_rf_profile - Configure wireless RF profiles.
- meraki_mr_settings - Configure network settings for wireless.
- meraki_ms_l3_interface - New module
- meraki_ms_ospf - Configure OSPF.

Minor Changes
-------------

- meraki - Add optional debugging for is_update_required() method.
- meraki_admin - Update endpoints for API v1
- meraki_alert - Manage network wide alert settings.
- meraki_device - Added query parameter
- meraki_intrusion_prevention - Change documentation to show proper way to clear rules
- meraki_malware - Update documentation to show how to allow multiple URLs at once.
- meraki_mx_l2_interface - Configure physical interfaces on MX appliances.
- meraki_mx_uplink - Renamed to meraki_mx_uplink_bandwidth
- meraki_ssid - Add `WPA3 Only` and `WPA3 Transition Mode`
- meraki_switchport - Add support for `access_policy_type` parameter

Breaking Changes / Porting Guide
--------------------------------

- meraki_device - Changed tags from string to list
- meraki_device - Removed serial_lldp_cdp parameter
- meraki_device - Removed serial_uplink parameter
- meraki_intrusion_prevention - Rename whitedlisted_rules to allowed_rules
- meraki_mx_l3_firewall - Rule responses are now in a `rules` list
- meraki_mx_l7_firewall - Rename blacklisted_countries to blocked_countries
- meraki_mx_l7_firewall - Rename whitelisted_countries to allowed_countries
- meraki_network - Local and remote status page settings cannot be set during network creation
- meraki_network - `disableRemoteStatusPage` response is now `remote_status_page_enabled`
- meraki_network - `disable_my_meraki_com` response is now `local_status_page_enabled`
- meraki_network - `disable_my_meraki` has been deprecated
- meraki_network - `enable_my_meraki` is now called `local_status_page_enabled`
- meraki_network - `enable_remote_status_page` is now called `remote_status_page_enabled`
- meraki_network - `enabled` response for VLAN status is now `vlans_enabled`
- meraki_network - `tags` and `type` now return a list
- meraki_snmp - peer_ips is now a list
- meraki_switchport - `access_policy_number` is now an int and not a string
- meraki_switchport - `tags` is now a list and not a string
- meraki_webhook - Querying test status now uses state of query.

Security Fixes
--------------

- meraki_webhook - diff output may show data for values set to not display

Bugfixes
--------

- Remove unnecessary files from the collection package, significantly reduces package size
- meraki_admin - Fix error when adding network privileges to admin using network name
- meraki_switch_stack - Fix situation where module may crash due to switch being in or not in a stack already
- meraki_webhook - Proper response is shown when creating webhook test
