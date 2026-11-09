#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_appliance_security_intrusion_rule_groups_overviews_info
short_description: Information module for organizations _appliance _security _intrusion
  _rule _groups _overviews
description:
  - Get all organizations _appliance _security _intrusion _rule _groups _overviews.
  - List counts for the child rule groups and rules for each rule group in a security
    policy.
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
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 500. Default is 50.
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
  policyIds:
    description:
      - PolicyIds query parameter. Collection of base or intrusion policy identifiers
        to filter results by.
    elements: str
    type: list
  parentRuleGroupIds:
    description:
      - >
        ParentRuleGroupIds query parameter. Filter results to rule groups whose parent
        matches any of the provided identifiers.
    elements: str
    type: list
  search:
    description:
      - Search query parameter. Case-insensitive text filter applied to rule group
        name and description.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance getOrganizationApplianceSecurityIntrusionRuleGroupsOverviews
    description: Complete reference of the getOrganizationApplianceSecurityIntrusionRuleGroupsOverviews
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-intrusion-rule-groups-overviews
notes:
  - SDK Method used are
    appliance.Appliance.get_organization_appliance_security_intrusion_rule_groups_overviews,
  - Paths used are
    get /organizations/{organizationId}/appliance/security/intrusion/ruleGroups/overviews,
"""

EXAMPLES = r"""
- name: Get all organizations _appliance _security _intrusion _rule _groups _overviews
  cisco.meraki.organizations_appliance_security_intrusion_rule_groups_overviews_info:
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
    policyIds: []
    parentRuleGroupIds: []
    search: string
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
          "ruleGroupId": "string",
          "policy": {
            "id": "string"
          },
          "counts": {
            "ruleGroups": {
              "total": 0,
              "bySecurityLevel": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "unknown": 0
              }
            },
            "rules": {
              "total": 0,
              "byAction": {
                "alert": 0,
                "block": 0,
                "other": 0
              }
            }
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
