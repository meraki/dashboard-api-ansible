#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_zigbee_door_locks
short_description: Resource module for organizations _wireless _zigbee _door _locks
description:
  - Manage operation update of the resource organizations _wireless _zigbee _door
    _locks.
  - Endpoint to batch update door locks params.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  doorLockId:
    description: DoorLockId path parameter. Door lock ID.
    type: str
  name:
    description: Door lock name to update.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless updateOrganizationWirelessZigbeeDoorLock
    description: Complete reference of the updateOrganizationWirelessZigbeeDoorLock
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-zigbee-door-lock
notes:
  - SDK Method used are
    wireless.Wireless.update_organization_wireless_zigbee_door_lock,
  - Paths used are
    put /organizations/{organizationId}/wireless/zigbee/doorLocks/{doorLockId},
"""

EXAMPLES = r"""
- name: Update by id
  cisco.meraki.organizations_wireless_zigbee_door_locks:
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
    doorLockId: string
    name: 'door #123'
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "doorLockId": "string",
      "name": "string",
      "shortId": "string",
      "lqi": "string",
      "rssi": "string",
      "status": "string",
      "eui64": "string",
      "enrolledAt": "string",
      "lastSeenAt": "string",
      "network": {
        "id": "string",
        "name": "string"
      },
      "gateway": {
        "name": "string",
        "serial": "string"
      }
    }
"""
