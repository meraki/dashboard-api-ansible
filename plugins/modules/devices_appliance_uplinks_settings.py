#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_appliance_uplinks_settings
short_description: Resource module for devices _appliance _uplinks _settings
description:
  - Manage operation update of the resource devices _appliance _uplinks _settings.
  - Update the uplink settings for a secure router or security appliance.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  interfaces:
    description: Interface settings.
    suboptions:
      wan1:
        description: WAN 1 settings.
        suboptions:
          enabled:
            description: Enable or disable the interface.
            type: bool
          pppoe:
            description: Configuration options for PPPoE.
            suboptions:
              authentication:
                description: Settings for PPPoE Authentication.
                suboptions:
                  enabled:
                    description: Whether PPPoE authentication is enabled.
                    type: bool
                  password:
                    description: Password for PPPoE authentication. This parameter
                      is not returned.
                    type: str
                  username:
                    description: Username for PPPoE authentication.
                    type: str
                type: dict
              enabled:
                description: Whether PPPoE is enabled.
                type: bool
            type: dict
          svis:
            description: SVI settings by protocol.
            suboptions:
              ipv4:
                description: IPv4 settings for static/dynamic mode.
                suboptions:
                  address:
                    description: IP address and subnet mask when in static mode.
                    type: str
                  assignmentMode:
                    description: The assignment mode for this SVI. Applies only when
                      PPPoE is disabled.
                    type: str
                  gateway:
                    description: Gateway IP address when in static mode.
                    type: str
                  nameservers:
                    description: The nameserver settings for this SVI.
                    suboptions:
                      addresses:
                        description: Up to 2 nameserver addresses to use, ordered
                          in priority from highest to lowest priority. The addresses
                          must be unique.
                        elements: str
                        type: list
                    type: dict
                type: dict
              ipv6:
                description: IPv6 settings for static/dynamic mode.
                suboptions:
                  address:
                    description: Static IPv6 address in CIDR notation that overrides
                      addresses received by SLAAC when PPPoE is disabled. With PPPoE
                      enabled, use a bare IPv6 address without a prefix.
                    type: str
                  assignmentMode:
                    description: The assignment mode for this SVI. Applies only when
                      PPPoE is disabled.
                    type: str
                  gateway:
                    description: Static gateway that will override the one received
                      by autoconf.
                    type: str
                  nameservers:
                    description: The nameserver settings for this SVI.
                    suboptions:
                      addresses:
                        description: Up to 2 nameserver addresses to use, ordered
                          in priority from highest to lowest priority.
                        elements: str
                        type: list
                    type: dict
                type: dict
            type: dict
          transition:
            description: Configuration options for IPoE transition IPv4 to IPv6.
            suboptions:
              authentication:
                description: Settings for IPoE transition Authentication.
                suboptions:
                  enabled:
                    description: Whether IPoE transition authentication is enabled.
                    type: bool
                  password:
                    description: Password for IPoE transition authentication. This
                      parameter is not returned.
                    type: str
                  username:
                    description: Username for IPoE transition authentication.
                    type: str
                type: dict
              enabled:
                description: Whether the IPoE transition IPv4 to IPv6 is enabled.
                type: bool
              ipv4:
                description: IPv4 specific settings for the IPoE transition.
                suboptions:
                  local:
                    description: Static IPv4 settings for the IPoE transition.
                    suboptions:
                      address:
                        description: Static IPv4 information used for host origination
                          and NAT44 translation.
                        type: str
                    type: dict
                type: dict
              ipv6:
                description: IPv6 specific settings for the IPoE transition.
                suboptions:
                  borderRelay:
                    description: Settings for the border relay for the IPoE transition
                      Authentication.
                    suboptions:
                      address:
                        description: CIDR for the border relay for the IPoE transition
                          authentication.
                        type: str
                      mode:
                        description: Mode selection for the border relay for the IPoE
                          transition.
                        type: str
                    type: dict
                  interfaceId:
                    description: The 64-bit interface ID (suffix) of the uplink IPv6
                      address.
                    type: str
                type: dict
              isp:
                description: ISP selection for the IPoE transition.
                suboptions:
                  name:
                    description: ISP name for the IPoE transition.
                    type: str
                type: dict
              map:
                description: MAP-E/MAP-T settings for the IPoE transition.
                suboptions:
                  draft:
                    description: MAP-E draft mode.
                    suboptions:
                      enabled:
                        description: Whether MAP-E draft mode is enabled. This field
                          is accepted only for MAP-E. Null is treated as omitted and
                          preserves the existing setting.
                        type: bool
                    type: dict
                  rules:
                    description: MAP rule source and manual rule entries.
                    suboptions:
                      entries:
                        description: Manual MAP rules. At most one entry is supported.
                        elements: dict
                        suboptions:
                          borderRelay:
                            description: MAP border relay address or prefix.
                            suboptions:
                              address:
                                description: IPv6 border relay address for MAP-E.
                                type: str
                              prefix:
                                description: IPv6 border relay prefix for MAP-T in
                                  CIDR notation, with a prefix length from 0 to 96.
                                type: str
                            type: dict
                          eaBitLength:
                            description: Embedded address bit length (0-48).
                            type: int
                          ipv4:
                            description: IPv4 settings used by the MAP rule.
                            suboptions:
                              prefix:
                                description: IPv4 prefix used by the MAP rule.
                                suboptions:
                                  address:
                                    description: IPv4 network address used by the
                                      MAP rule, without the prefix length.
                                    type: str
                                  length:
                                    description: IPv4 prefix length (0-32).
                                    type: int
                                type: dict
                            type: dict
                          ipv6:
                            description: IPv6 settings used by the MAP rule.
                            suboptions:
                              prefix:
                                description: IPv6 prefix used by the MAP rule.
                                suboptions:
                                  address:
                                    description: IPv6 network address used by the
                                      MAP rule, without the prefix length.
                                    type: str
                                  length:
                                    description: IPv6 prefix length (0-128).
                                    type: int
                                type: dict
                            type: dict
                          psIdOffset:
                            description: PSID offset (0-15).
                            type: int
                        type: list
                      source:
                        description: How MAP rules are obtained. HTTPS requires an
                          ISP supported for the transition mode.
                        type: str
                    type: dict
                type: dict
              mode:
                description: Mode selector for the IPoE transition IPv4 to IPv6 is
                  enabled.
                type: str
            type: dict
          vlanTagging:
            description: VLAN tagging settings.
            suboptions:
              enabled:
                description: Whether VLAN tagging is enabled.
                type: bool
              vlanId:
                description: The ID of the VLAN to use for VLAN tagging.
                type: int
            type: dict
        type: dict
      wan2:
        description: WAN 2 settings.
        suboptions:
          enabled:
            description: Enable or disable the interface.
            type: bool
          pppoe:
            description: Configuration options for PPPoE.
            suboptions:
              authentication:
                description: Settings for PPPoE Authentication.
                suboptions:
                  enabled:
                    description: Whether PPPoE authentication is enabled.
                    type: bool
                  password:
                    description: Password for PPPoE authentication. This parameter
                      is not returned.
                    type: str
                  username:
                    description: Username for PPPoE authentication.
                    type: str
                type: dict
              enabled:
                description: Whether PPPoE is enabled.
                type: bool
            type: dict
          svis:
            description: SVI settings by protocol.
            suboptions:
              ipv4:
                description: IPv4 settings for static/dynamic mode.
                suboptions:
                  address:
                    description: IP address and subnet mask when in static mode.
                    type: str
                  assignmentMode:
                    description: The assignment mode for this SVI. Applies only when
                      PPPoE is disabled.
                    type: str
                  gateway:
                    description: Gateway IP address when in static mode.
                    type: str
                  nameservers:
                    description: The nameserver settings for this SVI.
                    suboptions:
                      addresses:
                        description: Up to 2 nameserver addresses to use, ordered
                          in priority from highest to lowest priority. The addresses
                          must be unique.
                        elements: str
                        type: list
                    type: dict
                type: dict
              ipv6:
                description: IPv6 settings for static/dynamic mode.
                suboptions:
                  address:
                    description: Static IPv6 address in CIDR notation that overrides
                      addresses received by SLAAC when PPPoE is disabled. With PPPoE
                      enabled, use a bare IPv6 address without a prefix.
                    type: str
                  assignmentMode:
                    description: The assignment mode for this SVI. Applies only when
                      PPPoE is disabled.
                    type: str
                  gateway:
                    description: Static gateway that will override the one received
                      by autoconf.
                    type: str
                  nameservers:
                    description: The nameserver settings for this SVI.
                    suboptions:
                      addresses:
                        description: Up to 2 nameserver addresses to use, ordered
                          in priority from highest to lowest priority.
                        elements: str
                        type: list
                    type: dict
                type: dict
            type: dict
          transition:
            description: Configuration options for IPoE transition IPv4 to IPv6.
            suboptions:
              authentication:
                description: Settings for IPoE transition Authentication.
                suboptions:
                  enabled:
                    description: Whether IPoE transition authentication is enabled.
                    type: bool
                  password:
                    description: Password for IPoE transition authentication. This
                      parameter is not returned.
                    type: str
                  username:
                    description: Username for IPoE transition authentication.
                    type: str
                type: dict
              enabled:
                description: Whether the IPoE transition IPv4 to IPv6 is enabled.
                type: bool
              ipv4:
                description: IPv4 specific settings for the IPoE transition.
                suboptions:
                  local:
                    description: Static IPv4 settings for the IPoE transition.
                    suboptions:
                      address:
                        description: Static IPv4 information used for host origination
                          and NAT44 translation.
                        type: str
                    type: dict
                type: dict
              ipv6:
                description: IPv6 specific settings for the IPoE transition.
                suboptions:
                  borderRelay:
                    description: Settings for the border relay for the IPoE transition
                      Authentication.
                    suboptions:
                      address:
                        description: CIDR for the border relay for the IPoE transition
                          authentication.
                        type: str
                      mode:
                        description: Mode selection for the border relay for the IPoE
                          transition.
                        type: str
                    type: dict
                  interfaceId:
                    description: The 64-bit interface ID (suffix) of the uplink IPv6
                      address.
                    type: str
                type: dict
              isp:
                description: ISP selection for the IPoE transition.
                suboptions:
                  name:
                    description: ISP name for the IPoE transition.
                    type: str
                type: dict
              map:
                description: MAP-E/MAP-T settings for the IPoE transition.
                suboptions:
                  draft:
                    description: MAP-E draft mode.
                    suboptions:
                      enabled:
                        description: Whether MAP-E draft mode is enabled. This field
                          is accepted only for MAP-E. Null is treated as omitted and
                          preserves the existing setting.
                        type: bool
                    type: dict
                  rules:
                    description: MAP rule source and manual rule entries.
                    suboptions:
                      entries:
                        description: Manual MAP rules. At most one entry is supported.
                        elements: dict
                        suboptions:
                          borderRelay:
                            description: MAP border relay address or prefix.
                            suboptions:
                              address:
                                description: IPv6 border relay address for MAP-E.
                                type: str
                              prefix:
                                description: IPv6 border relay prefix for MAP-T in
                                  CIDR notation, with a prefix length from 0 to 96.
                                type: str
                            type: dict
                          eaBitLength:
                            description: Embedded address bit length (0-48).
                            type: int
                          ipv4:
                            description: IPv4 settings used by the MAP rule.
                            suboptions:
                              prefix:
                                description: IPv4 prefix used by the MAP rule.
                                suboptions:
                                  address:
                                    description: IPv4 network address used by the
                                      MAP rule, without the prefix length.
                                    type: str
                                  length:
                                    description: IPv4 prefix length (0-32).
                                    type: int
                                type: dict
                            type: dict
                          ipv6:
                            description: IPv6 settings used by the MAP rule.
                            suboptions:
                              prefix:
                                description: IPv6 prefix used by the MAP rule.
                                suboptions:
                                  address:
                                    description: IPv6 network address used by the
                                      MAP rule, without the prefix length.
                                    type: str
                                  length:
                                    description: IPv6 prefix length (0-128).
                                    type: int
                                type: dict
                            type: dict
                          psIdOffset:
                            description: PSID offset (0-15).
                            type: int
                        type: list
                      source:
                        description: How MAP rules are obtained. HTTPS requires an
                          ISP supported for the transition mode.
                        type: str
                    type: dict
                type: dict
              mode:
                description: Mode selector for the IPoE transition IPv4 to IPv6 is
                  enabled.
                type: str
            type: dict
          vlanTagging:
            description: VLAN tagging settings.
            suboptions:
              enabled:
                description: Whether VLAN tagging is enabled.
                type: bool
              vlanId:
                description: The ID of the VLAN to use for VLAN tagging.
                type: int
            type: dict
        type: dict
    type: dict
  serial:
    description: Serial path parameter.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance updateDeviceApplianceUplinksSettings
    description: Complete reference of the updateDeviceApplianceUplinksSettings API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-uplinks-settings
