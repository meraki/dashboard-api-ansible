==========================
Cisco.Meraki Release Notes
==========================

.. contents:: Topics

v2.16.13
=======

Bugfixes
-------------

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
