#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_certificates_revoke
short_description: Resource module for devices _certificates _revoke
description:
  - Manage operation create of the resource devices _certificates _revoke. - > Revoke
    a device certificate. The device and certificate are identified by the path parameters.
    You may supply a revocation reason in the request body; if omitted, a default
    reason is applied.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  certificateSerial:
    description: CertificateSerial path parameter. Certificate serial.
    type: str
  reason:
    description: Revocation reason per RFC 5280; omit to use `unspecified`.
    type: str
  serial:
    description: Serial path parameter.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for devices revokeDeviceCertificate
    description: Complete reference of the revokeDeviceCertificate API.
    link: https://developer.cisco.com/meraki/api-v1/#!revoke-device-certificate
notes:
  - SDK Method used are
    devices.Devices.revoke_device_certificate,
  - Paths used are
    post /devices/{serial}/certificates/{certificateSerial}/revoke,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.devices_certificates_revoke:
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
    certificateSerial: string
    reason: unspecified
    serial: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "message": "string",
      "result": {
        "certificate": {
          "id": "string"
        },
        "serial": "string",
        "feature": {
          "type": "string"
        }
      }
    }
"""
