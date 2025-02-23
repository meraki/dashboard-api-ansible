#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource networks _devices _claim _vmx.
  - Claim a vMX into a network.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_devices_claim_vmx
notes:
  - SDK Method used are networks.Networks.vmx_network_devices_claim,
  - Paths used are post /networks/{networkId}/devices/claim/vmx,
options:
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  size:
    description: The size of the vMX you claim. It can be one of small, medium, large,
      xlarge, 100.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the vmxNetworkDevicesClaim API.
    link: https://developer.cisco.com/meraki/api-v1/#!vmx-network-devices-claim
    name: Cisco Meraki documentation for networks vmxNetworkDevicesClaim
short_description: Resource module for networks _devices _claim _vmx
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_devices_claim_vmx:
    meraki_api_key: '{{ meraki_api_key }}'
    meraki_base_url: '{{ meraki_base_url }}'
    meraki_single_request_timeout: '{{ meraki_single_request_timeout }}'
    meraki_certificate_path: '{{ meraki_certificate_path }}'
    meraki_requests_proxy: '{{ meraki_requests_proxy }}'
    meraki_wait_on_rate_limit: '{{ meraki_wait_on_rate_limit }}'
    meraki_nginx_429_retry_wait_time: '{{ meraki_nginx_429_retry_wait_time }}'
    meraki_action_batch_retry_wait_time: '{{ meraki_action_batch_retry_wait_time }}'
    meraki_retry_4xx_error: '{{ meraki_retry_4xx_error }}'
    meraki_retry_4xx_error_wait_time: '{{ meraki_retry_4xx_error_wait_time }}'
    meraki_maximum_retries: '{{ meraki_maximum_retries }}'
    meraki_output_log: '{{ meraki_output_log }}'
    meraki_log_file_prefix: '{{ meraki_log_file_prefix }}'
    meraki_log_path: '{{ meraki_log_path }}'
    meraki_print_console: '{{ meraki_print_console }}'
    meraki_suppress_logging: '{{ meraki_suppress_logging }}'
    meraki_simulate: '{{ meraki_simulate }}'
    meraki_be_geo_id: '{{ meraki_be_geo_id }}'
    meraki_use_iterator_for_get_pages: '{{ meraki_use_iterator_for_get_pages }}'
    meraki_inherit_logging_config: '{{ meraki_inherit_logging_config }}'
    networkId: string
    size: small
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "address": "string",
      "details": [
        {
          "name": "string",
          "value": "string"
        }
      ],
      "firmware": "string",
      "imei": "string",
      "lanIp": "string",
      "lat": 0,
      "lng": 0,
      "mac": "string",
      "model": "string",
      "name": "string",
      "networkId": "string",
      "notes": "string",
      "productType": "string",
      "serial": "string",
      "tags": [
        "string"
      ]
    }
"""
