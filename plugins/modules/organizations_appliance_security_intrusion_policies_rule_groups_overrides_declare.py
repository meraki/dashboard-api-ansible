#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_appliance_security_intrusion_policies_rule_groups_overrides_declare
short_description: Resource module for organizations _appliance _security _intrusion
  _policies _rule _groups _overrides _declare
description:
  - Manage operation create of the resource organizations _appliance _security _intrusion
    _policies _rule _groups _overrides _declare.
  - Declare the desired rule group overrides for an intrusion policy.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  items:
    description: Desired overrides state.
    elements: dict
    suboptions:
      group:
        description: Rule group reference.
        suboptions:
          id:
            description: Identifier of the rule group.
            type: str
        type: dict
      security:
        description: Security metadata.
        suboptions:
          level:
            description: Security level override.
            type: int
        type: dict
    type: list
  mode:
    description: Controls how the configuration payload in the request body is applied
      to the resource. This parameter dictates the declarative mode * **`complete`**
      The request body represents the entire desired configuration for this resource.
      Any existing configurations that are not included in the payload will be removed.
      * **`partial` (default)** The request body contains only the configurations
      to be created or modified. Existing configurations that are not specified in
      the payload will be preserved.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  policyId:
    description: PolicyId path parameter. Policy ID.
    type: str
  recursive:
    description: Controls how the configuration payload in the request body applies
      to the rule group hierarchy. When true, the API applies each declared override
      to the rule group itself and its descendants unless the payload explicitly sets
      a descendant override. When false (default), the API applies overrides only
      to the rule groups listed in the payload.
    type: bool
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance declareOrganizationApplianceSecurityIntrusionPolicyRuleGroupsOverrides
    description: Complete reference of the declareOrganizationApplianceSecurityIntrusionPolicyRuleGroupsOverrides
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!declare-organization-appliance-security-intrusion-policy-rule-groups-overrides
notes:
  - SDK Method used are
    appliance.Appliance.declare_organization_appliance_security_intrusion_policy_rule_groups_overrides,
  - Paths used are
    post /organizations/{organizationId}/appliance/security/intrusion/policies/{policyId}/ruleGroups/overrides/declare,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_appliance_security_intrusion_policies_rule_groups_overrides_declare:
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
    items:
      - group:
          id: 9c7645bf-1b92-43d9-b4bb-8b4d5af731e1
        security:
          level: 3
    mode: partial
    organizationId: string
    policyId: string
    recursive: false
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
          "overrideId": "string",
          "policy": {
            "id": "string"
          },
          "group": {
            "id": "string"
          },
          "security": {
            "level": 0
          }
        }
      ]
    }
"""
