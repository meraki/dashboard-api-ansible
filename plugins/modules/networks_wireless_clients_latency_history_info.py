#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_wireless_clients_latency_history_info
short_description: Information module for networks _wireless _clients _latency _history
description:
  - Get all networks _wireless _clients _latency _history. - > Return the latency
    history for a client. Clients can be identified by a client key or either the
    MAC or IP depending on whether the network uses Track-by-IP. The latency data
    is from a sample of 2% of packets and is grouped into 4 traffic categories background,
    best effort, video, voice. Within these categories the sampled packet counters
    are bucketed by latency in milliseconds.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
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
  t0:
    description:
      - >
        T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 791 days from today.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 791 days after t0.
    type: str
  timespan:
    description:
      - >
        Timespan query parameter. The timespan for which the information will be fetched.
        If specifying timespan, do not specify parameters t0 and t1. The value must
        be in seconds and be less than or equal to 791 days. The default is 1 day.
    type: float
  resolution:
    description:
      - >
        Resolution query parameter. The time resolution in seconds for returned data.
        The valid resolutions are 86400. The default is 86400.
    type: int
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getNetworkWirelessClientLatencyHistory
    description: Complete reference of the getNetworkWirelessClientLatencyHistory
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-history
notes:
  - SDK Method used are
    wireless.Wireless.get_network_wireless_client_latency_history,
  - Paths used are
    get /networks/{networkId}/wireless/clients/{clientId}/latencyHistory,
"""

EXAMPLES = r"""
- name: Get all networks _wireless _clients _latency _history
  cisco.meraki.networks_wireless_clients_latency_history_info:
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
    networkId: string
    clientId: string
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
        "t0": 0,
        "t1": 0,
        "latencyBinsByCategory": {
          "backgroundTraffic": {
            "0.5": 0,
            "1.0": 0,
            "2.0": 0,
            "4.0": 0,
            "8.0": 0,
            "16.0": 0,
            "32.0": 0,
            "64.0": 0,
            "128.0": 0,
            "256.0": 0,
            "512.0": 0,
            "1024.0": 0,
            "2048.0": 0
          },
          "bestEffortTraffic": {
            "0.5": 0,
            "1.0": 0,
            "2.0": 0,
            "4.0": 0,
            "8.0": 0,
            "16.0": 0,
            "32.0": 0,
            "64.0": 0,
            "128.0": 0,
            "256.0": 0,
            "512.0": 0,
            "1024.0": 0,
            "2048.0": 0
          },
          "videoTraffic": {
            "0.5": 0,
            "1.0": 0,
            "2.0": 0,
            "4.0": 0,
            "8.0": 0,
            "16.0": 0,
            "32.0": 0,
            "64.0": 0,
            "128.0": 0,
            "256.0": 0,
            "512.0": 0,
            "1024.0": 0,
            "2048.0": 0
          },
          "voiceTraffic": {
            "0.5": 0,
            "1.0": 0,
            "2.0": 0,
            "4.0": 0,
            "8.0": 0,
            "16.0": 0,
            "32.0": 0,
            "64.0": 0,
            "128.0": 0,
            "256.0": 0,
            "512.0": 0,
            "1024.0": 0,
            "2048.0": 0
          }
        }
      }
    ]
"""
