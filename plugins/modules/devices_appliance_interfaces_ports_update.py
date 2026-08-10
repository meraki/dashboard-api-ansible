#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_appliance_interfaces_ports_update
short_description: Resource module for devices _appliance _interfaces _ports _update
description:
  - Manage operation create of the resource devices _appliance _interfaces _ports
    _update.
  - Update configurations for an appliance's specified port.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  downlink:
    description: The port's VLAN settings when in LAN mode.
    suboptions:
      access:
        description: The port's settings when in 'access' mode.
        suboptions:
          policy:
            description: The access policy settings for this port.
            suboptions:
              type:
                description: The access policy that will be enforced by the 'access'
                  VLAN.
                type: str
            type: dict
          vlan:
            description: The VLAN for which this port will accept and pass traffic
              in 'access' mode. All untagged traffic will automatically be treated
              as if it belonged to this VLAN.
            type: str
        type: dict
      mode:
        description: Indicates whether the port is in 'trunk' or 'access' mode.
        type: str
      sgt:
        description: Security Group Tag settings for this port.
        suboptions:
          id:
            description: Adaptive policy group ID that all traffic originating from
              this port is assigned to.
            type: str
        type: dict
      trunk:
        description: The port's settings when in 'trunk' mode.
        suboptions:
          allowedVlans:
            description: The VLANs for which this port will accept and pass traffic
              in 'trunk' mode. This must include the Native VLAN if one is set.
            elements: str
            type: list
          nativeVlan:
            description: The Native VLAN for the port. All untagged traffic that comes
              in on this port will be treated as if it belonged to this VLAN. This
              can also be set to 0 to drop untagged traffic.
            type: str
          sgt:
            description: Security Group Tag settings for this trunk port.
            suboptions:
              enabled:
                description: Indicates whether the trunk port is Peer SGT capable.
                type: bool
            type: dict
        type: dict
    type: dict
  enabled:
    description: Indicates whether the port is enabled.
    type: bool
  interface:
    description: The interface tuple used to identify the port.
    suboptions:
      number:
        description: The leaf port number.
        type: int
      slot:
        description: The slot number for the port.
        type: int
      subslot:
        description: The subslot number for the port.
        type: int
    type: dict
  personality:
    description: Describes the port's configurability.
    suboptions:
      layer:
        description: Describes the port's layer configurability.
        suboptions:
          mode:
            description: The layer at which the port operates.
            type: int
        type: dict
      mode:
        description: The type of interface, 'wan' or 'lan', the port is configured
          as.
        type: str
    type: dict
  serial:
    description: Serial path parameter.
    type: str
  uplink:
    description: The port's settings when in WAN mode.
    suboptions:
      type:
        description: Describes the uplink device.
        type: str
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance createDeviceApplianceInterfacesPortsUpdate
    description: Complete reference of the createDeviceApplianceInterfacesPortsUpdate
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-device-appliance-interfaces-ports-update
notes:
  - SDK Method used are
    appliance.Appliance.create_device_appliance_interfaces_ports_update,
  - Paths used are
    post /devices/{serial}/appliance/interfaces/ports/update,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.devices_appliance_interfaces_ports_update:
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
    downlink:
      access:
        policy:
          type: 802.1X
        vlan: '1'
      mode: access
      sgt:
        id: '1234'
      trunk:
        allowedVlans:
          - '2'
          - '3'
          - '4'
          - '5'
        nativeVlan: '2'
        sgt:
          enabled: false
    enabled: true
    interface:
      number: 3
      slot: 1
      subslot: 2
    personality:
      layer:
        mode: 3
      mode: wan
    serial: string
    uplink:
      type: ethernet
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "number": "string",
      "interface": {
        "name": "string",
        "slot": {},
        "subslot": {},
        "number": 0
      },
      "enabled": true,
      "name": "string",
      "personality": {
        "mode": "string",
        "isFlexible": true,
        "layer": {
          "mode": 0,
          "isFlexible": true
        }
      },
      "uplink": {
        "type": "string",
        "primary": true
      },
      "downlink": {
        "mode": "string",
        "sgt": {
          "id": {}
        },
        "access": {
          "vlan": "string",
          "policy": {
            "type": {}
          }
        },
        "trunk": {
          "nativeVlan": "string",
          "allowedVlans": [
            "string"
          ],
          "sgt": {
            "enabled": true
          }
        }
      }
    }
"""
