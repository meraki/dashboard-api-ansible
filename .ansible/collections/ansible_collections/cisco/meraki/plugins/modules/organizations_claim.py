#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource organizations _claim.
  - 'Claim a list of devices, licenses, and/or orders into an organization inventory.
    When claiming by order, all devices and licenses in the order will be claimed;
    licenses will be added to the organization and devices will be placed in the organization''s
    inventory. This operation can be used up to ten times within a single five minute
    window.

    '
extends_documentation_fragment:
  - cisco.meraki.module
module: organizations_claim
notes:
  - SDK Method used are organizations.Organizations.claim_into_organization,
  - Paths used are post /organizations/{organizationId}/claim,
options:
  licenses:
    description: The licenses that should be claimed.
    elements: dict
    suboptions:
      key:
        description: The key of the license.
        type: str
      mode:
        description: Either 'renew' or 'addDevices'. 'addDevices' will increase the
          license limit, while 'renew' will extend the amount of time until expiration.
          Defaults to 'addDevices'. All licenses must be claimed with the same mode,
          and at most one renewal can be claimed at a time. This parameter is legacy
          and does not apply to organizations with per-device licensing enabled.
        type: str
    type: list
  orders:
    description: The numbers of the orders that should be claimed.
    elements: str
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  serials:
    description: The serials of the devices that should be claimed.
    elements: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the claimIntoOrganization API.
    link: https://developer.cisco.com/meraki/api-v1/#!claim-into-organization
    name: Cisco Meraki documentation for organizations claimIntoOrganization
short_description: Resource module for organizations _claim
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_claim:
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
    licenses:
      - key: Z2XXXXXXXXXX
        mode: addDevices
    orders:
      - 4CXXXXXXX
    organizationId: string
    serials:
      - Q234-ABCD-5678
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "licenses": [
        {
          "key": "string",
          "mode": "string"
        }
      ],
      "orders": [
        "string"
      ],
      "serials": [
        "string"
      ]
    }
"""
