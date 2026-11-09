#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_switch_ports_statuses_packets_info
short_description: Information module for devices _switch _ports _statuses _packets
description:
  - Get all devices _switch _ports _statuses _packets.
  - Return the packet counters for all the ports of a switch.
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
      - Serial path parameter.
    type: str
  t0:
    description:
      - >
        T0 query parameter. The beginning of the timespan for the data. The value
        is used only to determine the elapsed duration between t0 and the time of
        the request; the API snaps that duration to the nearest preset window (5 minutes,
        15 minutes, 1 hour, or 1 day).
    type: str
  timespan:
    description:
      - >
        Timespan query parameter. The timespan for which the information will be fetched.
        If specifying timespan, do not specify t0. The value must be in seconds and
        be less than or equal to 86400 seconds (1 day). The default is 1 day.
    type: float
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for switch getDeviceSwitchPortsStatusesPackets
    description: Complete reference of the getDeviceSwitchPortsStatusesPackets API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses-packets
notes:
  - SDK Method used are
    switch.Switch.get_device_switch_ports_statuses_packets,
  - Paths used are
    get /devices/{serial}/switch/ports/statuses/packets,
"""

EXAMPLES = r"""
- name: Get all devices _switch _ports _statuses _packets
  cisco.meraki.devices_switch_ports_statuses_packets_info:
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
    t0: string
    timespan: 0
    serial: string
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
        "portId": "string",
        "packets": [
          {
            "desc": "string",
            "total": 0,
            "sent": 0,
            "recv": 0,
            "ratePerSec": {
              "total": 0,
              "sent": 0,
              "recv": 0
            }
          }
        ]
      }
    ]
"""
