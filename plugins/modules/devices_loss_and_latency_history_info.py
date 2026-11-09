#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_loss_and_latency_history_info
short_description: Information module for devices _loss _and _latency _history
description:
  - Get all devices _loss _and _latency _history. - > Get the uplink loss percentage
    and latency in milliseconds, and goodput in kilobits per second for MX, MG and
    Z devices.
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
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 60 days from today.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 31 days after t0.
    type: str
  timespan:
    description:
      - >
        Timespan query parameter. The timespan for which the information will be fetched.
        If specifying timespan, do not specify parameters t0 and t1. The value must
        be in seconds and be less than or equal to 31 days. The default is 1 day.
    type: float
  resolution:
    description:
      - >
        Resolution query parameter. The time resolution in seconds for returned data.
        The valid resolutions are 60, 600, 3600, 86400. The default is 60.
    type: int
  uplink:
    description:
      - >
        Uplink query parameter. The WAN uplink used to obtain the requested stats.
        Valid uplinks are wan1, wan2, wan3, cellular, wan4. The default is wan1.
    type: str
  ip:
    description:
      - Ip query parameter. The destination IP used to obtain the requested stats.
        This is required.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for devices getDeviceLossAndLatencyHistory
    description: Complete reference of the getDeviceLossAndLatencyHistory API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-loss-and-latency-history
notes:
  - SDK Method used are
    devices.Devices.get_device_loss_and_latency_history,
  - Paths used are
    get /devices/{serial}/lossAndLatencyHistory,
"""

EXAMPLES = r"""
- name: Get all devices _loss _and _latency _history
  cisco.meraki.devices_loss_and_latency_history_info:
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
    t1: string
    timespan: 0
    resolution: 0
    uplink: string
    ip: string
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
        "startTime": "string",
        "endTime": "string",
        "lossPercent": 0,
        "latencyMs": 0,
        "goodput": 0,
        "jitter": 0
      }
    ]
"""
