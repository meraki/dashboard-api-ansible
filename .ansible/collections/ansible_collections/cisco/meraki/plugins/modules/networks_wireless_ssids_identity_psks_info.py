#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all networks _wireless _ssids _identity _psks.
  - Get networks _wireless _ssids _identity _psks by id.
  - List all Identity PSKs in a wireless network.
  - Return an Identity PSK.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: networks_wireless_ssids_identity_psks_info
notes:
  - SDK Method used are wireless.Wireless.get_network_wireless_ssid_identity_psk,
    wireless.Wireless.get_network_wireless_ssid_identity_psks,
  - Paths used are get /networks/{networkId}/wireless/ssids/{number}/identityPsks,
    get /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId},
options:
  headers:
    description: Additional headers.
    type: dict
  identityPskId:
    description:
      - IdentityPskId path parameter. Identity psk ID.
    type: str
  networkId:
    description:
      - NetworkId path parameter. Network ID.
    type: str
  number:
    description:
      - Number path parameter.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getNetworkWirelessSsidIdentityPsk API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psk
    name: Cisco Meraki documentation for wireless getNetworkWirelessSsidIdentityPsk
  - description: Complete reference of the getNetworkWirelessSsidIdentityPsks API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psks
    name: Cisco Meraki documentation for wireless getNetworkWirelessSsidIdentityPsks
short_description: Information module for networks _wireless _ssids _identity _psks
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all networks _wireless _ssids _identity _psks
  cisco.meraki.networks_wireless_ssids_identity_psks_info:
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
    number: string
  register: result
- name: Get networks _wireless _ssids _identity _psks by id
  cisco.meraki.networks_wireless_ssids_identity_psks_info:
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
    number: string
    identityPskId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "email": "string",
      "expiresAt": "string",
      "groupPolicyId": "string",
      "id": "string",
      "name": "string",
      "passphrase": "string",
      "wifiPersonalNetworkId": "string"
    }
"""
