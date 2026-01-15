#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_wireless_zigbee
short_description: Resource module for networks _wireless _zigbee
description:
  - Manage operation update of the resource networks _wireless _zigbee.
  - Update Zigbee Configs for specified network.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  defaults:
    description: Default Settings for Zigbee Devices.
    suboptions:
      channel:
        description: Channel.
        type: str
      transmitPowerLevel:
        description: Transmit Power Level.
        type: int
    type: dict
  enabled:
    description: To enable/disable Zigbee on the network.
    type: bool
  iotController:
    description: Zigbee's IoT controller details.
    suboptions:
      serial:
        description: Device Serial number.
        type: str
    type: dict
  lockManagement:
    description: Login Credentials of on-premises lock management.
    suboptions:
      address:
        description: Host Address.
        type: str
      password:
        description: Password.
        type: str
      username:
        description: Username.
        type: str
    type: dict
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless updateNetworkWirelessZigbee
    description: Complete reference of the updateNetworkWirelessZigbee API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-zigbee
notes:
  - SDK Method used are
    wireless.Wireless.update_network_wireless_zigbee,
  - Paths used are
    put /networks/{networkId}/wireless/zigbee,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_wireless_zigbee:
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
    defaults:
      channel: string
      transmitPowerLevel: 0
    enabled: true
    iotController:
      serial: string
    lockManagement:
      address: string
      password: string
      username: string
    networkId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "network": {
        "id": "string"
      },
      "enabled": true,
      "iotController": {
        "name": "string",
        "mac": "string",
        "serial": "string",
        "status": "string"
      },
      "lockManagement": {
        "address": "string",
        "username": "string",
        "status": "string"
      },
      "defaults": {
        "transmitPowerLevel": 0,
        "channel": "string"
      }
    }
"""
