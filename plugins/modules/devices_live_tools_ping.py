#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: devices_live_tools_ping
short_description: Resource module for devices _livetools _ping
description:
- Manage operation create of the resource devices _livetools _ping.
- Enqueue a job to ping a target host from the device.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  count:
    description: Count parameter to pass to ping. 1..5, default 5.
    type: int
  serial:
    description: Serial path parameter.
    type: str
  target:
    description: FQDN, IPv4 or IPv6 address.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for devices createDeviceLiveToolsPing
  description: Complete reference of the createDeviceLiveToolsPing API.
  link: https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ping
notes:
  - SDK Method used are
    devices.Devices.create_device_live_tools_ping,

  - Paths used are
    post /devices/{serial}/liveTools/ping,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.devices_live_tools_ping:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    count: 2
    serial: string
    target: 75.75.75.75

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "pingId": "string",
      "url": "string",
      "request": {
        "serial": "string",
        "target": "string",
        "count": 0
      },
      "status": "string"
    }
"""
