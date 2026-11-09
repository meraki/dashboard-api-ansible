#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_appliance_vpn_site_to_site_vpn
short_description: Resource module for networks _appliance _vpn _site _to _site _vpn
description:
  - Manage operation update of the resource networks _appliance _vpn _site _to _site
    _vpn. - > Update the site-to-site VPN settings of an MX network or configuration
    template in NAT mode. Unacknowledged warnings return 400 Bad Request with retry
    guidance in errors and the warnings in confirmations. Review the warnings returned
    in confirmations, then retry with confirmed true to accept them. Fatal errors
    must be corrected before retrying.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  confirmed:
    description: Whether to accept the confirmation warnings for these changes. Defaults
      to true, which accepts confirmation warnings and preserves the existing update
      behavior. Set to false to opt in to confirmation warnings. Review the warnings
      returned in confirmations, then retry with confirmed true to accept them. Fatal
      errors must be corrected before retrying.
    type: bool
  hostTranslations:
    description: The list of VPN host translations. Host translations are supported
      starting from MX firmware version 26.1.2.
    elements: dict
    suboptions:
      local:
        description: Configuration of the local address of the translated host.
        suboptions:
          address:
            description: The local IP address of the translated host.
            type: str
        type: dict
      name:
        description: The name of the translated host.
        type: str
      remote:
        description: Configuration of the remote address of the translated host.
        suboptions:
          address:
            description: The remote IP address of the translated host.
            type: str
        type: dict
    type: list
  hubs:
    description: The list of VPN hubs, in order of preference. In spoke mode, at least
      1 hub is required.
    elements: dict
    suboptions:
      hubId:
        description: The network ID of the hub.
        type: str
      useDefaultRoute:
        description: Only valid in 'spoke' mode. Indicates whether default route traffic
          should be sent to this hub.
        type: bool
    type: list
  mode:
    description: The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'.
    type: str
  natTraversal:
    description: NAT traversal settings. Omit to leave the existing setting unchanged.
    suboptions:
      mode:
        description: Whether NAT traversal is automatic or manually configured.
        type: str
      publicIp:
        description: The public IP address used for manual NAT traversal.
        type: str
      publicPort:
        description: The public port used for manual NAT traversal. Must be between
          1024 and 65535.
        type: int
    type: dict
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  sgt:
    description: Security Group Tag settings for the VPN peer.
    suboptions:
      enabled:
        description: Whether or not Peer SGT is enabled for traffic to this VPN peer.
        type: bool
    type: dict
  subnet:
    description: Configuration of subnet features.
    suboptions:
      nat:
        description: Configuration of NAT for subnets.
        suboptions:
          isAllowed:
            description: If enabled, VPN subnet translation can be used to translate
              any local subnets that are allowed to use the VPN into a new subnet
              with the same number of addresses.
            type: bool
        type: dict
    type: dict
  subnets:
    description: The list of local VPN subnets and their VPN presence. VLAN entries
      include vlanId and subnetting where applicable. When the corresponding NFO is
      enabled, NAT settings are returned for every VLAN; non-VLAN entries omit vlanId,
      subnetting, and nat.legacy.
    elements: dict
    suboptions:
      localSubnet:
        description: The CIDR notation subnet used within the VPN. Required for standalone
          networks.
        type: str
      nat:
        description: Configuration of NAT for the subnet.
        suboptions:
          enabled:
            description: Whether or not VPN subnet translation is enabled for the
              subnet.
            type: bool
          legacy:
            description: DEPRECATED Legacy VPN NAT settings. For VLAN entries, when
              the corresponding NFO is enabled, the related field is returned for
              every VLAN, including false values.
            type: dict
          remoteSubnet:
            description: The translated subnet to be used in the VPN.
            type: str
        type: dict
      useVpn:
        description: Indicates the presence of the subnet in the VPN.
        type: bool
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance updateNetworkApplianceVpnSiteToSiteVpn
    description: Complete reference of the updateNetworkApplianceVpnSiteToSiteVpn
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn
notes:
  - SDK Method used are
    appliance.Appliance.update_network_appliance_vpn_site_to_site_vpn,
  - Paths used are
    put /networks/{networkId}/appliance/vpn/siteToSiteVpn,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_appliance_vpn_site_to_site_vpn:
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
    confirmed: false
    hostTranslations:
      - local:
          address: 192.168.1.10
        name: Host 1
        remote:
          address: 72.168.2.10
    hubs:
      - hubId: N_4901849
        useDefaultRoute: true
    mode: spoke
    natTraversal:
      mode: manual
      publicIp: 203.0.113.8
      publicPort: 4500
    networkId: string
    sgt:
      enabled: true
    subnet:
      nat:
        isAllowed: true
    subnets:
      - localSubnet: 192.168.1.0/24
        nat:
          enabled: true
          remoteSubnet: 198.51.100.3/32
        useVpn: true
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "mode": "string",
      "hubs": [
        {
          "hubId": "string",
          "useDefaultRoute": true,
          "vrfs": [
            {
              "id": "string",
              "name": "string"
            }
          ]
        }
      ],
      "subnets": [
        {
          "localSubnet": "string",
          "useVpn": true,
          "nat": {
            "enabled": true,
            "remoteSubnet": "string",
            "legacy": {}
          }
        }
      ],
      "sgt": {
        "enabled": true
      },
      "subnet": {
        "nat": {
          "isAllowed": true
        }
      },
      "hostTranslations": [
        {
          "name": "string",
          "local": {
            "address": "string"
          },
          "remote": {
            "address": "string"
          }
        }
      ],
      "natTraversal": {
        "mode": "string",
        "publicIp": "string",
        "publicPort": 0
      }
    }
"""
