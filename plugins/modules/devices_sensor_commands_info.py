#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_sensor_commands_info
short_description: Information module for devices _sensor _commands
description:
  - Get all devices _sensor _commands.
  - Get devices _sensor _commands by id.
  - Returns a historical log of all commands.
  - Returns information about the command's execution, including the status.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  serial:
    description:
      - Serial path parameter.
    type: str
  operations:
    description:
      - >
        Operations query parameter. Optional parameter to filter commands by operation. Allowed values are disableDownstreamPower, enableDownstreamPower,
        cycleDownstreamPower, and refreshData.
    elements: str
    type: list
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
    type: int
  startingAfter:
    description:
      - >
        StartingAfter query parameter. A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it
        is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page
        in the HTTP Link header should define it.
    type: str
  endingBefore:
    description:
      - >
        EndingBefore query parameter. A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is
        not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in
        the HTTP Link header should define it.
    type: str
  sortOrder:
    description:
      - >
        SortOrder query parameter. Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'descending'.
    type: str
  t0:
    description:
      - T0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum of 30 days after t0.
    type: str
  timespan:
    description:
      - >
        Timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0
        and t1. The value must be in seconds and be less than or equal to 30 days. The default is 30 days.
    type: float
  commandId:
    description:
      - CommandId path parameter. Command ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for sensor getDeviceSensorCommand
    description: Complete reference of the getDeviceSensorCommand API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-command
  - name: Cisco Meraki documentation for sensor getDeviceSensorCommands
    description: Complete reference of the getDeviceSensorCommands API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-commands
notes:
  - SDK Method used are
    sensor.Sensor.get_device_sensor_command,
    sensor.Sensor.get_device_sensor_commands,
  - Paths used are
    get /devices/{serial}/sensor/commands,
    get /devices/{serial}/sensor/commands/{commandId},
"""

EXAMPLES = r"""
- name: Get all devices _sensor _commands
  cisco.meraki.devices_sensor_commands_info:
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
    operations: []
    perPage: 0
    startingAfter: string
    endingBefore: string
    sortOrder: string
    t0: string
    t1: string
    timespan: 0
    serial: string
    total_pages: -1
    direction: next
  register: result
- name: Get devices _sensor _commands by id
  cisco.meraki.devices_sensor_commands_info:
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
    commandId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "commandId": "string",
      "completedAt": "string",
      "createdAt": "string",
      "createdBy": {
        "adminId": "string",
        "email": "string",
        "name": "string"
      },
      "errors": [
        "string"
      ],
      "operation": "string",
      "status": "string"
    }
"""