notes:
  - SDK Method used are
    appliance.Appliance.update_device_appliance_uplinks_settings,
  - Paths used are
    put /devices/{serial}/appliance/uplinks/settings,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.devices_appliance_uplinks_settings:
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
    interfaces:
      wan1:
        enabled: true
        pppoe:
          authentication:
            enabled: true
            password: password
            username: username
          enabled: true
        svis:
          ipv4:
            address: 9.10.11.10/16
            assignmentMode: static
            gateway: 13.14.15.16
            nameservers:
              addresses:
                - 1.2.3.4
          ipv6:
            address: 1:2:3::4/64
            assignmentMode: static
            gateway: 1:2:3::5
            nameservers:
              addresses:
                - 1001:4860:4860::8888
                - 1001:4860:4860::8844
        transition:
          authentication:
            enabled: true
            password: password
            username: 4o6ddns
          enabled: true
          ipv4:
            local:
              address: null
          ipv6:
            borderRelay:
              address: null
              mode: auto
            interfaceId: null
          isp:
            name: OCN IPoE
          map:
            draft:
              enabled: false
            rules:
              entries:
                - borderRelay:
                    address: 2001:db8:ffff::1
                    prefix: null
                  eaBitLength: 20
                  ipv4:
                    prefix:
                      address: 192.0.2.0
                      length: 18
                  ipv6:
                    prefix:
                      address: '2001:db8:100::'
                      length: 36
                  psIdOffset: 6
              source: manual
          mode: MAP-E
        vlanTagging:
          enabled: true
          vlanId: 1
      wan2:
        enabled: true
        pppoe:
          authentication:
            enabled: true
            password: password
            username: username
          enabled: true
        svis:
          ipv4:
            address: 9.10.11.10/16
            assignmentMode: static
            gateway: 13.14.15.16
            nameservers:
              addresses:
                - 1.2.3.4
          ipv6:
            address: 1:2:3::4/64
            assignmentMode: static
            gateway: 1:2:3::5
            nameservers:
              addresses:
                - 1001:4860:4860::8888
                - 1001:4860:4860::8844
        transition:
          authentication:
            enabled: true
            password: password
            username: 4o6ddns
          enabled: true
          ipv4:
            local:
              address: null
          ipv6:
            borderRelay:
              address: null
              mode: auto
            interfaceId: null
          isp:
            name: OCN IPoE
          map:
            draft:
              enabled: false
            rules:
              entries:
                - borderRelay:
                    address: 2001:db8:ffff::1
                    prefix: null
                  eaBitLength: 20
                  ipv4:
                    prefix:
                      address: 192.0.2.0
                      length: 18
                  ipv6:
                    prefix:
                      address: '2001:db8:100::'
                      length: 36
                  psIdOffset: 6
              source: manual
          mode: MAP-E
        vlanTagging:
          enabled: true
          vlanId: 1
      wan3:
        mtu:
          limit: 1500
    serial: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "wan1": {
        "enabled": true,
        "vlanTagging": {
          "enabled": true,
          "vlanId": 0
        },
        "svis": {
          "ipv4": {
            "assignmentMode": "string",
            "address": "string",
            "gateway": "string",
            "nameservers": {
              "addresses": [
                "string"
              ]
            }
          },
          "ipv6": {
            "assignmentMode": "string",
            "address": "string",
            "gateway": "string",
            "nameservers": {
              "addresses": [
                "string"
              ]
            }
          }
        },
        "pppoe": {
          "enabled": true,
          "authentication": {
            "enabled": true,
            "username": "string"
          }
        },
        "transition": {
          "enabled": true,
          "mode": "string",
          "authentication": {
            "enabled": true,
            "username": "string"
          },
          "ipv4": {
            "local": {
              "address": {}
            }
          },
          "ipv6": {
            "borderRelay": {
              "mode": "string",
              "address": {}
            },
            "interfaceId": {}
          },
          "isp": {
            "name": "string"
          },
          "map": {
            "rules": {
              "source": {},
              "entries": [
                {
                  "ipv6": {
                    "prefix": {
                      "address": "string",
                      "length": 0
                    }
                  },
                  "ipv4": {
                    "prefix": {
                      "address": "string",
                      "length": 0
                    }
                  },
                  "borderRelay": {
                    "address": {},
                    "prefix": {}
                  },
                  "eaBitLength": 0,
                  "psIdOffset": 0
                }
              ]
            },
            "draft": {
              "enabled": {}
            }
          }
        }
      },
      "wan2": {
        "enabled": true,
        "vlanTagging": {
          "enabled": true,
          "vlanId": 0
        },
        "svis": {
          "ipv4": {
            "assignmentMode": "string",
            "address": "string",
            "gateway": "string",
            "nameservers": {
              "addresses": [
                "string"
              ]
            }
          },
          "ipv6": {
            "assignmentMode": "string",
            "address": "string",
            "gateway": "string",
            "nameservers": {
              "addresses": [
                "string"
              ]
            }
          }
        },
        "pppoe": {
          "enabled": true,
          "authentication": {
            "enabled": true,
            "username": "string"
          }
        },
        "transition": {
          "enabled": true,
          "mode": "string",
          "authentication": {
            "enabled": true,
            "username": "string"
          },
          "ipv4": {
            "local": {
              "address": {}
            }
          },
          "ipv6": {
            "borderRelay": {
              "mode": "string",
              "address": {}
            },
            "interfaceId": {}
          },
          "isp": {
            "name": "string"
          },
          "map": {
            "rules": {
              "source": {},
              "entries": [
                {
                  "ipv6": {
                    "prefix": {
                      "address": "string",
                      "length": 0
                    }
                  },
                  "ipv4": {
                    "prefix": {
                      "address": "string",
                      "length": 0
                    }
                  },
                  "borderRelay": {
                    "address": {},
                    "prefix": {}
                  },
                  "eaBitLength": 0,
                  "psIdOffset": 0
                }
              ]
            },
            "draft": {
              "enabled": {}
            }
          }
        }
      }
    }
"""
