#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource organizations _networks _combine.
  - Combine multiple networks into a single network.
extends_documentation_fragment:
  - cisco.meraki.module
module: organizations_networks_combine
notes:
  - SDK Method used are organizations.Organizations.combine_organization_networks,
  - Paths used are post /organizations/{organizationId}/networks/combine,
options:
  enrollmentString:
    description: A unique identifier which can be used for device enrollment or easy
      access through the Meraki SM Registration page or the Self Service Portal. Please
      note that changing this field may cause existing bookmarks to break. All networks
      that are part of this combined network will have their enrollment string appended
      by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.
    type: str
  name:
    description: The name of the combined network.
    type: str
  networkIds:
    description: A list of the network IDs that will be combined. If an ID of a combined
      network is included in this list, the other networks in the list will be grouped
      into that network.
    elements: str
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the combineOrganizationNetworks API.
    link: https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks
    name: Cisco Meraki documentation for organizations combineOrganizationNetworks
short_description: Resource module for organizations _networks _combine
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_networks_combine:
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
    enrollmentString: my-enrollment-string
    name: Long Island Office
    networkIds:
      - N_1234
      - N_5678
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "resultingNetwork": {
        "enrollmentString": "string",
        "id": "string",
        "isBoundToConfigTemplate": true,
        "name": "string",
        "notes": "string",
        "organizationId": "string",
        "productTypes": [
          "string"
        ],
        "tags": [
          "string"
        ],
        "timeZone": "string",
        "url": "string"
      }
    }
"""
