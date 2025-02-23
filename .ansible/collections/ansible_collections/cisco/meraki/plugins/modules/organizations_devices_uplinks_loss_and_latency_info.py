#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all organizations _devices _uplinks _loss _and _latency.
  - Return the uplink loss and latency for every MX in the organization from at latest
    2 minutes ago.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: organizations_devices_uplinks_loss_and_latency_info
notes:
  - SDK Method used are organizations.Organizations.get_organization_devices_uplinks_loss_and_latency,
  - Paths used are get /organizations/{organizationId}/devices/uplinksLossAndLatency,
options:
  headers:
    description: Additional headers.
    type: dict
  ip:
    description:
      - Ip query parameter. Optional filter for a specific destination IP. Default
        will return all destination IPs.
    type: str
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  t0:
    description:
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 60 days from today.
    type: str
  t1:
    description:
      - 'T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes
        into the past.

        '
    type: str
  timespan:
    description:
      - 'Timespan query parameter. The timespan for which the information will be
        fetched. If specifying timespan, do not specify parameters t0 and t1. The
        value must be in seconds and be less than or equal to 5 minutes. The default
        is 5 minutes.

        '
    type: float
  uplink:
    description:
      - 'Uplink query parameter. Optional filter for a specific WAN uplink. Valid
        uplinks are wan1, wan2, wan3, cellular. Default will return all uplinks.

        '
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getOrganizationDevicesUplinksLossAndLatency
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency
    name: Cisco Meraki documentation for organizations getOrganizationDevicesUplinksLossAndLatency
short_description: Information module for organizations _devices _uplinks _loss _and
  _latency
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all organizations _devices _uplinks _loss _and _latency
  cisco.meraki.organizations_devices_uplinks_loss_and_latency_info:
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
    t0: string
    t1: string
    timespan: 0
    uplink: string
    ip: string
    organizationId: string
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
        "ip": "string",
        "networkId": "string",
        "serial": "string",
        "timeSeries": [
          {
            "latencyMs": 0,
            "lossPercent": 0,
            "ts": "string"
          }
        ],
        "uplink": "string"
      }
    ]
"""
