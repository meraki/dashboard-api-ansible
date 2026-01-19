#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_devices_packet_capture_schedules
short_description: Resource module for organizations _devices _packet _capture _schedules
description:
  - Manage operations create, update and delete of the resource organizations _devices
    _packet _capture _schedules.
  - Create a schedule for packet capture.
  - Delete schedule from cloud.
  - Update a schedule for packet capture.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  devices:
    description: Device details.
    elements: dict
    suboptions:
      interface:
        description: Interface to capture.
        type: str
      serial:
        description: Serial of the devices to schedule packet capture.
        type: str
      switchports:
        description: Switchports to capture.
        type: str
    type: list
  duration:
    description: Duration of the capture in seconds.
    type: int
  enabled:
    description: Enable or disable the schedule.
    type: bool
  filterExpression:
    description: Filter expression for the capture.
    type: str
  name:
    description: Name of the packet capture file.
    type: str
  notes:
    description: Reason for capture.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  schedule:
    description: Schedule details.
    suboptions:
      endTs:
        description: End date and time of the recurring schedule entry.
        type: str
      frequency:
        description: Frequency of the recurring schedule entry (hour, week, month,
          day, minute).
        type: str
      name:
        description: Name of the schedule.
        type: str
      recurrence:
        description: Cardinality of the schedule frequency, ex. 1 = every day, 2 =
          every other day (when frequency = day).
        type: int
      startTs:
        description: Start date and time of the recurring schedule entry.
        type: str
      weekdays:
        description: Weekdays for the schedule Sunday, Monday, Tuesday, Wednesday,
          Thursday, Friday, Saturday.
        elements: str
        type: list
    type: dict
  scheduleId:
    description: ScheduleId path parameter. Schedule ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations createOrganizationDevicesPacketCaptureSchedule
    description: Complete reference of the createOrganizationDevicesPacketCaptureSchedule
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-schedule
  - name: Cisco Meraki documentation for organizations deleteOrganizationDevicesPacketCaptureSchedule
    description: Complete reference of the deleteOrganizationDevicesPacketCaptureSchedule
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-schedule
  - name: Cisco Meraki documentation for organizations updateOrganizationDevicesPacketCaptureSchedule
    description: Complete reference of the updateOrganizationDevicesPacketCaptureSchedule
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-devices-packet-capture-schedule
notes:
  - SDK Method used are
    organizations.Organizations.create_organization_devices_packet_capture_schedule,
    organizations.Organizations.delete_organization_devices_packet_capture_schedule,
    organizations.Organizations.update_organization_devices_packet_capture_schedule,
  - Paths used are
    post /organizations/{organizationId}/devices/packetCapture/schedules,
    delete /organizations/{organizationId}/devices/packetCapture/schedules/{scheduleId},
    put /organizations/{organizationId}/devices/packetCapture/schedules/{scheduleId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_devices_packet_capture_schedules:
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
    devices:
      - interface: TenGigabitEthernet0/0/0
        serial: Q234-ABCD-5678
        switchports: 1, 2
    duration: 60
    enabled: true
    filterExpression: (icmp)
    name: daily_capture_for_debugging
    notes: Debugging persistent issue on device
    organizationId: string
    schedule:
      endTs: '2021-01-01T14:00:00Z'
      frequency: daily
      name: Daily at 1pm
      recurrence: 1
      startTs: '2021-01-01T13:00:00Z'
      weekdays:
        - Monday
        - Wednesday
        - Friday
- name: Update by id
  cisco.meraki.organizations_devices_packet_capture_schedules:
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
    devices:
      - interface: TenGigabitEthernet0/0/0
        serial: Q234-ABCD-5678
        switchports: 1, 2
    duration: 60
    enabled: true
    filterExpression: (icmp)
    name: daily_capture_for_debugging
    notes: Debugging persistent issue on device
    organizationId: string
    schedule:
      endTs: '2021-01-01T14:00:00Z'
      frequency: daily
      name: Daily at 1pm
      recurrence: 1
      startTs: '2021-01-01T13:00:00Z'
      weekdays:
        - Monday
        - Wednesday
        - Friday
    scheduleId: string
- name: Delete by id
  cisco.meraki.organizations_devices_packet_capture_schedules:
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
    state: absent
    organizationId: string
    scheduleId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "scheduleId": "string",
      "devices": [
        {
          "device": {
            "serial": "string",
            "switchports": "string",
            "interface": "string"
          }
        }
      ],
      "name": "string",
      "admin": {
        "id": "string",
        "name": "string"
      },
      "notes": "string",
      "duration": 0,
      "filterExpression": "string",
      "createdAt": "string",
      "updatedAt": "string",
      "captureCount": 0,
      "lastCaptureId": "string",
      "enabled": true,
      "priority": 0,
      "schedule": {
        "name": "string",
        "startTs": "string",
        "endTs": "string",
        "frequency": "string",
        "weekdays": [
          "string"
        ],
        "recurrence": 0,
        "nextCaptureTs": "string"
      },
      "warnings": [
        "string"
      ]
    }
"""
