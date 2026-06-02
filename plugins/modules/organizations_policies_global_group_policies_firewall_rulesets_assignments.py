#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_policies_global_group_policies_firewall_rulesets_assignments
short_description: Resource module for organizations _policies _global _group _policies
  _firewall _rulesets _assignments
description:
  - Manage operations create, update and delete of the resource organizations _policies
    _global _group _policies _firewall _rulesets _assignments.
  - Create an Organization-Wide Policy Ruleset Assignment.
  - Delete an Organization-Wide Policy Ruleset Assignment.
  - Update an Organization-Wide Policy Ruleset Assignment.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  assignmentId:
    description: AssignmentId path parameter. Assignment ID.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  policyId:
    description: ID of the policy to assign the ruleset to.
    type: str
  priority:
    description: Priority of the ruleset assignment (lower numbers = higher priority).
    type: int
  rulesetId:
    description: ID of the ruleset to assign.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations createOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment
    description: Complete reference of the createOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-group-policies-firewall-rulesets-assignment
  - name: Cisco Meraki documentation for organizations deleteOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment
    description: Complete reference of the deleteOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-group-policies-firewall-rulesets-assignment
  - name: Cisco Meraki documentation for organizations updateOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment
    description: Complete reference of the updateOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-group-policies-firewall-rulesets-assignment
notes:
  - SDK Method used are
    organizations.Organizations.create_organization_policies_global_group_policies_firewall_rulesets_assignment,
    organizations.Organizations.delete_organization_policies_global_group_policies_firewall_rulesets_assignment,
    organizations.Organizations.update_organization_policies_global_group_policies_firewall_rulesets_assignment,
  - Paths used are
    post /organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments,
    delete /organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments/{assignmentId},
    put /organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments/{assignmentId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_policies_global_group_policies_firewall_rulesets_assignments:
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
    state: present
    organizationId: string
    policyId: '789'
    priority: 0
    rulesetId: '456'
- name: Update by id
  cisco.meraki.organizations_policies_global_group_policies_firewall_rulesets_assignments:
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
    state: present
    assignmentId: string
    organizationId: string
    policyId: '789'
    priority: 0
    rulesetId: '456'
- name: Delete by id
  cisco.meraki.organizations_policies_global_group_policies_firewall_rulesets_assignments:
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
    state: absent
    assignmentId: string
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "assignmentId": "string",
      "rulesetId": "string",
      "policyId": "string",
      "priority": 0,
      "createdAt": "string",
      "lastUpdatedAt": "string"
    }
"""
