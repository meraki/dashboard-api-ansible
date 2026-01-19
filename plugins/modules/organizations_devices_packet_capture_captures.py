#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_devices_packet_capture_captures
short_description: Resource module for organizations _devices _packet _capture _captures
description:
  - Manage operations create and delete of the resource organizations _devices _packet
    _capture _captures.
  - >
    Perform a packet capture on a device and store in Meraki Cloud. Only a single
    switch may be chosen per request, while multiple access points are allowed at
    once.
  - Delete a single packet capture from cloud using captureId.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  advanced:
    description: Advanced filters for IOSXE devices (supported for Campus Gateway
      devices only).
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
      innerFilterMacs:
        description: Inner MAC address filter for tunneled traffic (up to 5 MAC addresses
          for Campus Gateway devices).
        elements: str
        type: list
      maxFilesize:
        description: Maximum file size in megabytes (MB). Range 1-100 MB when bufferFiles=1,
          1-500 MB when bufferFiles=2-5.
        type: int
      packetsPerSecond:
        description: Packets per second limit for Campus Gateway devices (1-1000000).
        type: int
      physicalInterfaceDirection:
        description: Direction for physical interface capture.
        type: str
    type: dict
  captureId:
    description: CaptureId path parameter. Capture ID.
    type: str
  destination:
    description: Destination of packet capture file. Possible values upload_to_cloud.
    type: str
  duration:
    description: Duration in seconds of packet capture.
    type: int
  filterExpression:
    description: Filter expression for packet capture.
    type: str
  interface:
    description: Interface of the device.
    type: str
  name:
    description: Name of packet capture file.
    type: str
  notes:
    description: Reason for taking the packet capture.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  outputType:
    description: Output type of packet capture file. Possible values text, pcap, cloudshark,
      or upload_to_cloud.
    type: str
  ports:
    description: Ports of packet capture file, comma-separated.
    type: str
  serials:
    description: The serial(s) of the device(s).
    elements: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations createOrganizationDevicesPacketCaptureCapture
    description: Complete reference of the createOrganizationDevicesPacketCaptureCapture
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-capture
  - name: Cisco Meraki documentation for organizations deleteOrganizationDevicesPacketCaptureCapture
    description: Complete reference of the deleteOrganizationDevicesPacketCaptureCapture
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-capture
notes:
  - SDK Method used are
    organizations.Organizations.create_organization_devices_packet_capture_capture,
    organizations.Organizations.delete_organization_devices_packet_capture_capture,
  - Paths used are
    post /organizations/{organizationId}/devices/packetCapture/captures,
    delete /organizations/{organizationId}/devices/packetCapture/captures/{captureId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_devices_packet_capture_captures:
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
    advanced:
      bufferFiles: 5
      captureType: circular
      controlPlaneDirection: both
      innerFilterMacs:
        - aa:bb:cc:dd:ee:ff
        - 11:22:33:44:55:66
      maxFilesize: 10
      packetsPerSecond: 10000
      physicalInterfaceDirection: both
    destination: upload_to_cloud
    duration: 3
    filterExpression: host 10.1.27.253
    interface: wireless
    name: Capture no. 3
    notes: Debugging connectivity issue...
    organizationId: string
    outputType: upload_to_cloud
    ports: 1, 3
    serials:
      - Q234-ABCD-5678
- name: Delete by id
  cisco.meraki.organizations_devices_packet_capture_captures:
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
    captureId: string
    organizationId: string
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
