#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource networks _switch _stacks _add.
  - Add a switch to a stack.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_switch_stacks_add
notes:
  - SDK Method used are switch.Switch.add_network_switch_stack,
  - Paths used are post /networks/{networkId}/switch/stacks/{switchStackId}/add,
options:
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  serial:
    description: The serial of the switch to be added.
    type: str
  switchStackId:
    description: SwitchStackId path parameter. Switch stack ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the addNetworkSwitchStack API.
    link: https://developer.cisco.com/meraki/api-v1/#!add-network-switch-stack
    name: Cisco Meraki documentation for switch addNetworkSwitchStack
short_description: Resource module for networks _switch _stacks _add
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_switch_stacks_add:
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
    networkId: string
    serial: QBZY-XWVU-TSRQ
    switchStackId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "isMonitorOnly": true,
      "members": [
        {
          "mac": "string",
          "model": "string",
          "name": "string",
          "role": "string",
          "serial": "string"
        }
      ],
      "name": "string",
      "serials": [
        "string"
      ]
    }
"""
