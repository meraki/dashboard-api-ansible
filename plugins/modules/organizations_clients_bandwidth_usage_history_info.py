#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all organizations _clients _bandwidth _usage _history.
  - 'Return data usage in megabits per second over time for all clients in the given
    organization within a given time range.

    '
extends_documentation_fragment:
  - cisco.meraki.module_info
module: organizations_clients_bandwidth_usage_history_info
notes:
  - SDK Method used are organizations.Organizations.get_organization_clients_bandwidth_usage_history,
  - Paths used are get /organizations/{organizationId}/clients/bandwidthUsageHistory,
options:
  deviceTag:
    description:
      - DeviceTag query parameter. Match result to an exact device tag.
    type: str
  headers:
    description: Additional headers.
    type: dict
  networkTag:
    description:
      - NetworkTag query parameter. Match result to an exact network tag.
    type: str
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  ssidName:
    description:
      - SsidName query parameter. Filter results by ssid name.
    type: str
  t0:
    description:
      - T0 query parameter. The beginning of the timespan for the data.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 186 days after t0.
    type: str
  timespan:
    description:
      - 'Timespan query parameter. The timespan for which the information will be
        fetched. If specifying timespan, do not specify parameters t0 and t1. The
        value must be in seconds and be less than or equal to 186 days. The default
        is 1 day.

        '
    type: float
  usageUplink:
    description:
      - UsageUplink query parameter. Filter results by usage uplink.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getOrganizationClientsBandwidthUsageHistory
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-bandwidth-usage-history
    name: Cisco Meraki documentation for organizations getOrganizationClientsBandwidthUsageHistory
short_description: Information module for organizations _clients _bandwidth _usage
  _history
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all organizations _clients _bandwidth _usage _history
  cisco.meraki.organizations_clients_bandwidth_usage_history_info:
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
    networkTag: string
    deviceTag: string
    ssidName: string
    usageUplink: string
    t0: string
    t1: string
    timespan: 0
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
        "downstream": 0,
        "total": 0,
        "ts": "string",
        "upstream": 0
      }
    ]
"""
