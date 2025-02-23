#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource networks _snmp.
  - Update the SNMP settings for a network.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_snmp
notes:
  - SDK Method used are networks.Networks.update_network_snmp,
  - Paths used are put /networks/{networkId}/snmp,
options:
  access:
    description: The type of SNMP access. Can be one of 'none' (disabled), 'community'
      (V1/V2c), or 'users' (V3).
    type: str
  communityString:
    description: The SNMP community string. Only relevant if 'access' is set to 'community'.
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  users:
    description: The list of SNMP users. Only relevant if 'access' is set to 'users'.
    elements: dict
    suboptions:
      passphrase:
        description: The passphrase for the SNMP user. Required.
        type: str
      username:
        description: The username for the SNMP user. Required.
        type: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateNetworkSnmp API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-snmp
    name: Cisco Meraki documentation for networks updateNetworkSnmp
short_description: Resource module for networks _snmp
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_snmp:
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
    state: present
    access: users
    communityString: sample
    networkId: string
    users:
      - passphrase: hunter2
        username: AzureDiamond
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "access": "string",
      "communityString": "string",
      "users": [
        {
          "passphrase": "string",
          "username": "string"
        }
      ]
    }
"""
