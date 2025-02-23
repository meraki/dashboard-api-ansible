#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource networks _vlan _profiles _assignments
    _reassign.
  - Update the assigned VLAN Profile for devices in a network.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_vlan_profiles_assignments_reassign
notes:
  - SDK Method used are networks.Networks.reassign_network_vlan_profiles_assignments,
  - Paths used are post /networks/{networkId}/vlanProfiles/assignments/reassign,
options:
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  serials:
    description: Array of Device Serials.
    elements: str
    type: list
  stackIds:
    description: Array of Switch Stack IDs.
    elements: str
    type: list
  vlanProfile:
    description: The VLAN Profile.
    suboptions:
      iname:
        description: IName of the VLAN Profile.
        type: str
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the reassignNetworkVlanProfilesAssignments
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!reassign-network-vlan-profiles-assignments
    name: Cisco Meraki documentation for networks reassignNetworkVlanProfilesAssignments
short_description: Resource module for networks _vlan _profiles _assignments _reassign
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_vlan_profiles_assignments_reassign:
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
    serials:
      - Q234-ABCD-5678
    stackIds:
      - '1234'
    vlanProfile:
      iname: Profile1
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "serials": [
        "string"
      ],
      "stackIds": [
        "string"
      ],
      "vlanProfile": {
        "iname": "string",
        "name": "string"
      }
    }
"""
