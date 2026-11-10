#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_wireless_radio_overrides
short_description: Resource module for devices _wireless _radio _overrides
description:
  - Manage operation update of the resource devices _wireless _radio _overrides. -
    > Update 2.4 GHz, 5 GHz, and 6 GHz radio settings channel, channel width, power,
    and enable/disable that override RF profiles. Read-only fields returned by this
    endpoint, such as 'serial', 'network', and 'radios .band', may be included when
    sending a previously returned object back to this PUT endpoint and will be ignored.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  radios:
    description: Radio overrides. If omitted, existing per-radio override settings
      remain unchanged. If provided, only the radios included in the array are updated;
      the array does not replace the device's full existing set of radio overrides.
      Read-only response fields for each radio, such as 'band', may be included in
      the request body and are ignored.
    elements: dict
    suboptions:
      channel:
        description: Sets a radio override channel. Can be null to use auto channel.
        type: int
      channelWidth:
        description: Set a radio override channel width. Can be null to use auto channel
          width.
        type: int
      enabled:
        description: Enable radio. Setting to false will set tx power to -1.
        type: bool
      index:
        description: Indicates which radio to override.
        type: str
      targetPower:
        description: Set a radio override target power (dBm). Can be null to use auto
          power range.
        type: int
    type: list
  rfProfile:
    description: This device's RF profile. If omitted, the existing RF profile assignment
      remains unchanged.
    suboptions:
      id:
        description: The ID of an RF profile to assign to the device. If this field
          is omitted, the device's existing RF profile assignment will remain unchanged.
          If the value of this parameter is null, the appropriate basic RF profile
          (indoor or outdoor) will be assigned to the device. Assigning an RF profile
          will clear ALL manually configured overrides on the device (channel width,
          channel, power).
        type: str
    type: dict
  serial:
    description: Serial path parameter.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless updateDeviceWirelessRadioOverrides
    description: Complete reference of the updateDeviceWirelessRadioOverrides API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-overrides
notes:
  - SDK Method used are
    wireless.Wireless.update_device_wireless_radio_overrides,
  - Paths used are
    put /devices/{serial}/wireless/radio/overrides,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.devices_wireless_radio_overrides:
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
    state: present
    radios:
      - channel: 149
        channelWidth: 20
        enabled: true
        index: '1'
        targetPower: 15
    rfProfile:
      id: '1234'
    serial: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "serial": "string",
      "network": {
        "id": "string"
      },
      "rfProfile": {
        "id": "string"
      },
      "radios": [
        {
          "enabled": true,
          "index": "string",
          "band": "string",
          "channel": 0,
          "channelWidth": 0,
          "targetPower": 0
        }
      ]
    }
"""
