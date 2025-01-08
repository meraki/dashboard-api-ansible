#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource devices _wireless _electronic _shelf _label.
  - Update the ESL settings of a device.
extends_documentation_fragment:
  - cisco.meraki.module
module: devices_wireless_electronic_shelf_label
notes:
  - SDK Method used are wireless.Wireless.update_device_wireless_electronic_shelf_label,
  - Paths used are put /devices/{serial}/wireless/electronicShelfLabel,
options:
  channel:
    description: Desired ESL channel for the device, or 'Auto' (case insensitive)
      to use the recommended channel.
    type: str
  enabled:
    description: Turn ESL features on and off for this device.
    type: bool
  serial:
    description: Serial path parameter.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateDeviceWirelessElectronicShelfLabel
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-electronic-shelf-label
    name: Cisco Meraki documentation for wireless updateDeviceWirelessElectronicShelfLabel
short_description: Resource module for devices _wireless _electronic _shelf _label
version_added: 2.20.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.devices_wireless_electronic_shelf_label:
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
    state: present
    channel: '1'
    enabled: true
    serial: string

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "apEslId": 0,
      "channel": "string",
      "enabled": true,
      "hostname": "string",
      "networkId": "string",
      "provider": "string",
      "serial": "string"
    }
"""
