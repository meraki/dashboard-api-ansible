#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_zigbee_door_locks_info
short_description: Information module for organizations _wireless _zigbee _door _locks
description:
  - Get all organizations _wireless _zigbee _door _locks.
  - Return the list of door locks for a network.
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
  networkIds:
    description:
      - NetworkIds query parameter. Filter by specified Network IDs.
    elements: str
    type: list
  serial:
    description:
      - Serial query parameter. Filter by device serial.
    type: str
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 500. Default is 50.
    type: int
  startingAfter:
    description:
      - >
        StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.
    type: str
  endingBefore:
    description:
      - >
        EndingBefore query parameter. A token used by the server to indicate the end
        of the page. Often this is a timestamp or an ID but it is not limited to those.
        This parameter should not be defined by client applications. The link for
        the first, last, prev, or next page in the HTTP Link header should define
        it.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getOrganizationWirelessZigbeeDoorLocks
    description: Complete reference of the getOrganizationWirelessZigbeeDoorLocks
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-door-locks
notes:
  - SDK Method used are
    wireless.Wireless.get_organization_wireless_zigbee_door_locks,
  - Paths used are
    get /organizations/{organizationId}/wireless/zigbee/doorLocks,
"""

EXAMPLES = r"""
- name: Get all organizations _wireless _zigbee _door _locks
  cisco.meraki.organizations_wireless_zigbee_door_locks_info:
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
    networkIds: []
    serial: string
    perPage: 0
    startingAfter: string
    endingBefore: string
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
    ]
"""
