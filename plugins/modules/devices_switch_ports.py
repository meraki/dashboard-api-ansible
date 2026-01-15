#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_switch_ports
short_description: Resource module for devices _switch _ports
description:
  - Manage operation update of the resource devices _switch _ports.
  - Update a switch port.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  accessPolicyNumber:
    description: The number of a custom access policy to configure on the switch port.
      Only applicable when 'accessPolicyType' is 'Custom access policy'.
    type: int
  accessPolicyType:
    description: The type of the access policy of the switch port. Only applicable
      to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list'
      or 'Sticky MAC allow list'.
    type: str
  adaptivePolicyGroupId:
    description: The adaptive policy group ID that will be used to tag traffic through
      this switch port. This ID must pre-exist during the configuration, else needs
      to be created using adaptivePolicy/groups API. Cannot be applied to a port on
      a switch bound to profile.
    type:
      - string
      - 'null'
  allowedVlans:
    description: The VLANs allowed on the switch port. Only applicable to trunk ports.
    type: str
  daiTrusted:
    description: If true, ARP packets for this port will be considered trusted, and
      Dynamic ARP Inspection will allow the traffic.
    type: bool
  dot3az:
    description: Dot3az settings for the port.
    suboptions:
      enabled:
        description: The Energy Efficient Ethernet status of the switch port.
        type: bool
    type: dict
  enabled:
    description: The status of the switch port.
    type: bool
  flexibleStackingEnabled:
    description: For supported switches (e.g. MS420/MS425), whether or not the port
      has flexible stacking enabled.
    type: bool
  highSpeed:
    description: High speed port enablement settings for C9500-32QC.
    suboptions:
      enabled:
        description: For C9500-32QC, whether or not the port is enabled for high speed.
        type: bool
    type: dict
  isolationEnabled:
    description: The isolation status of the switch port.
    type: bool
  linkNegotiation:
    description: The link speed for the switch port.
    type: str
  macAllowList:
    description: Only devices with MAC addresses specified in this list will have
      access to this port. Up to 20 MAC addresses can be defined. Only applicable
      when 'accessPolicyType' is 'MAC allow list'.
    elements: str
    type: list
  macWhitelistLimit:
    description: The maximum number of MAC addresses for regular MAC allow list. Only
      applicable when 'accessPolicyType' is 'MAC allow list'. Note Config only supported
      on verions greater than ms18 only for classic switches.
    type: int
  name:
    description: The name of the switch port.
    type:
      - string
      - 'null'
  peerSgtCapable:
    description: If true, Peer SGT is enabled for traffic through this switch port.
      Applicable to trunk port only, not access port. Cannot be applied to a port
      on a switch bound to profile.
    type: bool
  poeEnabled:
    description: The PoE status of the switch port.
    type: bool
  portId:
    description: PortId path parameter. Port ID.
    type: str
  portScheduleId:
    description: The ID of the port schedule. A value of null will clear the port
      schedule.
    type:
      - string
      - 'null'
  profile:
    description: Profile attributes.
    suboptions:
      enabled:
        description: When enabled, override this port's configuration with a port
          profile.
        type: bool
      id:
        description: When enabled, the ID of the port profile used to override the
          port's configuration.
        type: str
      iname:
        description: When enabled, the IName of the profile.
        type: str
    type: dict
  rstpEnabled:
    description: The rapid spanning tree protocol status.
    type: bool
  serial:
    description: Serial path parameter.
    type: str
  stickyMacAllowList:
    description: The initial list of MAC addresses for sticky Mac allow list. Only
      applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
    elements: str
    type: list
  stickyMacAllowListLimit:
    description: The maximum number of MAC addresses for sticky MAC allow list. Only
      applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
    type: int
  stormControlEnabled:
    description: The storm control status of the switch port.
    type: bool
  stpGuard:
    description: The state of the STP guard ('disabled', 'root guard', 'bpdu guard'
      or 'loop guard').
    type: str
  stpPortFastTrunk:
    description: The state of STP PortFast Trunk on the switch port.
    type: bool
  tags:
    description: The list of tags of the switch port.
    elements: str
    type: list
  type:
    description: The type of the switch port ('access', 'trunk', 'stack', 'routed',
      'svl' or 'dad').
    type: str
  udld:
    description: The action to take when Unidirectional Link is detected (Alert only,
      Enforce). Default configuration is Alert only.
    type: str
  vlan:
    description: The VLAN of the switch port. For a trunk port, this is the native
      VLAN. A null value will clear the value set for trunk ports.
    type:
      - integer
      - 'null'
  voiceVlan:
    description: The voice VLAN of the switch port. Only applicable to access ports.
    type:
      - integer
      - 'null'
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for switch updateDeviceSwitchPort
    description: Complete reference of the updateDeviceSwitchPort API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port
