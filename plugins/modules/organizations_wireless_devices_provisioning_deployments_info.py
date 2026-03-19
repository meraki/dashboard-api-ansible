#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_devices_provisioning_deployments_info
short_description: Information module for organizations _wireless _devices _provisioning _deployments
description:
  - Get all organizations _wireless _devices _provisioning _deployments.
  - List the zero touch deployments for wireless access points in an organization.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable range is 3 - 1000. Default is 20.
    type: int
  startingAfter:
    description:
      - >
        StartingAfter query parameter. A token used by the server to indicate the start of the page. Often this
        is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client
        applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    type: str
  endingBefore:
    description:
      - >
        EndingBefore query parameter. A token used by the server to indicate the end of the page. Often this is
        a timestamp or an ID but it is not limited to those. This parameter should not be defined by client
        applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    type: str
  search:
    description:
      - Search query parameter. Filter by MAC address, serial number, new device name, old device name, or model.
    type: str
  sortBy:
    description:
      - SortBy query parameter. Field used to sort results. Default is 'status'.
    type: str
  sortOrder:
    description:
      - SortOrder query parameter. Sort order. Default is 'asc'.
    type: str
  deploymentType:
    description:
      - DeploymentType query parameter. Filter deployments by type.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getOrganizationWirelessDevicesProvisioningDeployments
    description: Complete reference of the getOrganizationWirelessDevicesProvisioningDeployments API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-provisioning-deployments
notes:
  - SDK Method used are
    wireless.Wireless.get_organization_wireless_devices_provisioning_deployments,

  - Paths used are
    get /organizations/{organizationId}/wireless/devices/provisioning/deployments,
"""

EXAMPLES = r"""
- name: Get all organizations _wireless _devices _provisioning _deployments
  cisco.meraki.organizations_wireless_devices_provisioning_deployments_info:
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
    perPage: 0
    startingAfter: string
    endingBefore: string
    search: string
    sortBy: string
    sortOrder: string
    deploymentType: string
    organizationId: string
    total_pages: -1
    direction: next
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "items": [
          {
            "deploymentId": "string",
            "devices": {
              "old": {
                "serial": "string",
                "afterAction": "string",
                "name": "string",
                "model": "string",
                "mac": "string",
                "tags": [
                  "string"
                ],
                "rfProfile": {
                  "id": "string",
                  "name": "string"
                }
              },
              "new": {
                "serial": "string",
                "name": "string",
                "model": "string",
                "mac": "string",
                "tags": [
                  "string"
                ],
                "rfProfile": {
                  "id": "string",
                  "name": "string"
                }
              }
            },
            "status": "string",
            "type": "string",
            "network": {
              "id": "string",
              "name": "string"
            },
            "createdAt": "string",
            "requestedAt": "string",
            "lastUpdatedAt": "string",
            "completedAt": "string",
            "errors": [
              "string"
            ]
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
    ]
"""
