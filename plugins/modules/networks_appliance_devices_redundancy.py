#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_appliance_devices_redundancy
short_description: Resource module for networks _appliance _devices _redundancy
description:
  - Manage operation update of the resource networks _appliance _devices _redundancy.
  - Update MX warm spare settings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  designations:
    description: Ordered warm spare roles.
    elements: dict
    suboptions:
      priority:
        description: Role priority (1=primary, 2=spare).
        type: int
      serial:
        description: Appliance serial.
        type: str
    type: list
  enabled:
    description: Enable warm spare.
    type: bool
  mode:
    description: HA mode (disabled|active-passive|active-active).
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  uplink:
    description: Uplink configuration.
    suboptions:
      interfaces:
        description: Interfaces to configure.
        elements: dict
        suboptions:
          addresses:
            description: Interface VIP addresses.
            elements: dict
            suboptions:
              address:
                description: Virtual IP.
                type: str
              subnet:
                description: Subnet for the VIP (optional).
                type: str
            type: list
          name:
            description: Interface name (wan1, wan2, ...).
            type: str
        type: list
      loadBalancing:
        description: Load balancing configuration.
        suboptions:
          enabled:
            description: Enable load balancing.
            type: bool
          vlanSelection:
            description: VLAN selection strategy.
            suboptions:
              byDevice:
                description: Per-device VLAN selection.
                elements: dict
                suboptions:
                  serial:
                    description: Device serial number.
                    type: str
                  vlanIds:
                    description: VLAN IDs participating in sharing.
                    elements: int
                    type: list
                type: list
              mode:
                description: Selection mode (auto|manual).
                type: str
            type: dict
        type: dict
      mode:
        description: Uplink mode (public|virtual).
        type: str
      sharing:
        description: HA uplink sharing properties.
        suboptions:
          byInterface:
            description: Per-interface sharing configuration.
            elements: dict
            suboptions:
              name:
                description: Interface name (wan1, wan2, ...).
                type: str
              parent:
                description: Parent appliance role (primary|secondary).
                type: str
            type: list
          enabled:
            description: Enable uplink sharing.
            type: bool
          vlanId:
            description: Uplink sharing VLAN ID.
            type: str
        type: dict
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance updateNetworkApplianceDevicesRedundancy
    description: Complete reference of the updateNetworkApplianceDevicesRedundancy
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-devices-redundancy
notes:
  - SDK Method used are
    appliance.Appliance.update_network_appliance_devices_redundancy,
  - Paths used are
    put /networks/{networkId}/appliance/devices/redundancy,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_appliance_devices_redundancy:
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
    designations:
      - priority: 1
        serial: Q234-ABCD-5678
    enabled: true
    mode: active-active
    networkId: string
    uplink:
      interfaces:
        - addresses:
            - address: 1.2.3.4
              subnet: 192.168.1.0/24
          name: wan1
      loadBalancing:
        enabled: true
        vlanSelection:
          byDevice:
            - serial: Q234-ABCD-5678
              vlanIds:
                - 1
                - 2
          mode: auto
      mode: virtual
      sharing:
        byInterface:
          - name: wan1
            parent: primary
        enabled: true
        vlanId: '100'
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "networkId": "string",
      "name": "string",
      "enabled": true,
      "mode": "string",
      "designations": [
        {
          "serial": "string",
          "priority": 0
        }
      ],
      "uplink": {
        "mode": "string",
        "interfaces": [
          {
            "name": "string",
            "addresses": [
              {
                "address": "string",
                "subnet": "string"
              }
            ]
          }
        ],
        "sharing": {
          "enabled": true,
          "vlanId": {},
          "byInterface": [
            {
              "name": "string",
              "parent": "string"
            }
          ]
        },
        "loadBalancing": {
          "enabled": true,
          "vlanSelection": {
            "mode": "string",
            "byDevice": [
              {
                "serial": "string",
                "vlanIds": [
                  0
                ]
              }
            ]
          }
        }
      }
    }
"""
