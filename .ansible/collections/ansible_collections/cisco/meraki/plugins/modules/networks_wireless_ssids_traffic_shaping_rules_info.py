#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all networks _wireless _ssids _traffic _shaping _rules.
  - Display the traffic shaping settings for a SSID on an MR network.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: networks_wireless_ssids_traffic_shaping_rules_info
notes:
  - SDK Method used are wireless.Wireless.get_network_wireless_ssid_traffic_shaping_rules,
  - Paths used are get /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules,
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
  - description: Complete reference of the getNetworkWirelessSsidTrafficShapingRules
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-traffic-shaping-rules
    name: Cisco Meraki documentation for wireless getNetworkWirelessSsidTrafficShapingRules
short_description: Information module for networks _wireless _ssids _traffic _shaping
  _rules
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all networks _wireless _ssids _traffic _shaping _rules
  cisco.meraki.networks_wireless_ssids_traffic_shaping_rules_info:
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
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "defaultRulesEnabled": true,
      "rules": [
        {
          "definitions": [
            {
              "type": "string",
              "value": "string"
            }
          ],
          "dscpTagValue": 0,
          "pcpTagValue": 0,
          "perClientBandwidthLimits": {
            "bandwidthLimits": {
              "limitDown": 0,
              "limitUp": 0
            },
            "settings": "string"
          }
        }
      ],
      "trafficShapingEnabled": true
    }
"""
