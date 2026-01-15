#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_policies_assignments_by_client_info
short_description: Information module for organizations _policies _assignments _by
  _client
description:
  - Information module for Organizations Policies Assignments By Client Info.
  - Get all organizations _policies _assignments _by _client.
  - Get policies for all clients with policies.
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
  - Information module for Organizations Policies Assignments By Client Info.
      - OrganizationId path parameter. Organization ID.
    type: str
  perPage:
    description:
  - Information module for Organizations Policies Assignments By Client Info.
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 50.
    type: int
  startingAfter:
    description:
  - Information module for Organizations Policies Assignments By Client Info.
      - >
        StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.
    type: str
  endingBefore:
    description:
  - Information module for Organizations Policies Assignments By Client Info.
      - >
        EndingBefore query parameter. A token used by the server to indicate the end
        of the page. Often this is a timestamp or an ID but it is not limited to those.
        This parameter should not be defined by client applications. The link for
        the first, last, prev, or next page in the HTTP Link header should define
        it.
    type: str
  t0:
    description:
  - Information module for Organizations Policies Assignments By Client Info.
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 31 days from today.
    type: str
  timespan:
    description:
  - Information module for Organizations Policies Assignments By Client Info.
      - >
        Timespan query parameter. The timespan for which the information will be fetched.
        If specifying timespan, do not specify parameter t0. The value must be in
        seconds and be less than or equal to 31 days. The default is 1 day.
    type: float
  includeUndetectedClients:
    description:
  - Information module for Organizations Policies Assignments By Client Info.
      - >
        IncludeUndetectedClients query parameter. Include provisioned clients that
        have not associated to the network. Default false.
    type: bool
  networkIds:
    description:
  - Information module for Organizations Policies Assignments By Client Info.
      - NetworkIds query parameter. Network Ids (minimum 1, maximum 30).
    elements: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations getOrganizationPoliciesAssignmentsByClient
    description: Complete reference of the getOrganizationPoliciesAssignmentsByClient
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-assignments-by-client
notes:
  - SDK Method used are
    organizations.Organizations.get_organization_policies_assignments_by_client,
  - Paths used are
    get /organizations/{organizationId}/policies/assignments/byClient,
"""

EXAMPLES = r"""
- name: Get all organizations _policies _assignments _by _client
  cisco.meraki.organizations_policies_assignments_by_client_info:
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
    perPage: 0
    startingAfter: string
    endingBefore: string
    t0: string
    timespan: 0
    includeUndetectedClients: True
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
        "name": "string",
        "clientId": "string",
        "mac": "string",
        "networkId": "string",
        "assigned": [
          {
            "name": "string",
            "type": "string",
            "id": "string",
            "limitTo": [
              {
                "appliance": true,
                "ssids": [
                  {
                    "number": 0
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
"""
