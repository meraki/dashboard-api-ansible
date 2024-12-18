#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: organizations_assurance_alerts_overview_by_network_info
short_description: Information module for organizations _assurance _alerts _overview _by _network
description:
- Get all organizations _assurance _alerts _overview _by _network.
- Return a Summary of Alerts grouped by network and severity.
version_added: '2.20.0'
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
  perPage:
    description:
    - PerPage query parameter. The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
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
  sortOrder:
    description:
    - >
      SortOrder query parameter. Sorted order of entries. Order options are 'ascending' and 'descending'. Default
      is 'ascending'.
    type: str
  networkId:
    description:
    - NetworkId query parameter. Optional parameter to filter alerts overview by network id.
    type: str
  severity:
    description:
    - Severity query parameter. Optional parameter to filter alerts overview by severity type.
    type: str
  types:
    description:
    - Types query parameter. Optional parameter to filter by alert type.
    elements: str
    type: list
  tsStart:
    description:
    - TsStart query parameter. Optional parameter to filter by starting timestamp.
    type: str
  tsEnd:
    description:
    - TsEnd query parameter. Optional parameter to filter by end timestamp.
    type: str
  category:
    description:
    - Category query parameter. Optional parameter to filter by category.
    type: str
  serials:
    description:
    - Serials query parameter. Optional parameter to filter by primary device serial.
    elements: str
    type: list
  deviceTypes:
    description:
    - DeviceTypes query parameter. Optional parameter to filter by device types.
    elements: str
    type: list
  deviceTags:
    description:
    - DeviceTags query parameter. Optional parameter to filter by device tags.
    elements: str
    type: list
  active:
    description:
    - Active query parameter. Optional parameter to filter by active alerts defaults to true.
    type: bool
  dismissed:
    description:
    - Dismissed query parameter. Optional parameter to filter by dismissed alerts defaults to false.
    type: bool
  resolved:
    description:
    - Resolved query parameter. Optional parameter to filter by resolved alerts defaults to false.
    type: bool
  suppressAlertsForOfflineNodes:
    description:
    - >
      SuppressAlertsForOfflineNodes query parameter. When set to true the api will only return connectivity alerts
      for a given device if that device is in an offline state. This only applies to devices. This is ignored when
      resolved is true. Example If a Switch has a VLan Mismatch and is Unreachable. Only the Unreachable alert
      will be returned. Defaults to false.
    type: bool
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for organizations getOrganizationAssuranceAlertsOverviewByNetwork
  description: Complete reference of the getOrganizationAssuranceAlertsOverviewByNetwork API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-by-network
notes:
  - SDK Method used are
    organizations.Organizations.get_organization_assurance_alerts_overview_by_network,

  - Paths used are
    get /organizations/{organizationId}/assurance/alerts/overview/byNetwork,
"""

EXAMPLES = r"""
- name: Get all organizations _assurance _alerts _overview _by _network
  cisco.meraki.organizations_assurance_alerts_overview_by_network_info:
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
    perPage: 0
    startingAfter: string
    endingBefore: string
    sortOrder: string
    networkId: string
    severity: string
    types: []
    tsStart: string
    tsEnd: string
    category: string
    serials: []
    deviceTypes: []
    deviceTags: []
    active: True
    dismissed: True
    resolved: True
    suppressAlertsForOfflineNodes: True
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
          "alertCount": 0,
          "networkId": "string",
          "networkName": "string",
          "severityCounts": [
            {
              "count": 0,
              "type": "string"
            }
          ]
        }
      ],
      "meta": {
        "counts": {
          "items": 0
        }
      }
    }
"""