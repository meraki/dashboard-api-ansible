#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all networks _wireless _ssids _hotspot20.
  - Return the Hotspot 2.0 settings for an SSID.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: networks_wireless_ssids_hotspot20_info
notes:
  - SDK Method used are wireless.Wireless.get_network_wireless_ssid_hotspot20,
  - Paths used are get /networks/{networkId}/wireless/ssids/{number}/hotspot20,
options:
  headers:
    description: Additional headers.
    type: dict
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
  - description: Complete reference of the getNetworkWirelessSsidHotspot20 API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-hotspot20
    name: Cisco Meraki documentation for wireless getNetworkWirelessSsidHotspot20
short_description: Information module for networks _wireless _ssids _hotspot20
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all networks _wireless _ssids _hotspot20
  cisco.meraki.networks_wireless_ssids_hotspot20_info:
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
    meraki_use_iterator_for_get_pages: "{{ meraki_use_iterator_for_get_pages }}"
    meraki_inherit_logging_config: "{{ meraki_inherit_logging_config }}"
    networkId: string
    number: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "domains": [
        "string"
      ],
      "enabled": true,
      "mccMncs": [
        {
          "mcc": "string",
          "mnc": "string"
        }
      ],
      "naiRealms": [
        {
          "format": "string",
          "methods": [
            {
              "authenticationTypes": {
                "credentials": [
                  "string"
                ],
                "eapInnerAuthentication": [
                  "string"
                ],
                "nonEapInnerAuthentication": [
                  "string"
                ],
                "tunneledEapMethodCredentials": [
                  "string"
                ]
              },
              "id": "string"
            }
          ],
          "name": "string"
        }
      ],
      "networkAccessType": "string",
      "operator": {
        "name": "string"
      },
      "roamConsortOis": [
        "string"
      ],
      "venue": {
        "name": "string",
        "type": "string"
      }
    }
"""
