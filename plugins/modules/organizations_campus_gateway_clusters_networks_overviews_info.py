#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_campus_gateway_clusters_networks_overviews_info
short_description: Information module for organizations _campus _gateway _clusters
  _networks _overviews
description:
  - Get all organizations _campus _gateway _clusters _networks _overviews.
  - List networks tunneling through Campus Gateway clusters with their AP, ssids and
    client counts.
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
  clusterIds:
    description:
      - >
        ClusterIds query parameter. Optional parameter to filter by MCG cluster IDs.
        This filter uses multiple exact matches.
    elements: str
    type: list
  siteIds:
    description:
      - SiteIds query parameter. Optional parameter to filter by site IDs. This filter
        uses multiple exact matches.
    elements: str
    type: list
  networkIds:
    description:
      - NetworkIds query parameter. Optional parameter to filter networks. This filter
        uses multiple exact matches.
    elements: str
    type: list
  tunnelingSources:
    description:
      - >
        TunnelingSources query parameter. Optional parameter to filter networks by
        tunneling source. 'configured' returns networks explicitly set up to tunnel
        through the campus gateway. 'roaming' returns networks tunneling due to AP
        roaming or disaster recovery. 'roaming' is only effective when 'clusterIds'
        is also provided; without 'clusterIds', the filter defaults to configured-only
        behavior. Defaults to 'configured' if omitted.
    elements: str
    type: list
  search:
    description:
      - >
        Search query parameter. Optional parameter to filter networks by wireless
        network name. This filter uses case-insensitive substring matching.
    type: str
  sortBy:
    description:
      - >
        SortBy query parameter. Optional parameter to sort results. Default is 'name'.
        Use 'siteName' to sort by site name.
    type: str
  sortOrder:
    description:
      - SortOrder query parameter. Optional parameter to specify sort direction. Default
        is 'asc'.
    type: str
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 100.
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
  - name: Cisco Meraki documentation for campusGateway getOrganizationCampusGatewayClustersNetworksOverviews
    description: Complete reference of the getOrganizationCampusGatewayClustersNetworksOverviews
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clusters-networks-overviews
notes:
  - SDK Method used are
    campus_gateway.CampusGateway.get_organization_campus_gateway_clusters_networks_overviews,
  - Paths used are
    get /organizations/{organizationId}/campusGateway/clusters/networks/overviews,
"""

EXAMPLES = r"""
- name: Get all organizations _campus _gateway _clusters _networks _overviews
  cisco.meraki.organizations_campus_gateway_clusters_networks_overviews_info:
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
    clusterIds: []
    siteIds: []
    networkIds: []
    tunnelingSources: []
    search: string
    sortBy: string
    sortOrder: string
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
          "networkId": "string",
          "name": "string",
          "tunneling": {
            "source": "string"
          },
          "site": {
            "id": "string",
            "name": "string",
            "url": "string"
          },
          "url": "string",
          "counts": {
            "connections": {
              "total": 0
            },
            "clients": {
              "total": 0
            },
            "ssids": {
              "total": 0
            }
          },
          "cluster": {
            "id": "string",
            "name": "string"
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
