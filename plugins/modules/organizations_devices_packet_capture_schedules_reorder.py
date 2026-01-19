#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_devices_packet_capture_schedules_reorder
short_description: Resource module for organizations _devices _packet _capture _schedules
  _reorder
description:
  - Manage operation create of the resource organizations _devices _packet _capture
    _schedules _reorder.
  - Bulk update priorities of pcap schedules.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  order:
    description: Array of schedule IDs and their priorities to reorder.
    elements: dict
    suboptions:
      priority:
        description: The priority of the schedule.
        type: int
      scheduleId:
        description: ID of the schedule to update to the specified priority.
        type: str
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations reorderOrganizationDevicesPacketCaptureSchedules
    description: Complete reference of the reorderOrganizationDevicesPacketCaptureSchedules
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!reorder-organization-devices-packet-capture-schedules
notes:
  - SDK Method used are
    organizations.Organizations.reorder_organization_devices_packet_capture_schedules,
  - Paths used are
    post /organizations/{organizationId}/devices/packetCapture/schedules/reorder,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_devices_packet_capture_schedules_reorder:
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
    order:
      - priority: 1
        scheduleId: '1234'
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "updatedPriorities": [
        {
          "scheduleId": "string",
          "priority": 0
        }
      ]
    }
"""
