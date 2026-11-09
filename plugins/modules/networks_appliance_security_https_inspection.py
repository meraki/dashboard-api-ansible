#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_appliance_security_https_inspection
short_description: Resource module for networks _appliance _security _https _inspection
description:
  - Manage operation update of the resource networks _appliance _security _https _inspection.
  - Update HTTPS inspection configuration for a network.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  allowLists:
    description: Allow lists for HTTPS inspection exclusions.
    suboptions:
      applications:
        description: Specific applications to be excluded from inspection. Maximum
          600 entries.
        elements: dict
        suboptions:
          id:
            description: Application ID.
            type: str
          name:
            description: Application name.
            type: str
        type: list
      l3:
        description: Layer 3 allow list of source IP addresses excluded from inspection.
          Maximum 600 entries.
        elements: str
        type: list
      l7:
        description: Layer 7 allow list of domains excluded from inspection. Maximum
          600 entries.
        elements: str
        type: list
    type: dict
  enabled:
    description: Whether HTTPS inspection is enabled.
    type: bool
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance updateNetworkApplianceSecurityHttpsInspection
    description: Complete reference of the updateNetworkApplianceSecurityHttpsInspection
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-https-inspection
notes:
  - SDK Method used are
    appliance.Appliance.update_network_appliance_security_https_inspection,
  - Paths used are
    put /networks/{networkId}/appliance/security/httpsInspection,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_appliance_security_https_inspection:
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
    allowLists:
      applications:
        - id: meraki:layer7/application/5
          name: Advertising.com
      l3:
        - 192.0.2.10
      l7:
        - '*.example.com'
    enabled: true
    networkId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "network": {
        "id": "string"
      },
      "enabled": true,
      "allowLists": {
        "l3": [
          "string"
        ],
        "l7": [
          "string"
        ],
        "applications": [
          {
            "id": "string",
            "name": "string"
          }
        ]
      }
    }
"""
