#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_wireless_ssids_owe
short_description: Resource module for networks _wireless _ssids _owe
description:
  - Manage operation update of the resource networks _wireless _ssids _owe.
  - Update the OWE transition pairs for a network.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  transitions:
    description: Array of OWE transition pairs.
    elements: dict
    suboptions:
      ssids:
        description: The paired SSIDs in this transition.
        suboptions:
          encrypted:
            description: The encrypted (OWE) SSID.
            suboptions:
              number:
                description: SSID number (0-14).
                type: int
            type: dict
          legacy:
            description: The legacy (Open) SSID. Omit to remove pairing.
            suboptions:
              number:
                description: SSID number (0-14).
                type: int
            type: dict
        type: dict
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless updateNetworkWirelessSsidsOwe
    description: Complete reference of the updateNetworkWirelessSsidsOwe API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssids-owe
notes:
  - SDK Method used are
    wireless.Wireless.update_network_wireless_ssids_owe,
  - Paths used are
    put /networks/{networkId}/wireless/ssids/owe,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_wireless_ssids_owe:
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
    networkId: string
    transitions:
      - ssids:
          encrypted:
            number: 0
          legacy:
            number: 2
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
          "network": {
            "id": "string",
            "name": "string"
          },
          "transitions": [
            {
              "ssids": {
                "legacy": {
                  "number": 0
                },
                "encrypted": {
                  "number": 0
                }
              }
            }
          ]
        }
      ]
    }
"""
