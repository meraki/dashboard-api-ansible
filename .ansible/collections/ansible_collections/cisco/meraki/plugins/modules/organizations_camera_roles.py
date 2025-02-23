#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operations create, update and delete of the resource organizations _camera
    _roles.
  - Creates new role for this organization.
extends_documentation_fragment:
  - cisco.meraki.module
module: organizations_camera_roles
notes:
  - SDK Method used are camera.Camera.create_organization_camera_role,
  - Paths used are post /organizations/{organizationId}/camera/roles,
options:
  appliedOnDevices:
    description: Device tag on which this specified permission is applied.
    elements: dict
    suboptions:
      id:
        description: Device id.
        type: str
      inNetworksWithId:
        description: Network id scope.
        type: str
      inNetworksWithTag:
        description: Network tag scope.
        type: str
      permissionScopeId:
        description: Permission scope id.
        type: str
      tag:
        description: Device tag.
        type: str
    type: list
  appliedOnNetworks:
    description: Network tag on which this specified permission is applied.
    elements: dict
    suboptions:
      id:
        description: Network id.
        type: str
      permissionScopeId:
        description: Permission scope id.
        type: str
      tag:
        description: Network tag.
        type: str
    type: list
  appliedOrgWide:
    description: Permissions to be applied org wide.
    elements: dict
    suboptions:
      permissionScopeId:
        description: Permission scope id.
        type: str
    type: list
  name:
    description: The name of the new role. Must be unique. This parameter is required.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the createOrganizationCameraRole API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-camera-role
    name: Cisco Meraki documentation for camera createOrganizationCameraRole
short_description: Resource module for organizations _camera _roles
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_camera_roles:
    meraki_api_key: '{{ meraki_api_key }}'
    meraki_base_url: '{{ meraki_base_url }}'
    meraki_single_request_timeout: '{{ meraki_single_request_timeout }}'
    meraki_certificate_path: '{{ meraki_certificate_path }}'
    meraki_requests_proxy: '{{ meraki_requests_proxy }}'
    meraki_wait_on_rate_limit: '{{ meraki_wait_on_rate_limit }}'
    meraki_nginx_429_retry_wait_time: '{{ meraki_nginx_429_retry_wait_time }}'
    meraki_action_batch_retry_wait_time: '{{ meraki_action_batch_retry_wait_time }}'
    meraki_retry_4xx_error: '{{ meraki_retry_4xx_error }}'
    meraki_retry_4xx_error_wait_time: '{{ meraki_retry_4xx_error_wait_time }}'
    meraki_maximum_retries: '{{ meraki_maximum_retries }}'
    meraki_output_log: '{{ meraki_output_log }}'
    meraki_log_file_prefix: '{{ meraki_log_file_prefix }}'
    meraki_log_path: '{{ meraki_log_path }}'
    meraki_print_console: '{{ meraki_print_console }}'
    meraki_suppress_logging: '{{ meraki_suppress_logging }}'
    meraki_simulate: '{{ meraki_simulate }}'
    meraki_be_geo_id: '{{ meraki_be_geo_id }}'
    meraki_use_iterator_for_get_pages: '{{ meraki_use_iterator_for_get_pages }}'
    meraki_inherit_logging_config: '{{ meraki_inherit_logging_config }}'
    state: present
    appliedOnDevices:
      - id: ''
        permissionScopeId: '1'
        tag: reception-desk
    appliedOnNetworks:
      - id: ''
        permissionScopeId: '2'
        tag: building-a
    appliedOrgWide:
      - id: ''
        permissionScopeId: '2'
        tag: building-a
    name: Security_Guard
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
