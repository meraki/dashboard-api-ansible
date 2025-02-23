#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all organizations _action _batches.
  - Get organizations _action _batches by id.
  - Return an action batch.
  - Return the list of action batches in the organization.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: organizations_action_batches_info
notes:
  - SDK Method used are organizations.Organizations.get_organization_action_batch,
    organizations.Organizations.get_organization_action_batches,
  - Paths used are get /organizations/{organizationId}/actionBatches, get /organizations/{organizationId}/actionBatches/{actionBatchId},
options:
  actionBatchId:
    description:
      - ActionBatchId path parameter. Action batch ID.
    type: str
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  status:
    description:
      - Status query parameter. Filter batches by status. Valid types are pending,
        completed, and failed.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getOrganizationActionBatch API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batch
    name: Cisco Meraki documentation for organizations getOrganizationActionBatch
  - description: Complete reference of the getOrganizationActionBatches API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batches
    name: Cisco Meraki documentation for organizations getOrganizationActionBatches
short_description: Information module for organizations _action _batches
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all organizations _action _batches
  cisco.meraki.organizations_action_batches_info:
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
    status: string
    organizationId: string
  register: result
- name: Get organizations _action _batches by id
  cisco.meraki.organizations_action_batches_info:
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
    organizationId: string
    actionBatchId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "actions": [
        {
          "body": {},
          "operation": "string",
          "resource": "string"
        }
      ],
      "callback": {
        "id": "string",
        "status": "string",
        "url": "string"
      },
      "confirmed": true,
      "id": "string",
      "organizationId": "string",
      "status": {
        "completed": true,
        "createdResources": [
          {
            "id": "string",
            "uri": "string"
          }
        ],
        "errors": [
          "string"
        ],
        "failed": true
      },
      "synchronous": true
    }
"""
