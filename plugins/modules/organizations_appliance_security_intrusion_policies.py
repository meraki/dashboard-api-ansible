#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_appliance_security_intrusion_policies
short_description: Resource module for organizations _appliance _security _intrusion
  _policies
description:
  - Manage operations create, update and delete of the resource organizations _appliance
    _security _intrusion _policies.
  - Create a new intrusion policy for the organization.
  - Delete a single intrusion policy for the organization.
  - Update a single intrusion policy for the organization.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  policy:
    description: Attributes for the intrusion policy.
    suboptions:
      basePolicy:
        description: Base policy metadata.
        suboptions:
          id:
            description: Identifier of the base policy the intrusion rules extend.
            type: str
        type: dict
      description:
        description: Description of the policy.
        type: str
      name:
        description: Display name for the policy.
        type: str
    type: dict
  policyId:
    description: PolicyId path parameter. Policy ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance createOrganizationApplianceSecurityIntrusionPolicy
    description: Complete reference of the createOrganizationApplianceSecurityIntrusionPolicy
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-appliance-security-intrusion-policy
  - name: Cisco Meraki documentation for appliance deleteOrganizationApplianceSecurityIntrusionPolicy
    description: Complete reference of the deleteOrganizationApplianceSecurityIntrusionPolicy
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-appliance-security-intrusion-policy
  - name: Cisco Meraki documentation for appliance updateOrganizationApplianceSecurityIntrusionPolicy
    description: Complete reference of the updateOrganizationApplianceSecurityIntrusionPolicy
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-security-intrusion-policy
notes:
  - SDK Method used are
    appliance.Appliance.create_organization_appliance_security_intrusion_policy,
    appliance.Appliance.delete_organization_appliance_security_intrusion_policy,
    appliance.Appliance.update_organization_appliance_security_intrusion_policy,
  - Paths used are
    post /organizations/{organizationId}/appliance/security/intrusion/policies,
    delete /organizations/{organizationId}/appliance/security/intrusion/policies/{policyId},
    put /organizations/{organizationId}/appliance/security/intrusion/policies/{policyId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_appliance_security_intrusion_policies:
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
    policy:
      basePolicy:
        id: eb508df4-58a2-59c3-a610-500d9a9e4423
      description: Custom strict policy
      name: Custom Strict
- name: Update by id
  cisco.meraki.organizations_appliance_security_intrusion_policies:
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
    policy:
      basePolicy:
        id: eb508df4-58a2-59c3-a610-500d9a9e4423
      description: Updated description
      name: Updated Strict
    policyId: string
- name: Delete by id
  cisco.meraki.organizations_appliance_security_intrusion_policies:
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
    organizationId: string
    policyId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "policyId": {},
      "name": "string",
      "description": {},
      "basePolicy": {
        "id": {}
      },
      "isBasePolicy": true
    }
"""
