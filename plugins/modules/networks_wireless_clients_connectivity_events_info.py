#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_wireless_clients_connectivity_events_info
short_description: Information module for networks _wireless _clients _connectivity
  _events
description:
  - Get all networks _wireless _clients _connectivity _events.
  - List the wireless connectivity events for a client within a network in the timespan.
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
  clientId:
    description:
      - ClientId path parameter. Client ID.
    type: str
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000.
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
        SortOrder query parameter. Sorted order of entries. Order options are 'ascending'
        and 'descending'. Default is 'ascending'.
    type: str
  t0:
    description:
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 31 days from today.
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
  types:
    description:
      - >
        Types query parameter. A list of event types to include. If not specified,
        events of all types will be returned. Valid types are 'assoc', 'disassoc',
        'auth', 'deauth', 'dns', 'dhcp', 'roam', 'connection' and/or 'sticky'.
    elements: str
    type: list
  band:
    description:
      - Band query parameter. Filter results by band. Valid bands are '2.4', '5' or
        '6'.
    type: str
  ssidNumber:
    description:
      - SsidNumber query parameter. Filter results by SSID. If not specified, events
        for all SSIDs will be returned.
    type: int
  includedSeverities:
    description:
      - >
        IncludedSeverities query parameter. A list of severities to include. If not
        specified, events of all severities will be returned. Valid severities are
        'good', 'info', 'warn' and/or 'bad'.
    elements: str
    type: list
  deviceSerial:
    description:
      - DeviceSerial query parameter. Filter results by an AP's serial number.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getNetworkWirelessClientConnectivityEvents
    description: Complete reference of the getNetworkWirelessClientConnectivityEvents
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connectivity-events
notes:
  - SDK Method used are
    wireless.Wireless.get_network_wireless_client_connectivity_events,
  - Paths used are
    get /networks/{networkId}/wireless/clients/{clientId}/connectivityEvents,
"""

EXAMPLES = r"""
- name: Get all networks _wireless _clients _connectivity _events
  cisco.meraki.networks_wireless_clients_connectivity_events_info:
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
    perPage: 0
    startingAfter: string
    endingBefore: string
    sortOrder: string
    t0: string
    t1: string
    timespan: 0
    types: []
    band: string
    ssidNumber: 0
    includedSeverities: []
    deviceSerial: string
    networkId: string
    clientId: string
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
      {
        "occurredAt": "string",
        "band": "string",
        "ssidNumber": 0,
        "type": "string",
        "subtype": "string",
        "severity": "string",
        "durationMs": 0,
        "channel": 0,
        "rssi": 0,
        "eventData": {},
        "deviceSerial": "string",
        "captureId": "string"
      }
    ]
"""
