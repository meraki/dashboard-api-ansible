#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource networks _appliance _firewall _firewalled
    _services.
  - Updates the accessibility settings for the given service 'ICMP', 'web', or 'SNMP'
    .
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_appliance_firewall_firewalled_services
notes:
  - SDK Method used are appliance.Appliance.update_network_appliance_firewall_firewalled_service,
  - Paths used are put /networks/{networkId}/appliance/firewall/firewalledServices/{service},
options:
  access:
    description: A string indicating the rule for which IPs are allowed to use the
      specified service. Acceptable values are "blocked" (no remote IPs can access
      the service), "restricted" (only allowed IPs can access the service), and "unrestriced"
      (any remote IP can access the service). This field is required.
    type: str
  allowedIps:
    description: An array of allowed IPs that can access the service. This field is
      required if "access" is set to "restricted". Otherwise this field is ignored.
    elements: str
    type: list
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  service:
    description: Service path parameter.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateNetworkApplianceFirewallFirewalledService
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-firewalled-service
    name: Cisco Meraki documentation for appliance updateNetworkApplianceFirewallFirewalledService
short_description: Resource module for networks _appliance _firewall _firewalled _services
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update by id
  cisco.meraki.networks_appliance_firewall_firewalled_services:
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
    state: present
    access: restricted
    allowedIps:
      - 123.123.123.1
    networkId: string
    service: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "access": "string",
      "allowedIps": [
        "string"
      ],
      "service": "string"
    }
"""
