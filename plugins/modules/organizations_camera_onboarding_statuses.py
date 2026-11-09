#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_camera_onboarding_statuses
short_description: Resource module for organizations _camera _onboarding _statuses
description:
  - Manage operation update of the resource organizations _camera _onboarding _statuses.
  - Notify that credential handoff to camera has completed.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  serial:
    description: Serial of camera.
    type: str
  wirelessCredentialsSent:
    description: Note whether credentials were sent successfully.
    type: bool
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for camera updateOrganizationCameraOnboardingStatuses
    description: Complete reference of the updateOrganizationCameraOnboardingStatuses
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-camera-onboarding-statuses
notes:
  - SDK Method used are
    camera.Camera.update_organization_camera_onboarding_statuses,
  - Paths used are
    put /organizations/{organizationId}/camera/onboarding/statuses,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.organizations_camera_onboarding_statuses:
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
    serial: Q234-ABCD-5678
    wirelessCredentialsSent: true
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
