#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all organizations _wireless _devices _channel _utilization _by _device.
  - Get average channel utilization for all bands in a network, split by AP.
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
module: organizations_wireless_devices_channel_utilization_by_device_info
notes:
  - SDK Method used are wireless.Wireless.get_organization_wireless_devices_channel_utilization_by_device,
  - Paths used are get /organizations/{organizationId}/wireless/devices/channelUtilization/byDevice,
options:
  endingBefore:
    description:
      - 'EndingBefore query parameter. A token used by the server to indicate the
        end of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.

        '
    type: str
  headers:
    description: Additional headers.
    type: dict
  interval:
    description:
      - 'Interval query parameter. The time interval in seconds for returned data.
        The valid intervals are 300, 600, 3600, 7200, 14400, 21600. The default is
        3600.

        '
    type: int
  networkIds:
    description:
      - NetworkIds query parameter. Filter results by network.
    elements: str
    type: list
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 1000.
    type: int
  serials:
    description:
      - Serials query parameter. Filter results by device.
    elements: str
    type: list
  startingAfter:
    description:
      - 'StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.

        '
    type: str
  t0:
    description:
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 90 days from today.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 90 days after t0.
    type: str
  timespan:
    description:
      - 'Timespan query parameter. The timespan for which the information will be
        fetched. If specifying timespan, do not specify parameters t0 and t1. The
        value must be in seconds and be less than or equal to 90 days. The default
        is 7 days.

        '
    type: float
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getOrganizationWirelessDevicesChannelUtilizationByDevice
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-by-device
    name: Cisco Meraki documentation for wireless getOrganizationWirelessDevicesChannelUtilizationByDevice
short_description: Information module for organizations _wireless _devices _channel
  _utilization _by _device
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all organizations _wireless _devices _channel _utilization _by _device
  cisco.meraki.organizations_wireless_devices_channel_utilization_by_device_info:
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
    networkIds: []
    serials: []
    perPage: 0
    startingAfter: string
    endingBefore: string
    t0: string
    t1: string
    timespan: 0
    interval: 0
    organizationId: string
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
        "byBand": [
          {
            "band": "string",
            "nonWifi": {
              "percentage": 0
            },
            "total": {
              "percentage": 0
            },
            "wifi": {
              "percentage": 0
            }
          }
        ],
        "mac": "string",
        "network": {
          "id": "string"
        },
        "serial": "string"
      }
    ]
"""
