#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all networks _pii _sm _owners _for _key.
  - 'Given a piece of Personally Identifiable Information PII , return the Systems
    Manager owner IDs associated with that identifier. These owner IDs can be used
    with the Systems Manager API endpoints to retrieve owner details. Exactly one
    identifier will be accepted.

    '
extends_documentation_fragment:
  - cisco.meraki.module_info
module: networks_pii_sm_owners_for_key_info
notes:
  - SDK Method used are networks.Networks.get_network_pii_sm_owners_for_key,
  - Paths used are get /networks/{networkId}/pii/smOwnersForKey,
options:
  bluetoothMac:
    description:
      - BluetoothMac query parameter. The MAC of a Bluetooth client.
    type: str
  email:
    description:
      - Email query parameter. The email of a network user account or a Systems Manager
        device.
    type: str
  headers:
    description: Additional headers.
    type: dict
  imei:
    description:
      - Imei query parameter. The IMEI of a Systems Manager device.
    type: str
  mac:
    description:
      - Mac query parameter. The MAC of a network client device or a Systems Manager
        device.
    type: str
  networkId:
    description:
      - NetworkId path parameter. Network ID.
    type: str
  serial:
    description:
      - Serial query parameter. The serial of a Systems Manager device.
    type: str
  username:
    description:
      - Username query parameter. The username of a Systems Manager user.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getNetworkPiiSmOwnersForKey API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-owners-for-key
    name: Cisco Meraki documentation for networks getNetworkPiiSmOwnersForKey
short_description: Information module for networks _pii _sm _owners _for _key
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all networks _pii _sm _owners _for _key
  cisco.meraki.networks_pii_sm_owners_for_key_info:
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
    username: string
    email: string
    mac: string
    serial: string
    imei: string
    bluetoothMac: string
    networkId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: list
  elements: str
  sample: >
    [
      "string"
    ]
"""
