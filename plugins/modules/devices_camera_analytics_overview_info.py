#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_camera_analytics_overview_info
short_description: Information module for devices _camera _analytics _overview
description:
  - Get all devices _camera _analytics _overview.
  - Returns an overview of aggregate analytics data for a timespan.
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
        T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 365 days from today.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 7 days after t0.
    type: str
  timespan:
    description:
      - >
        Timespan query parameter. The timespan for which the information will be fetched.
        If specifying timespan, do not specify parameters t0 and t1. The value must
        be in seconds and be less than or equal to 7 days. The default is 1 hour.
    type: float
  objectType:
    description:
      - >
        ObjectType query parameter. Optional The object type for which analytics will
        be retrieved. The default object type is person. The available types are person,
        vehicle.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for camera getDeviceCameraAnalyticsOverview
    description: Complete reference of the getDeviceCameraAnalyticsOverview API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-overview
notes:
  - SDK Method used are
    camera.Camera.get_device_camera_analytics_overview,
  - Paths used are
    get /devices/{serial}/camera/analytics/overview,
"""

EXAMPLES = r"""
- name: Get all devices _camera _analytics _overview
  cisco.meraki.devices_camera_analytics_overview_info:
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
    objectType: string
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
        "startTs": "string",
        "endTs": "string",
        "zoneId": 0,
        "entrances": 0,
        "averageCount": 0
      }
    ]
"""
