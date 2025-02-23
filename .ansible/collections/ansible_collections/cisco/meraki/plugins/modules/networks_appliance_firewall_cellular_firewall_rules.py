#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource networks _appliance _firewall _cellular
    _firewall _rules.
  - Update the cellular firewall rules of an MX network.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_appliance_firewall_cellular_firewall_rules
notes:
  - SDK Method used are appliance.Appliance.update_network_appliance_firewall_cellular_firewall_rules,
  - Paths used are put /networks/{networkId}/appliance/firewall/cellularFirewallRules,
options:
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  rules:
    description: An ordered array of the firewall rules (not including the default
      rule).
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
      srcCidr:
        description: Comma-separated list of source IP address(es) (in IP or CIDR
          notation), or 'any' (note FQDN not supported for source addresses).
        type: str
      srcPort:
        description: Comma-separated list of source port(s) (integer in the range
          1-65535), or 'any'.
        type: str
      syslogEnabled:
        description: Log this rule to syslog (true or false, boolean value) - only
          applicable if a syslog has been configured (optional).
        type: bool
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateNetworkApplianceFirewallCellularFirewallRules
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-cellular-firewall-rules
    name: Cisco Meraki documentation for appliance updateNetworkApplianceFirewallCellularFirewallRules
short_description: Resource module for networks _appliance _firewall _cellular _firewall
  _rules
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_appliance_firewall_cellular_firewall_rules:
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
    networkId: string
    rules:
      - comment: Allow TCP traffic to subnet with HTTP servers.
        destCidr: 192.168.1.0/24
        destPort: '443'
        policy: allow
        protocol: tcp
        srcCidr: Any
        srcPort: Any
        syslogEnabled: false
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
