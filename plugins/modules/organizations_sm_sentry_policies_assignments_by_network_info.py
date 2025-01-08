#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all organizations _sm _sentry _policies _assignments _by _network.
  - List the Sentry Policies for an organization ordered in ascending order of priority.
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
module: organizations_sm_sentry_policies_assignments_by_network_info
notes:
  - SDK Method used are sm.Sm.get_organization_sm_sentry_policies_assignments_by_network,
  - Paths used are get /organizations/{organizationId}/sm/sentry/policies/assignments/byNetwork,
options:
  endingBefore:
    description:
      - 'EndingBefore query parameter. A token used by the server to indicate the
        end of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.

        '
    type: str
  headers:
    description: Additional headers.
    type: dict
  networkIds:
    description:
      - NetworkIds query parameter. Optional parameter to filter Sentry Policies by
        Network Id.
    elements: str
    type: list
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 50.
    type: int
  startingAfter:
    description:
      - 'StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.

        '
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getOrganizationSmSentryPoliciesAssignmentsByNetwork
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-sentry-policies-assignments-by-network
    name: Cisco Meraki documentation for sm getOrganizationSmSentryPoliciesAssignmentsByNetwork
short_description: Information module for organizations _sm _sentry _policies _assignments
  _by _network
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all organizations _sm _sentry _policies _assignments _by _network
  cisco.meraki.organizations_sm_sentry_policies_assignments_by_network_info:
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
    meraki_use_iterator_for_get_pages: "{{ meraki_use_iterator_for_get_pages }}"
    meraki_inherit_logging_config: "{{ meraki_inherit_logging_config }}"
    perPage: 0
    startingAfter: string
    endingBefore: string
    networkIds: []
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
        "items": [
          {
            "networkId": "string",
            "policies": [
              {
                "createdAt": "string",
                "groupNumber": "string",
                "groupPolicyId": "string",
                "lastUpdatedAt": "string",
                "networkId": "string",
                "policyId": "string",
                "priority": "string",
                "scope": "string",
                "smNetworkId": "string",
                "tags": [
                  "string"
                ]
              }
            ]
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
    ]
"""
