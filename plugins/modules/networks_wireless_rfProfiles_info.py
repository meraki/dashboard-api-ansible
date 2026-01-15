#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_wireless_rfProfiles_info
short_description: Information module for networks _wireless _rfprofiles
description:
  - Information module for Networks Wireless Rfprofiles Info.
  - Get all networks _wireless _rfprofiles.
  - Get networks _wireless _rfprofiles by id.
  - List RF profiles for this network.
  - Return a RF profile.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
  - Information module for Networks Wireless Rfprofiles Info.
      - NetworkId path parameter. Network ID.
    type: str
  includeTemplateProfiles:
    description:
  - Information module for Networks Wireless Rfprofiles Info.
      - >
        IncludeTemplateProfiles query parameter. If the network is bound to a template,
        this parameter controls whether or not the non-basic RF profiles defined on
        the template should be included in the response alongside the non-basic profiles
        defined on the bound network. Defaults to false.
    type: bool
  rfProfileId:
    description:
  - Information module for Networks Wireless Rfprofiles Info.
      - RfProfileId path parameter. Rf profile ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getNetworkWirelessRfProfile
    description: Complete reference of the getNetworkWirelessRfProfile API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profile
  - name: Cisco Meraki documentation for wireless getNetworkWirelessRfProfiles
    description: Complete reference of the getNetworkWirelessRfProfiles API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_network_wireless_rf_profile,
    wireless.Wireless.get_network_wireless_rf_profiles,
  - Paths used are
    get /networks/{networkId}/wireless/rfProfiles,
    get /networks/{networkId}/wireless/rfProfiles/{rfProfileId},
"""

EXAMPLES = r"""
- name: Get all networks _wireless _rfprofiles
  cisco.meraki.networks_wireless_rf_profiles_info:
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
    includeTemplateProfiles: True
    networkId: string
  register: result
- name: Get networks _wireless _rfprofiles by id
  cisco.meraki.networks_wireless_rf_profiles_info:
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
    rfProfileId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "networkId": "string",
      "name": "string",
      "clientBalancingEnabled": true,
      "minBitrateType": "string",
      "bandSelectionType": "string",
      "apBandSettings": {
        "bandOperationMode": "string",
        "bands": {
          "enabled": [
            "string"
          ]
        },
        "bandSteeringEnabled": true
      },
      "twoFourGhzSettings": {
        "maxPower": 0,
        "minPower": 0,
        "minBitrate": 0,
        "validAutoChannels": [
          0
        ],
        "axEnabled": true,
        "rxsop": 0
      },
      "fiveGhzSettings": {
        "maxPower": 0,
        "minPower": 0,
        "minBitrate": 0,
        "validAutoChannels": [
          0
        ],
        "channelWidth": "string",
        "rxsop": 0
      },
      "sixGhzSettings": {
        "maxPower": 0,
        "minPower": 0,
        "minBitrate": 0,
        "validAutoChannels": [
          0
        ],
        "channelWidth": "string",
        "rxsop": 0
      },
      "transmission": {
        "enabled": true
      },
      "perSsidSettings": {
        "0": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "1": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "2": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "3": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "4": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "5": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "6": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "7": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "8": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "9": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "10": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "11": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "12": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "13": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        },
        "14": {
          "name": "string",
          "minBitrate": 0,
          "bandOperationMode": "string",
          "bands": {
            "enabled": [
              "string"
            ]
          },
          "bandSteeringEnabled": true
        }
      },
      "isIndoorDefault": true,
      "isOutdoorDefault": true
    }
"""
