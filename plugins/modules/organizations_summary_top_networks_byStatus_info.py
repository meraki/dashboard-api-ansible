#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_summary_top_networks_byStatus_info
short_description: Information module for organizations _summary _top _networks _bystatus
description:
  - Information module for Organizations Summary Top Networks Bystatus Info.
  - Get all organizations _summary _top _networks _bystatus.
  - >
    List the client and status overview information for the networks in an organization.
    Usage is measured in kilobytes and from the last seven days.
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
      - Information module for Organizations Summary Top Networks Bystatus Info.
      - OrganizationId path parameter. Organization ID.
    type: str
  networkTag:
    description:
      - Information module for Organizations Summary Top Networks Bystatus Info.
      - NetworkTag query parameter. Match result to an exact network tag.
    type: str
  deviceTag:
    description:
      - Information module for Organizations Summary Top Networks Bystatus Info.
      - DeviceTag query parameter. Match result to an exact device tag.
    type: str
  quantity:
    description:
      - Information module for Organizations Summary Top Networks Bystatus Info.
      - Quantity query parameter. Set number of desired results to return. Default
        is 10. Maximum is 50.
    type: int
  ssidName:
    description:
      - Information module for Organizations Summary Top Networks Bystatus Info.
      - SsidName query parameter. Filter results by ssid name.
    type: str
  usageUplink:
    description:
      - Information module for Organizations Summary Top Networks Bystatus Info.
      - UsageUplink query parameter. Filter results by usage uplink.
    type: str
  perPage:
    description:
      - Information module for Organizations Summary Top Networks Bystatus Info.
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 5000.
    type: int
  startingAfter:
    description:
      - Information module for Organizations Summary Top Networks Bystatus Info.
      - >
        StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.
    type: str
  endingBefore:
    description:
      - Information module for Organizations Summary Top Networks Bystatus Info.
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
  - name: Cisco Meraki documentation for organizations getOrganizationSummaryTopNetworksByStatus
    description: Complete reference of the getOrganizationSummaryTopNetworksByStatus
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-networks-by-status
notes:
  - SDK Method used are
    organizations.Organizations.get_organization_summary_top_networks_by_status,
  - Paths used are
    get /organizations/{organizationId}/summary/top/networks/byStatus,
"""

EXAMPLES = r"""
- name: Get all organizations _summary _top _networks _bystatus
  cisco.meraki.organizations_summary_top_networks_by_status_info:
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
    networkTag: string
    deviceTag: string
    quantity: 0
    ssidName: string
    usageUplink: string
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
  type: list
  elements: dict
  sample: >
    [
      {
        "networkId": "string",
        "name": "string",
        "url": "string",
        "tags": [
          "string"
        ],
        "clients": {
          "counts": {
            "total": 0
          },
          "usage": {
            "upstream": 0,
            "downstream": 0
          }
        },
        "statuses": {
          "overall": "string",
          "byProductType": [
            {
              "productType": "string",
              "counts": {
                "online": 0,
                "offline": 0,
                "alerting": 0,
                "dormant": 0
              }
            }
          ]
        },
        "devices": {
          "byProductType": [
            {
              "productType": "string",
              "url": "string"
            }
          ]
        },
        "productTypes": [
          "string"
        ]
      }
    ]
"""
