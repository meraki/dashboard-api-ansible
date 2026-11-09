#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_inventory_devices_swaps_bulk
short_description: Resource module for organizations _inventory _devices _swaps _bulk
description:
  - Manage operation create of the resource organizations _inventory _devices _swaps
    _bulk.
  - Swap the devices identified by devices.old with a devices.new, then perform the
    afterAction on the devices.old.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  swaps:
    description: List of replacments to perform.
    elements: dict
    suboptions:
      afterAction:
        description: What action to perform on devices.old after the device cloning
          is complete. 'remove from network' will return the device to inventory,
          while 'release from organization inventory' will free up the license attached
          to the device.
        type: str
      devices:
        description: The devices involved in the swap.
        suboptions:
          new:
            description: The serial of the device that the old device's settings will
              be cloned to.
            type: str
          old:
            description: The serial of the device to be cloned.
            type: str
        type: dict
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations createOrganizationInventoryDevicesSwapsBulk
    description: Complete reference of the createOrganizationInventoryDevicesSwapsBulk
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-devices-swaps-bulk
notes:
  - SDK Method used are
    organizations.Organizations.create_organization_inventory_devices_swaps_bulk,
  - Paths used are
    post /organizations/{organizationId}/inventory/devices/swaps/bulk,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_inventory_devices_swaps_bulk:
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
    swaps:
      - afterAction: remove from network
        devices:
          new: Q234-ABCD-5678
          old: Q234-ABCD-5678
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "jobId": "string",
      "swaps": [
        {
          "id": "string",
          "devices": {
            "old": {
              "mac": "string",
              "serial": "string",
              "model": "string",
              "name": "string"
            },
            "new": {
              "mac": "string",
              "serial": "string",
              "model": "string",
              "name": "string"
            }
          },
          "status": "string",
          "afterAction": "string",
          "createdAt": "string",
          "completedAt": "string",
          "errors": [
            "string"
          ]
        }
      ]
    }
"""
