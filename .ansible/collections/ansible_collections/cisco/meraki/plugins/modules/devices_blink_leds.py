#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource devices _blink _leds.
  - Blink the LEDs on a device. This endpoint is deprecrated in favor of /devices/{serial}/liveTools/leds/blink.
extends_documentation_fragment:
  - cisco.meraki.module
module: devices_blink_leds
notes:
  - SDK Method used are devices.Devices.blink_device_leds,
  - Paths used are post /devices/{serial}/blinkLeds,
options:
  duration:
    description: The duration in seconds. Must be between 5 and 120. Default is 20
      seconds.
    type: int
  duty:
    description: The duty cycle as the percent active. Must be between 10 and 90.
      Default is 50.
    type: int
  period:
    description: The period in milliseconds. Must be between 100 and 1000. Default
      is 160 milliseconds.
    type: int
  serial:
    description: Serial path parameter.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the blinkDeviceLeds API.
    link: https://developer.cisco.com/meraki/api-v1/#!blink-device-leds
    name: Cisco Meraki documentation for devices blinkDeviceLeds
short_description: Resource module for devices _blink _leds
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.devices_blink_leds:
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
    duration: 20
    duty: 50
    period: 160
    serial: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "duration": 0,
      "duty": 0,
      "period": 0
    }
"""
