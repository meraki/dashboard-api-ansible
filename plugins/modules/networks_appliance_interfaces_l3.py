#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_appliance_interfaces_l3
short_description: Resource module for networks _appliance _interfaces l3
description:
  - Manage operations create, update and delete of the resource networks _appliance
    _interfaces l3.
  - Create wired L3 interface.
  - Delete wired L3 interface.
  - Update wired L3 interface.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  interfaceId:
    description: InterfaceId path parameter. Interface ID.
    type: str
  ipv4:
    description: IPv4 configuration.
    suboptions:
      address:
        description: IPv4 address.
        type: str
      subnet:
        description: IPv4 subnet in CIDR notation.
        type: str
    type: dict
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  port:
    description: Port configuration.
    suboptions:
      interface:
        description: Structured interface identifier for the port being modified.
        suboptions:
          name:
            description: Read-only full interface name for the port.
            type: str
          number:
            description: Leaf port number for the port.
            type: int
          slot:
            description: Slot number for the port.
            type: int
          subslot:
            description: Subslot number for the port.
            type: int
        type: dict
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance createNetworkApplianceInterfacesL3
    description: Complete reference of the createNetworkApplianceInterfacesL3 API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-interfaces-l3
  - name: Cisco Meraki documentation for appliance deleteNetworkApplianceInterfacesL3
    description: Complete reference of the deleteNetworkApplianceInterfacesL3 API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-interfaces-l3
  - name: Cisco Meraki documentation for appliance updateNetworkApplianceInterfacesL3
    description: Complete reference of the updateNetworkApplianceInterfacesL3 API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-interfaces-l3
notes:
  - SDK Method used are
    appliance.Appliance.create_network_appliance_interfaces_l3,
    appliance.Appliance.delete_network_appliance_interfaces_l3,
    appliance.Appliance.update_network_appliance_interfaces_l3,
  - Paths used are
    post /networks/{networkId}/appliance/interfaces/l3,
    delete /networks/{networkId}/appliance/interfaces/l3/{interfaceId},
    put /networks/{networkId}/appliance/interfaces/l3/{interfaceId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_appliance_interfaces_l3:
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
    state: present
    ipv4:
      address: 192.0.2.1
      subnet: 192.0.2.0/24
    networkId: string
    port:
      interface:
        name: GigabitEthernet0/0/1
        number: 1
        slot: 0
        subslot: 0
- name: Update by id
  cisco.meraki.networks_appliance_interfaces_l3:
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
    state: present
    interfaceId: string
    ipv4:
      address: 192.0.2.1
      subnet: 192.0.2.0/24
    networkId: string
    port:
      interface:
        name: GigabitEthernet0/0/1
        number: 1
        slot: 0
        subslot: 0
- name: Delete by id
  cisco.meraki.networks_appliance_interfaces_l3:
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
    state: absent
    interfaceId: string
    networkId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "interfaceId": "string",
      "ipv4": {
        "address": "string",
        "subnet": "string"
      },
      "port": {
        "interface": {
          "name": {},
          "slot": {},
          "subslot": {},
          "number": {}
        }
      }
    }
"""
