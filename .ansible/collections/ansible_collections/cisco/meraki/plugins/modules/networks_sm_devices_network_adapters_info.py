#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all networks _sm _devices _network _adapters.
  - List the network adapters of a device.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: networks_sm_devices_network_adapters_info
notes:
  - SDK Method used are sm.Sm.get_network_sm_device_network_adapters,
  - Paths used are get /networks/{networkId}/sm/devices/{deviceId}/networkAdapters,
options:
  deviceId:
    description:
      - DeviceId path parameter. Device ID.
    type: str
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
      - NetworkId path parameter. Network ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getNetworkSmDeviceNetworkAdapters API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-network-adapters
    name: Cisco Meraki documentation for sm getNetworkSmDeviceNetworkAdapters
short_description: Information module for networks _sm _devices _network _adapters
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all networks _sm _devices _network _adapters
  cisco.meraki.networks_sm_devices_network_adapters_info:
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
    deviceId: string
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
        "dhcpServer": "string",
        "dnsServer": "string",
        "gateway": "string",
        "id": "string",
        "ip": "string",
        "mac": "string",
        "name": "string",
        "subnet": "string"
      }
    ]
"""
