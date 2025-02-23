#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource organizations _licensing _coterm _licenses
    _move.
  - Moves a license to a different organization coterm only .
extends_documentation_fragment:
  - cisco.meraki.module
module: organizations_licensing_coterm_licenses_move
notes:
  - SDK Method used are licensing.Licensing.move_organization_licensing_coterm_licenses,
  - Paths used are post /organizations/{organizationId}/licensing/coterm/licenses/move,
options:
  destination:
    description: Destination data for the license move.
    suboptions:
      mode:
        description: The claim mode of the moved license.
        type: str
      organizationId:
        description: The organization to move the license to.
        type: str
    type: dict
  licenses:
    description: The list of licenses to move.
    elements: dict
    suboptions:
      counts:
        description: The counts to move from the license by model type.
        elements: dict
        suboptions:
          count:
            description: The number of counts to move.
            type: int
          model:
            description: The license model type to move counts of.
            type: str
        type: list
      key:
        description: The license key to move counts from.
        type: str
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the moveOrganizationLicensingCotermLicenses
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!move-organization-licensing-coterm-licenses
    name: Cisco Meraki documentation for licensing moveOrganizationLicensingCotermLicenses
short_description: Resource module for organizations _licensing _coterm _licenses
  _move
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_licensing_coterm_licenses_move:
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
    destination:
      mode: addDevices
      organizationId: '123'
    licenses:
      - counts:
          - count: 5
            model: MR Enterprise
        key: Z2AA-BBBB-CCCC
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "movedLicenses": [
        {
          "claimedAt": "string",
          "counts": [
            {
              "count": 0,
              "model": "string"
            }
          ],
          "duration": 0,
          "editions": [
            {
              "edition": "string",
              "productType": "string"
            }
          ],
          "expired": true,
          "invalidated": true,
          "invalidatedAt": "string",
          "key": "string",
          "mode": "string",
          "organizationId": "string",
          "startedAt": "string"
        }
      ],
      "remainderLicenses": [
        {
          "claimedAt": "string",
          "counts": [
            {
              "count": 0,
              "model": "string"
            }
          ],
          "duration": 0,
          "editions": [
            {
              "edition": "string",
              "productType": "string"
            }
          ],
          "expired": true,
          "invalidated": true,
          "invalidatedAt": "string",
          "key": "string",
          "mode": "string",
          "organizationId": "string",
          "startedAt": "string"
        }
      ]
    }
"""
