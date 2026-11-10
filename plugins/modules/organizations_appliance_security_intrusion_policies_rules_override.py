#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_appliance_security_intrusion_policies_rules_override
short_description: Resource module for organizations _appliance _security _intrusion
  _policies _rules _override
description:
  - Manage operations create and update of the resource organizations _appliance _security
    _intrusion _policies _rules _override.
  - Create a rule override for an intrusion policy.
  - Update a rule override for an intrusion policy.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  override:
    description: Rule override to create.
    suboptions:
      action:
        description: Override action for the rule.
        type: str
    type: dict
  policyId:
    description: PolicyId path parameter. Policy ID.
    type: str
  ruleId:
    description: RuleId path parameter. Rule ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance createOrganizationApplianceSecurityIntrusionPolicyRuleOverride
    description: Complete reference of the createOrganizationApplianceSecurityIntrusionPolicyRuleOverride
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-security-intrusion-policy-rule-override
  - name: Cisco Meraki documentation for appliance updateOrganizationApplianceSecurityIntrusionPolicyRuleOverride
    description: Complete reference of the updateOrganizationApplianceSecurityIntrusionPolicyRuleOverride
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-security-intrusion-policy-rule-override
notes:
  - SDK Method used are
    appliance.Appliance.create_organization_appliance_security_intrusion_policy_rule_override,
    appliance.Appliance.update_organization_appliance_security_intrusion_policy_rule_override,
  - Paths used are
    post /organizations/{organizationId}/appliance/security/intrusion/policies/{policyId}/rules/{ruleId}/override,
    put /organizations/{organizationId}/appliance/security/intrusion/policies/{policyId}/rules/{ruleId}/override,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_appliance_security_intrusion_policies_rules_override:
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
    override:
      action: disable
    policyId: string
    ruleId: string
- name: Update all
  cisco.meraki.organizations_appliance_security_intrusion_policies_rules_override:
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
    override:
      action: disable
    policyId: string
    ruleId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "overrideId": "string",
      "policy": {
        "id": "string"
      },
      "rule": {
        "id": "string"
      },
      "action": {}
    }
"""
