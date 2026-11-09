#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_devices_certificates_info
short_description: Information module for organizations _devices _certificates
description:
  - Get all organizations _devices _certificates.
  - List device certificates for the organization. Optionally filter by device serial
    numbers and feature types.
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
  serials:
    description:
      - Serials query parameter. Device serial numbers to filter by (exact match;
        duplicates are ignored).
    elements: str
    type: list
  featureTypes:
    description:
      - >
        FeatureTypes query parameter. Feature types these device certificates serve
        (exact match; e.g., radsec, openroaming, zigbee).
    elements: str
    type: list
  sortBy:
    description:
      - SortBy query parameter. Field to sort by (default authorityId).
    type: str
  direction:
    description:
      - Direction query parameter. Sort direction (default asc).
    type: str
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 100. Default is 50.
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
  - name: Cisco Meraki documentation for organizations getOrganizationDevicesCertificates
    description: Complete reference of the getOrganizationDevicesCertificates API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-certificates
notes:
  - SDK Method used are
    organizations.Organizations.get_organization_devices_certificates,
  - Paths used are
    get /organizations/{organizationId}/devices/certificates,
"""

EXAMPLES = r"""
- name: Get all organizations _devices _certificates
  cisco.meraki.organizations_devices_certificates_info:
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
    serials: []
    featureTypes: []
    sortBy: string
    direction: string
    perPage: 0
    startingAfter: string
    endingBefore: string
    organizationId: string
    total_pages: -1
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
          "serial": "string",
          "feature": {
            "type": "string"
          },
          "authority": {
            "id": "string"
          },
          "contents": "string",
          "status": "string",
          "expiresAt": "string",
          "issuedAt": "string",
          "certificateSerial": "string"
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
