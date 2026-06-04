#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_sase_connectors_batch_create
short_description: Resource module for organizations _sase _connectors _batch _create
description:
  - Manage operation create of the resource organizations _sase _connectors _batch
    _create.
  - Deploy SSE Connectors for specified regions.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  items:
    description: List of connectors to deploy (maximum 20 items).
    elements: dict
    suboptions:
      region:
        description: Region.
        suboptions:
          slug:
            description: Region identifier slug.
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
  - name: Cisco Meraki documentation for organizations batchOrganizationSaseConnectorsCreate
    description: Complete reference of the batchOrganizationSaseConnectorsCreate API.
    link: https://developer.cisco.com/meraki/api-v1/#!batch-organization-sase-connectors-create
notes:
  - SDK Method used are
    organizations.Organizations.batch_organization_sase_connectors_create,
  - Paths used are
    post /organizations/{organizationId}/sase/connectors/batchCreate,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_sase_connectors_batch_create:
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
      - region:
          slug: us-west-1
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
          "pipelineId": "string",
          "operation": {
            "id": "string"
          },
          "status": "string",
          "counts": {
            "jobs": {
              "total": 0,
              "byStatus": {
                "completed": 0,
                "failed": 0,
                "pending": 0
              }
            }
          }
        }
      ],
      "meta": {
        "counts": {
          "items": {
            "total": 0,
            "remaining": 0
          }
        }
      }
    }
"""