notes:
  - SDK Method used are
    switch.Switch.update_device_switch_port,
  - Paths used are
    put /devices/{serial}/switch/ports/{portId},
"""

EXAMPLES = r"""
- name: Update by id
  cisco.meraki.devices_switch_ports:
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
    accessPolicyNumber: 2
    accessPolicyType: Sticky MAC allow list
    adaptivePolicyGroupId: '123'
    allowedVlans: 1,3,5-10
    daiTrusted: false
    dot3az:
      enabled: false
    enabled: true
    flexibleStackingEnabled: true
    highSpeed:
      enabled: false
    isolationEnabled: false
    linkNegotiation: Auto negotiate
    macAllowList:
      - 34:56:fe:ce:8e:a0
      - 34:56:fe:ce:8e:a1
    macWhitelistLimit: 10
    name: My switch port
    peerSgtCapable: false
    poeEnabled: true
    portId: string
    portScheduleId: '1234'
    profile:
      enabled: false
      id: '1284392014819'
      iname: iname
    rstpEnabled: true
    serial: string
    stickyMacAllowList:
      - 34:56:fe:ce:8e:b0
      - 34:56:fe:ce:8e:b1
    stickyMacAllowListLimit: 5
    stormControlEnabled: true
    stpGuard: disabled
    stpPortFastTrunk: false
    tags:
      - tag1
      - tag2
    type: access
    udld: Alert only
    vlan: 10
    voiceVlan: 20
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "portId": "string",
      "name": "string",
      "tags": [
        "string"
      ],
      "enabled": true,
      "poeEnabled": true,
      "type": "string",
      "vlan": 0,
      "voiceVlan": 0,
      "allowedVlans": "string",
      "isolationEnabled": true,
      "rstpEnabled": true,
      "stpGuard": "string",
      "stpPortFastTrunk": true,
      "linkNegotiation": "string",
      "linkNegotiationCapabilities": [
        "string"
      ],
      "portScheduleId": "string",
      "schedule": {
        "id": "string",
        "name": "string"
      },
      "udld": "string",
      "accessPolicyType": "string",
      "accessPolicyNumber": 0,
      "macAllowList": [
        "string"
      ],
      "macWhitelistLimit": 0,
      "stickyMacAllowList": [
        "string"
      ],
      "stickyMacAllowListLimit": 0,
      "stormControlEnabled": true,
      "adaptivePolicyGroupId": "string",
      "adaptivePolicyGroup": {
        "id": "string",
        "name": "string"
      },
      "peerSgtCapable": true,
      "flexibleStackingEnabled": true,
      "daiTrusted": true,
      "profile": {
        "enabled": true,
        "id": "string",
        "iname": "string"
      },
      "module": {
        "model": "string",
        "serial": "string",
        "slot": 0
      },
      "mirror": {
        "mode": "string"
      },
      "dot3az": {
        "enabled": true
      },
      "highSpeed": {
        "enabled": true
      }
    }
"""
