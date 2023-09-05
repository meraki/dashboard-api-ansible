#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: organizations_action_batches
short_description: Resource module for organizations _actionbatches
description:
- Manage operations create, update and delete of the resource organizations _actionbatches.
- Create an action batch.
- Delete an action batch.
- Update an action batch.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  actionBatchId:
    description: ActionBatchId path parameter. Action batch ID.
    type: str
  actions:
    description: A set of changes to make as part of this action (<a href='https //developer.cisco.com/meraki/api/#...
      details</a>).
    elements: dict
    suboptions:
      body:
        description: The body of the action.
        type: dict
      operation:
        description: The operation to be used.
        type: str
      resource:
        description: Unique identifier for the resource to be acted on.
        type: str
    type: list
  confirmed:
    description: Set to true for immediate execution. Set to false if the action should
      be previewed before executing. This property cannot be unset once it is true.
      Defaults to false.
    type: bool
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  synchronous:
    description: Set to true to force the batch to run synchronous. There can be at
      most 20 actions in synchronous batch. Defaults to false.
    type: bool
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for organizations createOrganizationActionBatch
  description: Complete reference of the createOrganizationActionBatch API.
  link: https://developer.cisco.com/meraki/api-v1/#!create-organization-action-batch
- name: Cisco Meraki documentation for organizations deleteOrganizationActionBatch
  description: Complete reference of the deleteOrganizationActionBatch API.
  link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-action-batch
- name: Cisco Meraki documentation for organizations updateOrganizationActionBatch
  description: Complete reference of the updateOrganizationActionBatch API.
  link: https://developer.cisco.com/meraki/api-v1/#!update-organization-action-batch
notes:
  - SDK Method used are
    organizations.Organizations.create_organization_action_batch,
    organizations.Organizations.delete_organization_action_batch,
    organizations.Organizations.update_organization_action_batch,

  - Paths used are
    post /organizations/{organizationId}/actionBatches,
    delete /organizations/{organizationId}/actionBatches/{actionBatchId},
    put /organizations/{organizationId}/actionBatches/{actionBatchId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_action_batches:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    actions:
    - operation: create
      resource: /devices/QXXX-XXXX-XXXX/switch/ports/3
    confirmed: true
    organizationId: string
    synchronous: true

- name: Update by id
  cisco.meraki.organizations_action_batches:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    actionBatchId: string
    confirmed: true
    organizationId: string
    synchronous: false

- name: Delete by id
  cisco.meraki.organizations_action_batches:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: absent
    actionBatchId: string
    organizationId: string

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "organizationId": "string",
      "confirmed": true,
      "synchronous": true,
      "status": {
        "completed": true,
        "failed": true,
        "errors": [
          "string"
        ],
        "createdResources": [
          {
            "id": "string",
            "uri": "string"
          }
        ]
      },
      "actions": [
        {
          "resource": "string",
          "operation": "string"
        }
      ]
    }
"""
