#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all networks _wireless _channel _utilization _history.
  - Return AP channel utilization over time for a device or network client.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: networks_wireless_channel_utilization_history_info
notes:
  - SDK Method used are wireless.Wireless.get_network_wireless_channel_utilization_history,
  - Paths used are get /networks/{networkId}/wireless/channelUtilizationHistory,
options:
  apTag:
    description:
      - 'ApTag query parameter. Filter results by AP tag to return AP channel utilization
        metrics for devices labeled with the given tag; either clientId or deviceSerial
        must be jointly specified.

        '
    type: str
  autoResolution:
    description:
      - 'AutoResolution query parameter. Automatically select a data resolution based
        on the given timespan; this overrides the value specified by the ''resolution''
        parameter. The default setting is false.

        '
    type: bool
  band:
    description:
      - Band query parameter. Filter results by band (either '2.4', '5' or '6').
    type: str
  clientId:
    description:
      - 'ClientId query parameter. Filter results by network client to return per-device,
        per-band AP channel utilization metrics inner joined by the queried client''s
        connection history.

        '
    type: str
  deviceSerial:
    description:
      - 'DeviceSerial query parameter. Filter results by device to return AP channel
        utilization metrics for the queried device; either band or clientId must be
        jointly specified.

        '
    type: str
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
      - NetworkId path parameter. Network ID.
    type: str
  resolution:
    description:
      - 'Resolution query parameter. The time resolution in seconds for returned data.
        The valid resolutions are 600, 1200, 3600, 14400, 86400. The default is 86400.

        '
    type: int
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
      - 'Timespan query parameter. The timespan for which the information will be
        fetched. If specifying timespan, do not specify parameters t0 and t1. The
        value must be in seconds and be less than or equal to 31 days. The default
        is 7 days.

        '
    type: float
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getNetworkWirelessChannelUtilizationHistory
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-channel-utilization-history
    name: Cisco Meraki documentation for wireless getNetworkWirelessChannelUtilizationHistory
short_description: Information module for networks _wireless _channel _utilization
  _history
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all networks _wireless _channel _utilization _history
  cisco.meraki.networks_wireless_channel_utilization_history_info:
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
    resolution: 0
    autoResolution: true
    clientId: string
    deviceSerial: string
    apTag: string
    band: string
    networkId: string
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
        "endTs": "string",
        "startTs": "string",
        "utilization80211": 0,
        "utilizationNon80211": 0,
        "utilizationTotal": 0
      }
    ]
"""
