#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_ssids_profiles_assignments
short_description: Resource module for organizations _wireless _ssids _profiles _assignments
description:
  - Manage operations create and delete of the resource organizations _wireless _ssids
    _profiles _assignments.
  - Assigns an SSID profile to an SSID in the organization.
  - Unassigns the SSID profile assigned to an SSID.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  network:
    description: Network containing the SSID (required if SSID number is used).
    suboptions:
      id:
        description: Network ID.
        type: str
    type: dict
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  profile:
    description: SSID profile to assign.
    suboptions:
      id:
        description: SSID profile ID.
        type: str
    type: dict
  ssid:
    description: SSID to assign the SSID profile to.
    suboptions:
      id:
        description: SSID ID.
        type: str
      number:
        description: SSID number.
        type: int
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless createOrganizationWirelessSsidsProfilesAssignment
    description: Complete reference of the createOrganizationWirelessSsidsProfilesAssignment
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-ssids-profiles-assignment
  - name: Cisco Meraki documentation for wireless deleteOrganizationWirelessSsidsProfilesAssignments
    description: Complete reference of the deleteOrganizationWirelessSsidsProfilesAssignments
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-ssids-profiles-assignments
notes:
  - SDK Method used are
    wireless.Wireless.create_organization_wireless_ssids_profiles_assignment,
    wireless.Wireless.delete_organization_wireless_ssids_profiles_assignments,
  - Paths used are
    post /organizations/{organizationId}/wireless/ssids/profiles/assignments,
    delete /organizations/{organizationId}/wireless/ssids/profiles/assignments,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_wireless_ssids_profiles_assignments:
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
    network:
      id: N_12345
    organizationId: string
    profile:
      id: '123'
    ssid:
      id: '123'
      number: 1
- name: Delete all
  cisco.meraki.organizations_wireless_ssids_profiles_assignments:
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
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "ssid": {
        "id": "string",
        "number": 0,
        "name": "string"
      },
      "profile": {
        "id": "string",
        "name": "string"
      },
      "network": {
        "id": "string",
        "encryptedId": "string",
        "name": "string"
      }
    }
"""
