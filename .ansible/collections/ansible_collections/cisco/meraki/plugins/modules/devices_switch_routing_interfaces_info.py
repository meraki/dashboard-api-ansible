#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all devices _switch _routing _interfaces.
  - Get devices _switch _routing _interfaces by id.
  - List layer 3 interfaces for a switch. Those for a stack may be found under switch
    stack routing.
  - Return a layer 3 interface for a switch.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: devices_switch_routing_interfaces_info
notes:
  - SDK Method used are switch.Switch.get_device_switch_routing_interface, switch.Switch.get_device_switch_routing_interfaces,
  - Paths used are get /devices/{serial}/switch/routing/interfaces, get /devices/{serial}/switch/routing/interfaces/{interfaceId},
options:
  headers:
    description: Additional headers.
    type: dict
  interfaceId:
    description:
      - InterfaceId path parameter. Interface ID.
    type: str
  serial:
    description:
      - Serial path parameter.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getDeviceSwitchRoutingInterface API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface
    name: Cisco Meraki documentation for switch getDeviceSwitchRoutingInterface
  - description: Complete reference of the getDeviceSwitchRoutingInterfaces API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interfaces
    name: Cisco Meraki documentation for switch getDeviceSwitchRoutingInterfaces
short_description: Information module for devices _switch _routing _interfaces
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all devices _switch _routing _interfaces
  cisco.meraki.devices_switch_routing_interfaces_info:
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
    serial: string
  register: result
- name: Get devices _switch _routing _interfaces by id
  cisco.meraki.devices_switch_routing_interfaces_info:
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
    serial: string
    interfaceId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "defaultGateway": "string",
      "interfaceId": "string",
      "interfaceIp": "string",
      "ipv6": {
        "address": "string",
        "assignmentMode": "string",
        "gateway": "string",
        "prefix": "string"
      },
      "multicastRouting": "string",
      "name": "string",
      "ospfSettings": {
        "area": "string",
        "cost": 0,
        "isPassiveEnabled": true
      },
      "ospfV3": {
        "area": "string",
        "cost": 0,
        "isPassiveEnabled": true
      },
      "subnet": "string",
      "uplinkV4": true,
      "uplinkV6": true,
      "vlanId": 0
    }
"""
