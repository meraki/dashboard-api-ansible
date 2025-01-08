#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: devices_cellular_sims_info
short_description: Information module for devices _cellular _sims
description:
- Get all devices _cellular _sims.
- Return the SIM and APN configurations for a cellular device.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  serial:
    description:
    - Serial path parameter.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for devices getDeviceCellularSims
  description: Complete reference of the getDeviceCellularSims API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-sims
notes:
  - SDK Method used are
    devices.Devices.get_device_cellular_sims,

  - Paths used are
    get /devices/{serial}/cellular/sims,
"""

EXAMPLES = r"""
- name: Get all devices _cellular _sims
  cisco.meraki.devices_cellular_sims_info:
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
    meraki_use_iterator_for_get_pages: "{{ meraki_use_iterator_for_get_pages }}"
    meraki_inherit_logging_config: "{{ meraki_inherit_logging_config }}"
    serial: string
  register: result

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "simFailover": {
        "enabled": true,
        "timeout": 0
      },
      "simOrdering": [
        "string"
      ],
      "sims": [
        {
          "apns": [
            {
              "allowedIpTypes": [
                "string"
              ],
              "authentication": {
                "password": "string",
                "type": "string",
                "username": "string"
              },
              "name": "string"
            }
          ],
          "isPrimary": true,
          "slot": "string"
        }
      ]
    }
"""
