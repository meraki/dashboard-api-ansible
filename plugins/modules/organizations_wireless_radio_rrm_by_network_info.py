#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_radio_rrm_by_network_info
short_description: Information module for organizations _wireless _radio _rrm _by _network
description:
  - Get all organizations _wireless _radio _rrm _by _network.
  - List the AutoRF settings of an organization by network.
version_added: '1.0.0'
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
      - NetworkIds query parameter. Optional parameter to filter results by network.
    elements: str
    type: list
  startingAfter:
    description:
      - StartingAfter query parameter. Retrieving items after this network ID.
    type: str
  endingBefore:
    description:
      - EndingBefore query parameter. Retrieving items before this network ID.
    type: str
  perPage:
    description:
      - PerPage query parameter. Number of items per page.
    type: int
  sortOrder:
    description:
      - SortOrder query parameter. The sort order of items.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getOrganizationWirelessRadioRrmByNetwork
    description: Complete reference of the getOrganizationWirelessRadioRrmByNetwork API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-radio-rrm-by-network
notes:
  - SDK Method used are
    wireless.Wireless.get_organization_wireless_radio_rrm_by_network,

  - Paths used are
    get /organizations/{organizationId}/wireless/radio/rrm/byNetwork,
"""

EXAMPLES = r"""
- name: Get all organizations _wireless _radio _rrm _by _network
  cisco.meraki.organizations_wireless_radio_rrm_by_network_info:
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
    networkIds: []
    startingAfter: string
    endingBefore: string
    perPage: 0
    sortOrder: string
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
          "networkId": "string",
          "name": "string",
          "timeZone": "string",
          "busyHour": {
            "schedule": {
              "mode": "string",
              "automatic": {
                "start": "string",
                "end": "string"
              },
              "manual": {
                "start": "string",
                "end": "string"
              }
            },
            "minimizeChanges": {
              "enabled": true
            }
          },
          "channel": {
            "avoidance": {
              "enabled": true
            }
          },
          "fra": {
            "enabled": true
          },
          "ai": {
            "enabled": true,
            "lastEnabledAt": "string"
          }
        }
      ],
      "meta": {
        "counts": {
          "items": {
            "total": 0,
            "remaining": 0
          }
        }
      }
    }
"""
