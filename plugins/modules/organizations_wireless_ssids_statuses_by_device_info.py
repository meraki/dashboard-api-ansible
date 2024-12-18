#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: organizations_wireless_ssids_statuses_by_device_info
short_description: Information module for organizations _wireless _ssids _statuses _by _device
description:
- Get all organizations _wireless _ssids _statuses _by _device.
- List status information of all BSSIDs in your organization.
version_added: '2.19.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
    - OrganizationId path parameter. Organization ID.
    type: str
  networkIds:
    description:
    - NetworkIds query parameter. Optional parameter to filter the result set by the included set of network IDs.
    elements: str
    type: list
  serials:
    description:
    - >
      Serials query parameter. A list of serial numbers. The returned devices will be filtered to only include
      these serials.
    elements: str
    type: list
  bssids:
    description:
    - Bssids query parameter. A list of BSSIDs. The returned devices will be filtered to only include these BSSIDs.
    elements: str
    type: list
  hideDisabled:
    description:
    - HideDisabled query parameter. If true, the returned devices will not include disabled SSIDs. (default true).
    type: bool
  perPage:
    description:
    - PerPage query parameter. The number of entries per page returned. Acceptable range is 3 - 500. Default is 100.
    type: int
  startingAfter:
    description:
    - >
      StartingAfter query parameter. A token used by the server to indicate the start of the page. Often this is a
      timestamp or an ID but it is not limited to those. This parameter should not be defined by client
      applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    type: str
  endingBefore:
    description:
    - >
      EndingBefore query parameter. A token used by the server to indicate the end of the page. Often this is a
      timestamp or an ID but it is not limited to those. This parameter should not be defined by client
      applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for wireless getOrganizationWirelessSsidsStatusesByDevice
  description: Complete reference of the getOrganizationWirelessSsidsStatusesByDevice API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-statuses-by-device
notes:
  - SDK Method used are
    wireless.Wireless.get_organization_wireless_ssids_statuses_by_device,

  - Paths used are
    get /organizations/{organizationId}/wireless/ssids/statuses/byDevice,
"""

EXAMPLES = r"""
- name: Get all organizations _wireless _ssids _statuses _by _device
  cisco.meraki.organizations_wireless_ssids_statuses_by_device_info:
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
    networkIds: []
    serials: []
    bssids: []
    hideDisabled: True
    perPage: 0
    startingAfter: string
    endingBefore: string
    organizationId: string
    total_pages: -1
    direction: next
  register: result

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "items": [
        {
          "basicServiceSets": [
            {
              "bssid": "string",
              "radio": {
                "band": "string",
                "channel": 0,
                "channelWidth": 0,
                "index": "string",
                "isBroadcasting": true,
                "power": 0
              },
              "ssid": {
                "advertised": true,
                "enabled": true,
                "name": "string",
                "number": 0
              }
            }
          ],
          "name": "string",
          "network": {
            "id": "string",
            "name": "string"
          },
          "serial": "string"
        }
      ],
      "meta": {
        "counts": {
          "items": {
            "remaining": 0,
            "total": 0
          }
        }
      }
    }
"""
