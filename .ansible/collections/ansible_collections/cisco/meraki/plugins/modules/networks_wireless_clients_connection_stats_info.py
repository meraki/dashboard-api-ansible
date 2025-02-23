#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all networks _wireless _clients _connection _stats.
  - Aggregated connectivity info for a given client on this network. Clients are identified
    by their MAC.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: networks_wireless_clients_connection_stats_info
notes:
  - SDK Method used are wireless.Wireless.get_network_wireless_client_connection_stats,
  - Paths used are get /networks/{networkId}/wireless/clients/{clientId}/connectionStats,
options:
  apTag:
    description:
      - ApTag query parameter. Filter results by AP Tag.
    type: str
  band:
    description:
      - 'Band query parameter. Filter results by band (either ''2.4'', ''5'' or ''6'').
        Note that data prior to February 2020 will not have band information.

        '
    type: str
  clientId:
    description:
      - ClientId path parameter. Client ID.
    type: str
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
      - NetworkId path parameter. Network ID.
    type: str
  ssid:
    description:
      - Ssid query parameter. Filter results by SSID.
    type: int
  t0:
    description:
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 180 days from today.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 7 days after t0.
    type: str
  timespan:
    description:
      - 'Timespan query parameter. The timespan for which the information will be
        fetched. If specifying timespan, do not specify parameters t0 and t1. The
        value must be in seconds and be less than or equal to 7 days.

        '
    type: float
  vlan:
    description:
      - Vlan query parameter. Filter results by VLAN.
    type: int
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getNetworkWirelessClientConnectionStats
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connection-stats
    name: Cisco Meraki documentation for wireless getNetworkWirelessClientConnectionStats
short_description: Information module for networks _wireless _clients _connection
  _stats
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all networks _wireless _clients _connection _stats
  cisco.meraki.networks_wireless_clients_connection_stats_info:
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
    band: string
    ssid: 0
    vlan: 0
    apTag: string
    networkId: string
    clientId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "connectionStats": {
        "assoc": 0,
        "auth": 0,
        "dhcp": 0,
        "success": 0
      },
      "mac": "string"
    }
"""
