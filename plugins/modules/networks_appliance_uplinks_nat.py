#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_appliance_uplinks_nat
short_description: Resource module for networks _appliance _uplinks _nat
description:
  - Manage operation update of the resource networks _appliance _uplinks _nat.
  - Update uplink NAT settings of the specified network.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  uplinks:
    description: Per-uplink NAT exception configuration on the network.
    elements: dict
    suboptions:
      interface:
        description: Interface name of the uplink.
        type: str
      nat:
        description: NAT settings of the uplink.
        suboptions:
          enabled:
            description: Whether NAT is enabled on the uplink.
            type: bool
        type: dict
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance updateNetworkApplianceUplinksNat
    description: Complete reference of the updateNetworkApplianceUplinksNat API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-uplinks-nat
notes:
  - SDK Method used are
    appliance.Appliance.update_network_appliance_uplinks_nat,
  - Paths used are
    put /networks/{networkId}/appliance/uplinks/nat,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_appliance_uplinks_nat:
    meraki_api_key: "{{ meraki_api_key }}"
    meraki_base_url: "{{ meraki_base_url }}"
    meraki_single_request_timeout: "{{ meraki_single_request_timeout }}"
    meraki_certificate_path: "{{ meraki_certificate_path }}"
    meraki_requests_proxy: "{{ meraki_requests_proxy }}"
    meraki_wait_on_rate_limit: "{{ meraki_wait_on_rate_limit }}"
    meraki_nginx_429_retry_wait_time: "{{ meraki_nginx_429_retry_wait_time }}"
    meraki_action_batch_retry_wait_time: "{{ meraki_action_batch_retry_wait_time }}"
    meraki_retry_4xx_error: "{{ meraki_retry_4xx_error }}"
    meraki_retry_4xx_error_wait_time: "{{ meraki_retry_4xx_error_wait_time }}"
    meraki_maximum_retries: "{{ meraki_maximum_retries }}"
    meraki_output_log: "{{ meraki_output_log }}"
    meraki_log_file_prefix: "{{ meraki_log_file_prefix }}"
    meraki_log_path: "{{ meraki_log_path }}"
    meraki_print_console: "{{ meraki_print_console }}"
    meraki_suppress_logging: "{{ meraki_suppress_logging }}"
    meraki_simulate: "{{ meraki_simulate }}"
    meraki_be_geo_id: "{{ meraki_be_geo_id }}"
    meraki_caller: "{{ meraki_caller }}"
    meraki_use_iterator_for_get_pages: "{{ meraki_use_iterator_for_get_pages }}"
    meraki_inherit_logging_config: "{{ meraki_inherit_logging_config }}"
    networkId: string
    uplinks:
      - interface: wan1
        nat:
          enabled: false
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "uplinks": [
        {
          "interface": "string",
          "nat": {
            "enabled": true
          }
        }
      ]
    }
"""
