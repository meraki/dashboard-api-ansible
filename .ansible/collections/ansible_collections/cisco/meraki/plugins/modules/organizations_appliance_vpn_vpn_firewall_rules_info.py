#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all organizations _appliance _vpn _vpn _firewall _rules.
  - Return the firewall rules for an organization's site-to-site VPN.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: organizations_appliance_vpn_vpn_firewall_rules_info
notes:
  - SDK Method used are appliance.Appliance.get_organization_appliance_vpn_vpn_firewall_rules,
  - Paths used are get /organizations/{organizationId}/appliance/vpn/vpnFirewallRules,
options:
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getOrganizationApplianceVpnVpnFirewallRules
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-vpn-firewall-rules
    name: Cisco Meraki documentation for appliance getOrganizationApplianceVpnVpnFirewallRules
short_description: Information module for organizations _appliance _vpn _vpn _firewall
  _rules
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all organizations _appliance _vpn _vpn _firewall _rules
  cisco.meraki.organizations_appliance_vpn_vpn_firewall_rules_info:
    meraki_api_key: '{{ meraki_api_key }}'
    meraki_base_url: '{{ meraki_base_url }}'
    meraki_single_request_timeout: '{{ meraki_single_request_timeout }}'
    meraki_certificate_path: '{{ meraki_certificate_path }}'
    meraki_requests_proxy: '{{ meraki_requests_proxy }}'
    meraki_wait_on_rate_limit: '{{ meraki_wait_on_rate_limit }}'
    meraki_nginx_429_retry_wait_time: '{{ meraki_nginx_429_retry_wait_time }}'
    meraki_action_batch_retry_wait_time: '{{ meraki_action_batch_retry_wait_time }}'
    meraki_retry_4xx_error: '{{ meraki_retry_4xx_error }}'
    meraki_retry_4xx_error_wait_time: '{{ meraki_retry_4xx_error_wait_time }}'
    meraki_maximum_retries: '{{ meraki_maximum_retries }}'
    meraki_output_log: '{{ meraki_output_log }}'
    meraki_log_file_prefix: '{{ meraki_log_file_prefix }}'
    meraki_log_path: '{{ meraki_log_path }}'
    meraki_print_console: '{{ meraki_print_console }}'
    meraki_suppress_logging: '{{ meraki_suppress_logging }}'
    meraki_simulate: '{{ meraki_simulate }}'
    meraki_be_geo_id: '{{ meraki_be_geo_id }}'
    meraki_use_iterator_for_get_pages: '{{ meraki_use_iterator_for_get_pages }}'
    meraki_inherit_logging_config: '{{ meraki_inherit_logging_config }}'
    organizationId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "comment": "string",
        "destCidr": "string",
        "destPort": "string",
        "policy": "string",
        "protocol": "string",
        "srcCidr": "string",
        "srcPort": "string",
        "syslogEnabled": true
      }
    ]
"""
