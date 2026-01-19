#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_cellular_gateway_esims_inventory
short_description: Resource module for organizations _cellular _gateway _esims _inventory
description:
  - Manage operation update of the resource organizations _cellular _gateway _esims
    _inventory.
  - Toggle the status of an eSIM.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  id:
    description: Id path parameter.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  status:
    description: Status the eSIM will be updated to.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for cellularGateway updateOrganizationCellularGatewayEsimsInventory
    description: Complete reference of the updateOrganizationCellularGatewayEsimsInventory
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-inventory
notes:
  - SDK Method used are
    cellular_gateway.CellularGateway.update_organization_cellular_gateway_esims_inventory,
  - Paths used are
    put /organizations/{organizationId}/cellularGateway/esims/inventory/{id},
"""

EXAMPLES = r"""
- name: Update by id
  cisco.meraki.organizations_cellular_gateway_esims_inventory:
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
    id: string
    organizationId: string
    status: activated
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "device": {
        "name": "string",
        "model": "string",
        "serial": "string",
        "url": "string",
        "status": "string"
      },
      "active": true,
      "eid": "string",
      "lastUpdatedAt": "string",
      "network": {
        "id": "string"
      },
      "profiles": [
        {
          "customApns": [
            "string"
          ],
          "iccid": "string",
          "status": "string",
          "serviceProvider": {
            "name": "string",
            "plans": [
              {
                "name": "string",
                "type": "string"
              }
            ]
          }
        }
      ]
    }
"""
