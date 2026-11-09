#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_assurance_wireless_experience_successful_connections_by_network_info
short_description: Information module for organizations _assurance _wireless _experience
  _successful _connections _by _network
description:
  - Get all organizations _assurance _wireless _experience _successful _connections
    _by _network. - > Returns connection and client counts aggregated by network for
    the requested time window. This operation returns one aggregate per network for
    the requested window. Use the byInterval operation for time buckets. Use either
    timespan or t0/t1 to set the window. The default is 2 hours, the minimum timespan
    is 15 minutes, and the maximum lookback is 14 days. Results use cursor pagination
    by network ID. The perPage value is between 3 and 100, with a default of 100 networks.
    Breakdowns return up to 5 contributors, 10 sub-contributors per contributor, and
    100 reasons per sub-contributor.
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
      - NetworkIds query parameter. Filter results by network.
    elements: str
    type: list
  serials:
    description:
      - Serials query parameter. Filter results by device serial.
    elements: str
    type: list
  ssidNumbers:
    description:
      - SsidNumbers query parameter. Filter results by SSID number. Valid values are
        0-14.
    elements: int
    type: list
  bands:
    description:
      - Bands query parameter. Filter results by wireless band in GHz (2.4, 5, or
        6).
    elements: str
    type: list
  t0:
    description:
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 14 days from today.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 14 days after t0.
    type: str
  timespan:
    description:
      - >
        Timespan query parameter. The timespan for which the information will be fetched.
        If specifying timespan, do not specify parameters t0 and t1. The value must
        be in seconds and be greater than or equal to 15 minutes and be less than
        or equal to 14 days. The default is 2 hours.
    type: float
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 100. Default is 100.
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
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getOrganizationAssuranceWirelessExperienceSuccessfulConnectionsByNetwork
    description: Complete reference of the getOrganizationAssuranceWirelessExperienceSuccessfulConnectionsByNetwork
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connections-by-network
notes:
  - SDK Method used are
    wireless.Wireless.get_organization_assurance_wireless_experience_successful_connections_by_network,
  - Paths used are
    get /organizations/{organizationId}/assurance/wireless/experience/successfulConnections/byNetwork,
"""

EXAMPLES = r"""
- name: Get all organizations _assurance _wireless _experience _successful _connections
    _by _network
  cisco.meraki.organizations_assurance_wireless_experience_successful_connections_by_network_info:
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
    serials: []
    ssidNumbers: []
    bands: []
    t0: string
    t1: string
    timespan: 0
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
      "meta": {
        "counts": {
          "items": {
            "total": 0,
            "remaining": 0
          }
        }
      },
      "items": [
        {
          "network": {
            "id": "string",
            "name": "string",
            "url": {},
            "type": "string"
          },
          "successes": {
            "count": 0
          },
          "failures": {
            "count": 0
          },
          "clients": {
            "total": 0,
            "failing": 0
          },
          "byContributor": [
            {
              "name": "string",
              "successes": {
                "count": 0
              },
              "failures": {
                "count": 0
              },
              "failureContribution": {
                "percent": 0
              },
              "clientFailureContribution": {
                "percent": 0
              },
              "clients": {
                "failing": 0,
                "total": 0
              },
              "bySubContributor": [
                {
                  "name": "string",
                  "failures": {
                    "count": 0
                  },
                  "failureContribution": {
                    "percent": 0
                  },
                  "clients": {
                    "failing": 0
                  },
                  "clientFailureContribution": {
                    "percent": 0
                  },
                  "byReason": [
                    {
                      "type": {},
                      "code": {},
                      "reason": {},
                      "count": 0
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
"""
