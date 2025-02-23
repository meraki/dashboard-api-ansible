#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource networks _wireless _ssids _firewall l3
    _firewall _rules.
  - Update the L3 firewall rules of an SSID on an MR network.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_wireless_ssids_firewall_l3_firewall_rules
notes:
  - SDK Method used are wireless.Wireless.update_network_wireless_ssid_firewall_l3_firewall_rules,
  - Paths used are put /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules,
options:
  allowLanAccess:
    description: Allow wireless client access to local LAN (boolean value - true allows
      access and false denies access) (optional).
    type: bool
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  number:
    description: Number path parameter.
    type: str
  rules:
    description: An ordered array of the firewall rules for this SSID (not including
      the local LAN access rule or the default rule).
    elements: dict
    suboptions:
      comment:
        description: Description of the rule (optional).
        type: str
      destCidr:
        description: Comma-separated list of destination IP address(es) (in IP or
          CIDR notation), fully-qualified domain names (FQDN) or 'any'.
        type: str
      destPort:
        description: Comma-separated list of destination port(s) (integer in the range
          1-65535), or 'any'.
        type: str
      policy:
        description: '''allow'' or ''deny'' traffic specified by this rule.'
        type: str
      protocol:
        description: The type of protocol (must be 'tcp', 'udp', 'icmp', 'icmp6' or
          'any').
        type: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateNetworkWirelessSsidFirewallL3FirewallRules
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l3-firewall-rules
    name: Cisco Meraki documentation for wireless updateNetworkWirelessSsidFirewallL3FirewallRules
short_description: Resource module for networks _wireless _ssids _firewall l3 _firewall
  _rules
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_wireless_ssids_firewall_l3_firewall_rules:
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
    allowLanAccess: true
    networkId: string
    number: string
    rules:
      - comment: Allow TCP traffic to subnet with HTTP servers.
        destCidr: 192.168.1.0/24
        destPort: '443'
        policy: allow
        protocol: tcp
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "allowLanAccess": true,
      "rules": [
        {
          "comment": "string",
          "destCidr": "string",
          "destPort": "string",
          "policy": "string",
          "protocol": "string"
        }
      ]
    }
"""
