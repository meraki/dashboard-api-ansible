#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource networks _appliance _vpn _site _to _site
    _vpn.
  - Update the site-to-site VPN settings of a network. Only valid for MX networks
    in NAT mode.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_appliance_vpn_site_to_site_vpn
notes:
  - SDK Method used are appliance.Appliance.update_network_appliance_vpn_site_to_site_vpn,
  - Paths used are put /networks/{networkId}/appliance/vpn/siteToSiteVpn,
options:
  hubs:
    description: The list of VPN hubs, in order of preference. In spoke mode, at least
      1 hub is required.
    elements: dict
    suboptions:
      hubId:
        description: The network ID of the hub.
        type: str
      useDefaultRoute:
        description: Only valid in 'spoke' mode. Indicates whether default route traffic
          should be sent to this hub.
        type: bool
    type: list
  mode:
    description: The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'.
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  subnets:
    description: The list of subnets and their VPN presence.
    elements: dict
    suboptions:
      localSubnet:
        description: The CIDR notation subnet used within the VPN.
        type: str
      useVpn:
        description: Indicates the presence of the subnet in the VPN.
        type: bool
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateNetworkApplianceVpnSiteToSiteVpn
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn
    name: Cisco Meraki documentation for appliance updateNetworkApplianceVpnSiteToSiteVpn
short_description: Resource module for networks _appliance _vpn _site _to _site _vpn
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_appliance_vpn_site_to_site_vpn:
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
    hubs:
      - hubId: N_4901849
        useDefaultRoute: true
    mode: spoke
    networkId: string
    subnets:
      - localSubnet: 192.168.1.0/24
        useVpn: true
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "hubs": [
        {
          "hubId": "string",
          "useDefaultRoute": true
        }
      ],
      "mode": "string",
      "subnets": [
        {
          "localSubnet": "string",
          "useVpn": true
        }
      ]
    }
"""
