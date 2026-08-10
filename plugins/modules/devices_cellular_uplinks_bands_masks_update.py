#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_cellular_uplinks_bands_masks_update
short_description: Resource module for devices _cellular _uplinks _bands _masks _update
description:
  - Manage operation create of the resource devices _cellular _uplinks _bands _masks
    _update.
  - Update the cellular band masks for a device.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  masked:
    description: Required parameter for the band identifiers to mask for the given
      SIM slot and signal type. For LTE use bands identifiers like '30', for 5G use
      band identifiers like 'n30', or use 'all' to mask all bands for that signal
      type. Maximum 256 bands.
    elements: str
    type: list
  serial:
    description: Serial path parameter.
    type: str
  slot:
    description: Required parameter for the SIM slot to update the cellular band mask
      for.
    type: str
  type:
    description: Required parameter for the signal type to update the cellular band
      mask for.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for devices createDeviceCellularUplinksBandsMasksUpdate
    description: Complete reference of the createDeviceCellularUplinksBandsMasksUpdate
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-device-cellular-uplinks-bands-masks-update
notes:
  - SDK Method used are
    devices.Devices.create_device_cellular_uplinks_bands_masks_update,
  - Paths used are
    post /devices/{serial}/cellular/uplinks/bands/masks/update,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.devices_cellular_uplinks_bands_masks_update:
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
    masked:
      - '2'
      - '12'
      - '30'
    serial: string
    slot: sim1
    type: LTE
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "bySlot": [
        {
          "slot": "string",
          "bySignalType": [
            {
              "type": "string",
              "masked": [
                "string"
              ],
              "enabled": [
                "string"
              ],
              "supported": [
                "string"
              ]
            }
          ]
        }
      ]
    }
"""
