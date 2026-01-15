#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_devices_packet_capture_captures_bulk_create
short_description: Resource module for organizations _devices _packet _capture _captures
  _bulk _create
description:
  - Manage operation create of the resource organizations _devices _packet _capture
    _captures _bulk _create.
  - Perform a packet capture on multiple devices and store in Meraki Cloud.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  advanced:
    description: Advanced capture options (optional).
    suboptions:
      bufferFiles:
        description: Number of buffer files for circular buffer capture (1-5 for Campus
          Gateway devices).
        type: int
      captureType:
        description: Type of capture. Possible values linear (default), circular.
        type: str
      controlPlaneDirection:
        description: Direction for control plane capture.
        type: str
      innerFilterMac:
        description: Inner MAC address filter for tunneled traffic (up to 5 MAC addresses
          for Campus Gateway devices).
        elements: str
        type: list
      maxFilesize:
        description: Maximum file size in megabytes (MB). Range 1-100 MB when bufferFiles=1,
          1-500 MB when bufferFiles=2-5.
        type: int
      physicalInterfaceDirection:
        description: Direction for physical interface capture.
        type: str
    type: dict
  devices:
    description: Device details (maximum of 20 devices allowed).
    elements: dict
    suboptions:
      interface:
        description: Interfaces to capture.
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
  filterExpression:
    description: Filter expression for the capture.
    type: str
  name:
    description: Name of packet capture file.
    type: str
  notes:
    description: Reason for capture.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations bulkOrganizationDevicesPacketCaptureCapturesCreate
    description: Complete reference of the bulkOrganizationDevicesPacketCaptureCapturesCreate
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-captures-create
notes:
  - SDK Method used are
    organizations.Organizations.bulk_organization_devices_packet_capture_captures_create,
  - Paths used are
    post /organizations/{organizationId}/devices/packetCapture/captures/bulkCreate,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_devices_packet_capture_captures_bulk_create:
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
    advanced:
      bufferFiles: 5
      captureType: circular
      controlPlaneDirection: both
      innerFilterMac:
        - aa:bb:cc:dd:ee:ff
        - 11:22:33:44:55:66
      maxFilesize: 10
      physicalInterfaceDirection: both
    devices:
      - interface: TenGigabitEthernet0/0/0
        serial: Q234-ABCD-5678
        switchports: 1, 2
    duration: 60
    filterExpression: (icmp)
    name: Capture no. 3
    notes: Debugging persistent issue on device
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
          "captureId": "string",
          "network": {
            "id": "string",
            "name": "string"
          },
          "devices": [
            {}
          ],
          "device": {
            "name": "string",
            "serial": "string"
          },
          "admin": {
            "id": "string",
            "name": "string"
          },
          "client": {
            "id": "string",
            "mac": "string"
          },
          "details": [
            {
              "name": "string",
              "value": "string",
              "productType": "string"
            }
          ],
          "name": "string",
          "startTs": "string",
          "ports": "string",
          "status": "string",
          "errorMessage": "string",
          "destination": "string",
          "process": "string",
          "file": {
            "size": 0
          },
          "duration": 0,
          "filterExpression": "string",
          "counts": {
            "packets": {
              "total": 0
            }
          },
          "interface": "string"
        }
      ]
    }
"""
