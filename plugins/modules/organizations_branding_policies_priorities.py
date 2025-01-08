#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource organizations _branding _policies _priorities.
  - Update the priority ordering of an organization's branding policies.
extends_documentation_fragment:
  - cisco.meraki.module
module: organizations_branding_policies_priorities
notes:
  - SDK Method used are organizations.Organizations.update_organization_branding_policies_priorities,
  - Paths used are put /organizations/{organizationId}/brandingPolicies/priorities,
options:
  brandingPolicyIds:
    description: An ordered list of branding policy IDs that determines the priority
      order of how to apply the policies.
    elements: str
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateOrganizationBrandingPoliciesPriorities
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities
    name: Cisco Meraki documentation for organizations updateOrganizationBrandingPoliciesPriorities
short_description: Resource module for organizations _branding _policies _priorities
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.organizations_branding_policies_priorities:
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
    state: present
    brandingPolicyIds:
    - '123'
    - '456'
    - '789'
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    [
      "string"
    ]
"""
