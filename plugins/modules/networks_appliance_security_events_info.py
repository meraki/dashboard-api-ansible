#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_appliance_security_events_info
short_description: Information module for networks _appliance _security _events
description:
  - Get all networks _appliance _security _events.
  - List the security events for a network.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
      - NetworkId path parameter. Network ID.
    type: str
  t0:
    description:
      - >
        T0 query parameter. The beginning of the timespan for the data. Data is gathered
        after the specified t0 value. The maximum lookback period is 365 days from
        today.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 365 days after t0.
    type: str
  timespan:
    description:
      - >
        Timespan query parameter. The timespan for which the information will be fetched.
        If specifying timespan, do not specify parameters t0 and t1. The value must
        be in seconds and be less than or equal to 365 days. The default is 31 days.
    type: float
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 100.
    type: int
  startingAfter:
    description:
      - >
        StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.
    type: str
  endingBefore:
    description:
      - >
        EndingBefore query parameter. A token used by the server to indicate the end
        of the page. Often this is a timestamp or an ID but it is not limited to those.
        This parameter should not be defined by client applications. The link for
        the first, last, prev, or next page in the HTTP Link header should define
        it.
    type: str
  sortOrder:
    description:
      - >
        SortOrder query parameter. Sorted order of security events based on event
        detection time. Order options are 'ascending' or 'descending'. Default is
        ascending order.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance getNetworkApplianceSecurityEvents
    description: Complete reference of the getNetworkApplianceSecurityEvents API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-events
notes:
  - SDK Method used are
    appliance.Appliance.get_network_appliance_security_events,
  - Paths used are
    get /networks/{networkId}/appliance/security/events,
"""

EXAMPLES = r"""
- name: Get all networks _appliance _security _events
  cisco.meraki.networks_appliance_security_events_info:
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
    perPage: 0
    startingAfter: string
    endingBefore: string
    sortOrder: string
    networkId: string
    total_pages: -1
    direction: next
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
      {}
    ]
"""
