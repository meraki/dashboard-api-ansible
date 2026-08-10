#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_devices_cellular_data_profiles_assignments_batch_create
short_description: Resource module for organizations _devices _cellular _data _profiles
  _assignments _batch _create
description:
  - Manage operation create of the resource organizations _devices _cellular _data
    _profiles _assignments _batch _create. - > Assign devices to a Cellular Data Management
    Profile in batch. Creates up to 100 device-to-profile assignments and returns
    the created assignment IDs.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  items:
    description: List of device-to-profile assignments to create.
    elements: dict
    suboptions:
      device:
        description: Device to assign to the profile.
        suboptions:
          serial:
            description: Serial of the device to be assigned to the profile.
            type: str
        type: dict
      profile:
        description: Profile to assign to the device.
        suboptions:
          id:
            description: ID of the profile to be assigned to the device.
            type: str
        type: dict
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations batchOrganizationDevicesCellularDataProfilesAssignmentsCreate
    description: Complete reference of the batchOrganizationDevicesCellularDataProfilesAssignmentsCreate
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!batch-organization-devices-cellular-data-profiles-assignments-create
notes:
  - SDK Method used are
    organizations.Organizations.batch_organization_devices_cellular_data_profiles_assignments_create,
  - Paths used are
    post /organizations/{organizationId}/devices/cellular/data/profiles/assignments/batchCreate,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_devices_cellular_data_profiles_assignments_batch_create:
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
      - device:
          serial: Q234-ABCD-5678
        profile:
          id: '42'
    organizationId: string
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
          "profile": {
            "id": "string"
          },
          "device": {
            "serial": "string"
          }
        }
      ]
    }
"""
