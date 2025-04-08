#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_appliance_dns_local_profiles_assignments_info
short_description: Information module for organizations _appliance _dns _local _profiles _assignments
description:
  - Get all organizations _appliance _dns _local _profiles _assignments.
  - Fetch the local DNS profile assignments in the organization.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  profileIds:
    description:
      - ProfileIds query parameter. Optional parameter to filter the results by profile IDs.
    elements: str
    type: list
  networkIds:
    description:
      - NetworkIds query parameter. Optional parameter to filter the results by network IDs.
    elements: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance getOrganizationApplianceDnsLocalProfilesAssignments
    description: Complete reference of the getOrganizationApplianceDnsLocalProfilesAssignments API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-dns-local-profiles-assignments
notes:
  - SDK Method used are
    appliance.Appliance.get_organization_appliance_dns_local_profiles_assignments,
  - Paths used are
    get /organizations/{organizationId}/appliance/dns/local/profiles/assignments,
"""

EXAMPLES = r"""
- name: Get all organizations _appliance _dns _local _profiles _assignments
  cisco.meraki.organizations_appliance_dns_local_profiles_assignments_info:
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
    profileIds: []
    networkIds: []
    organizationId: string
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
          "assignmentId": "string",
          "network": {
            "id": "string"
          },
          "profile": {
            "id": "string"
          }
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
"""
