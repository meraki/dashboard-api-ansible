#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_devices_packet_capture_captures_stop
short_description: Resource module for organizations _devices _packet _capture _captures
  _stop
description:
  - Manage operation create of the resource organizations _devices _packet _capture
    _captures _stop.
  - Stop a specific packet capture not supported for Catalyst devices .
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  captureId:
    description: CaptureId path parameter. Capture ID.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  serials:
    description: The serial(s) of the device(s) to stop the capture on.
    elements: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations stopOrganizationDevicesPacketCaptureCapture
    description: Complete reference of the stopOrganizationDevicesPacketCaptureCapture
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!stop-organization-devices-packet-capture-capture
notes:
  - SDK Method used are
    organizations.Organizations.stop_organization_devices_packet_capture_capture,
  - Paths used are
    post /organizations/{organizationId}/devices/packetCapture/captures/{captureId}/stop,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_devices_packet_capture_captures_stop:
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
    captureId: string
    organizationId: string
    serials:
      - Q234-ABCD-5678
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
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
"""
