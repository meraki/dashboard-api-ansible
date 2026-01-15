#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_switch_ports_info
short_description: Information module for devices _switch _ports
description:
  - Information module for Devices Switch Ports Info.
  - Get all devices _switch _ports.
  - Get devices _switch _ports by id.
  - List the switch ports for a switch.
  - Return a switch port.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  serial:
    description:
  - Information module for Devices Switch Ports Info.
      - Serial path parameter.
    type: str
  portId:
    description:
  - Information module for Devices Switch Ports Info.
      - PortId path parameter. Port ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for switch getDeviceSwitchPort
    description: Complete reference of the getDeviceSwitchPort API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-switch-port
  - name: Cisco Meraki documentation for switch getDeviceSwitchPorts
    description: Complete reference of the getDeviceSwitchPorts API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports
notes:
  - SDK Method used are
    switch.Switch.get_device_switch_port,
    switch.Switch.get_device_switch_ports,
  - Paths used are
    get /devices/{serial}/switch/ports,
    get /devices/{serial}/switch/ports/{portId},
"""

EXAMPLES = r"""
- name: Get all devices _switch _ports
  cisco.meraki.devices_switch_ports_info:
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
    serial: string
  register: result
- name: Get devices _switch _ports by id
  cisco.meraki.devices_switch_ports_info:
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
    serial: string
    portId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "portId": "string",
      "name": "string",
      "tags": [
        "string"
      ],
      "enabled": true,
      "poeEnabled": true,
      "type": "string",
      "vlan": 0,
      "voiceVlan": 0,
      "allowedVlans": "string",
      "isolationEnabled": true,
      "rstpEnabled": true,
      "stpGuard": "string",
      "stpPortFastTrunk": true,
      "linkNegotiation": "string",
      "linkNegotiationCapabilities": [
        "string"
      ],
      "portScheduleId": "string",
      "schedule": {
        "id": "string",
        "name": "string"
      },
      "udld": "string",
      "accessPolicyType": "string",
      "accessPolicyNumber": 0,
      "macAllowList": [
        "string"
      ],
      "macWhitelistLimit": 0,
      "stickyMacAllowList": [
        "string"
      ],
      "stickyMacAllowListLimit": 0,
      "stormControlEnabled": true,
      "adaptivePolicyGroupId": "string",
      "adaptivePolicyGroup": {
        "id": "string",
        "name": "string"
      },
      "peerSgtCapable": true,
      "flexibleStackingEnabled": true,
      "daiTrusted": true,
      "profile": {
        "enabled": true,
        "id": "string",
        "iname": "string"
      },
      "module": {
        "model": "string",
        "serial": "string",
        "slot": 0
      },
      "mirror": {
        "mode": "string"
      },
      "dot3az": {
        "enabled": true
      },
      "highSpeed": {
        "enabled": true
      }
    }
"""
