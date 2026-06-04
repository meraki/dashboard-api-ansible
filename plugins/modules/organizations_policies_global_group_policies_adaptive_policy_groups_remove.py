#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_policies_global_group_policies_adaptive_policy_groups_remove
short_description: Resource module for organizations _policies _global _group _policies
  _adaptive _policy _groups _remove
description:
  - Manage operation create of the resource organizations _policies _global _group
    _policies _adaptive _policy _groups _remove.
  - Remove adaptive policy groups from a policy.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  adaptivePolicyGroups:
    description: Adaptive policy groups to remove.
    elements: dict
    suboptions:
      id:
        description: Adaptive policy group ID.
        type: str
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  policy:
    description: Policy to remove adaptive policy groups from.
    suboptions:
      id:
        description: Policy ID.
        type: str
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations removeOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups
    description: Complete reference of the removeOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!remove-organization-policies-global-group-policies-adaptive-policy-groups
notes:
  - SDK Method used are
    organizations.Organizations.remove_organization_policies_global_group_policies_adaptive_policy_groups,
  - Paths used are
    post /organizations/{organizationId}/policies/global/group/policies/adaptivePolicyGroups/remove,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_policies_global_group_policies_adaptive_policy_groups_remove:
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
    adaptivePolicyGroups:
      - id: '1234'
    organizationId: string
    policy:
      id: '123'
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "success": true
    }
"""
