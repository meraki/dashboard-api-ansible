#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_appliance_vpn_thirdPartyVPNPeers
short_description: Resource module for organizations _appliance _vpn _thirdpartyvpnpeers
description:
  - Manage operation update of the resource organizations _appliance _vpn _thirdpartyvpnpeers.
  - Update the third party VPN peers for an organization.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  peers:
    description: The list of VPN peers.
    elements: dict
    suboptions:
      ebgpNeighbor:
        description: Optional The BGP neighbor configuration for the VPN peer. Supported
          only for MX 19.1 and above.
        suboptions:
          ebgpHoldTimer:
            description: The eBGP hold timer in seconds for each neighbor. The eBGP
              hold timer must be an integer between 12 and 240.
            type: int
          ebgpMultihop:
            description: Configure this if the neighbor is not adjacent. The eBGP
              multi-hop must be an integer between 1 and 255.
            type: int
          ipVersion:
            description: The IP version of the neighbor.
            type: int
          multiExitDiscriminator:
            description: Configures the local metric associated with routes received
              from the remote peer. Routes from peers with lower metrics are will
              be preferred. Must be an integer between 0 and 4294967295. MED is 6th
              in the decision tree when identical routes from multiple peers exist.
            type: int
          neighborIp:
            description: IPv4/IPv6 address of the neighbor.
            type: str
          pathPrepend:
            description: Prepends the AS_PATH BGP Attribute associated with routes
              received from the remote peer. Configurable value of ASNs to prepend.
              Length of the array may not exceed 10, and each ASN in the array must
              be an integer between 1 and 4294967295. AS_PATH is 4th in the decision
              tree when identical routes from multiple peers exist.
            elements: int
            type: list
          remoteAsNumber:
            description: Remote ASN of the neighbor. The remote ASN must be an integer
              between 1 and 4294967295.
            type: int
          sourceIp:
            description: Source IP of eBGP neighbor.
            type: str
          weight:
            description: Configures the local metric associated with routes received
              from the remote peer. Routes from peers with lower metrics are will
              be preferred. Must be an integer between 0 and 4294967295. MED is 6th
              in the decision tree when identical routes from multiple peers exist.
            type: int
        type: dict
      group:
        description: Optional Contains the mapping between primary tunnel and backup
          tunnels.
        suboptions:
          activeActiveTunnel:
            description: Optional Both primary and backup tunnels are active.
            type: bool
          failover:
            description: Optional Contains the failover configuration for the group.
            suboptions:
              directToInternet:
                description: Optional When both primary and backup tunnels are down,
                  direct traffic to the internet. Traffic will be routed via the WAN.
                type: bool
            type: dict
          number:
            description: Optional Represents the ordering of primary and backup tunnels
              group. Primary and backup tunnels are grouped by this number. If you
              submit a request with the numbers 1, 9, 999, these numbers will be automatically
              adjusted to a sequential order starting from 1. So, they will be changed
              to 1, 2, 3 to reflect their positions in the sequence.
            type: int
        type: dict
      ikeVersion:
        description: Optional The IKE version to be used for the IPsec VPN peer configuration.
          Defaults to '1' when omitted.
        type: str
      ipsecPolicies:
        description: Custom IPSec policies for the VPN peer. If not included and a
          preset has not been chosen, the default preset for IPSec policies will be
          used.
        suboptions:
          childAuthAlgo:
            description: This is the authentication algorithms to be used in Phase
              2. The value should be an array with one of the following algorithms
              'sha256', 'sha1', 'md5'.
            elements: str
            type: list
          childCipherAlgo:
            description: This is the cipher algorithms to be used in Phase 2. The
              value should be an array with one or more of the following algorithms
              'aes256', 'aes192', 'aes128', 'tripledes', 'des', 'null'.
            elements: str
            type: list
          childLifetime:
            description: The lifetime of the Phase 2 SA in seconds.
            type: int
          childPfsGroup:
            description: This is the Diffie-Hellman group to be used for Perfect Forward
              Secrecy in Phase 2. The value should be an array with one of the following
              values 'disabled','group14', 'group5', 'group2', 'group1'.
            elements: str
            type: list
          ikeAuthAlgo:
            description: This is the authentication algorithm to be used in Phase
              1. The value should be an array with one of the following algorithms
              'sha256', 'sha1', 'md5'.
            elements: str
            type: list
          ikeCipherAlgo:
            description: This is the cipher algorithm to be used in Phase 1. The value
              should be an array with one of the following algorithms 'aes256', 'aes192',
              'aes128', 'tripledes', 'des'.
            elements: str
            type: list
          ikeDiffieHellmanGroup:
            description: This is the Diffie-Hellman group to be used in Phase 1. The
              value should be an array with one of the following algorithms 'group14',
              'group5', 'group2', 'group1'.
            elements: str
            type: list
          ikeLifetime:
            description: The lifetime of the Phase 1 SA in seconds.
            type: int
          ikePrfAlgo:
            description: Optional This is the pseudo-random function to be used in
              IKE_SA. The value should be an array with one of the following algorithms
              'prfsha256', 'prfsha1', 'prfmd5', 'default'. The 'default' option can
              be used to default to the Authentication algorithm.
            elements: str
            type: list
        type: dict
      ipsecPoliciesPreset:
        description: One of the following available presets 'default', 'aws', 'azure',
          'umbrella', 'zscaler'. If this is provided, the 'ipsecPolicies' parameter
          is ignored.
        type: str
      isRouteBased:
        description: Optional If true, the VPN peer is route-based. If not included,
          the default is false. Supported only for MX 19.1 and above.
        type: bool
      localId:
        description: Optional The local ID is used to identify the MX to the peer.
          This will apply to all MXs this peer applies to.
        type: str
      name:
        description: The name of the VPN peer.
        type: str
      network:
        description: Optional A list of network Names and IDs that will connect with
          this peer. Supported only for MX 19.1 and above.
        suboptions:
          ids:
            description: Optional A list of network IDs.
            elements: str
            type: list
        type: dict
      networkTags:
        description: A list of network tags that will connect with this peer. Use
          'all' for all networks. Use 'none' for no networks. If not included, the
          default is 'all'.
        elements: str
        type: list
      peerId:
        description: The ID of the IPsec peer.
        type: str
      priorityInGroup:
        description: Optional Represents the order of peer inside a group. If you
          submit a request with the numbers 1, 9, 999, these numbers will be automatically
          adjusted to a sequential order starting from 1. So, they will be changed
          to 1, 2, 3 to reflect their positions in the sequence.
        type: int
      privateSubnets:
        description: The list of the private subnets of the VPN peer.
        elements: str
        type: list
      publicHostname:
        description: Optional The public hostname of the VPN peer.
        type: str
      publicIp:
        description: Optional The public IP of the VPN peer.
        type: str
      remoteId:
        description: Optional The remote ID is used to identify the connecting VPN
          peer. This can either be a valid IPv4 Address, FQDN or User FQDN.
        type: str
      secret:
        description: The shared secret with the VPN peer.
        type: str
      slaPolicy:
        description: Optional Information about the SLA policy to be applied to the
          peer.
        suboptions:
          id:
            description: The ID of the SLA policy.
            type: str
        type: dict
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance updateOrganizationApplianceVpnThirdPartyVPNPeers
    description: Complete reference of the updateOrganizationApplianceVpnThirdPartyVPNPeers
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-third-party-vpn-peers
notes:
  - SDK Method used are
    appliance.Appliance.update_organization_appliance_vpn_third_party_vpnpeers,
  - Paths used are
    put /organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.organizations_appliance_vpn_third_party_vpnpeers:
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
    organizationId: string
    peers:
      - ebgpNeighbor:
          ebgpHoldTimer: 180
          ebgpMultihop: 2
          ipVersion: 4
          multiExitDiscriminator: 1
          neighborIp: 10.10.10.22
          pathPrepend:
            - 1
            - 2
          remoteAsNumber: 64343
          sourceIp: 10.10.10.22
          weight: 10
        group:
          activeActiveTunnel: true
          failover:
            directToInternet: true
          number: 1
        ikeVersion: '2'
        ipsecPolicies:
          childAuthAlgo:
            - sha1
          childCipherAlgo:
            - aes128
          childLifetime: 28800
          childPfsGroup:
            - disabled
          ikeAuthAlgo:
            - sha1
          ikeCipherAlgo:
            - tripledes
          ikeDiffieHellmanGroup:
            - group2
          ikeLifetime: 28800
          ikePrfAlgo:
            - prfsha1
        ipsecPoliciesPreset: default
        isRouteBased: true
        localId: myMXId@meraki.com
        name: Peer Name
        network:
          ids:
            - N_1
            - L_2
            - N_3
        networkTags:
          - none
        peerId: '1234'
        priorityInGroup: 1
        privateSubnets:
          - 192.168.1.0/24
          - 192.168.128.0/24
        publicHostname: example.com
        publicIp: 123.123.123.1
        remoteId: miles@meraki.com
        secret: Sample Password
        slaPolicy:
          id: '1234'
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    [
      {
        "peerId": "string",
        "name": "string",
        "publicIp": "string",
        "remoteId": "string",
        "localId": "string",
        "secret": "string",
        "privateSubnets": [
          "string"
        ],
        "ipsecPolicies": {
          "ikeCipherAlgo": [
            "string"
          ],
          "ikeAuthAlgo": [
            "string"
          ],
          "ikePrfAlgo": [
            "string"
          ],
          "ikeDiffieHellmanGroup": [
            "string"
          ],
          "ikeLifetime": 0,
          "childCipherAlgo": [
            "string"
          ],
          "childAuthAlgo": [
            "string"
          ],
          "childPfsGroup": [
            "string"
          ],
          "childLifetime": 0
        },
        "slaPolicy": {
          "id": "string"
        },
        "ipsecPoliciesPreset": "string",
        "ikeVersion": "string",
        "networkTags": [
          "string"
        ],
        "network": {
          "names": [
            "string"
          ],
          "ids": [
            "string"
          ]
        },
        "isRouteBased": true,
        "ebgpNeighbor": {
          "neighborId": 0,
          "neighborIp": "string",
          "ipVersion": 0,
          "remoteAsNumber": 0,
          "ebgpHoldTimer": 0,
          "ebgpMultihop": 0,
          "sourceIp": "string",
          "pathPrepend": [
            0
          ],
          "multiExitDiscriminator": 0,
          "weight": 0
        },
        "priorityInGroup": 0,
        "group": {
          "number": 0,
          "failover": {
            "directToInternet": true
          },
          "activeActiveTunnel": true
        }
      }
    ]
"""
