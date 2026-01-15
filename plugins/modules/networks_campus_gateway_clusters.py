#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_campus_gateway_clusters
short_description: Resource module for networks _campus _gateway _clusters
description:
  - Manage operations create and update of the resource networks _campus _gateway
    _clusters.
  - Create a cluster and add campus gateways to it.
  - Update a cluster and add/remove campus gateways to/from it.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  clusterId:
    description: ClusterId path parameter. Cluster ID.
    type: str
  devices:
    description: Devices to be added to the cluster.
    elements: dict
    suboptions:
      serial:
        description: Serial of the device.
        type: str
      tunnels:
        description: Tunnel settings of the device when tunnel interface of cluster
          is specified.
        elements: dict
        suboptions:
          addresses:
            description: Tunnel IP addresses of the device.
            elements: dict
            suboptions:
              address:
                description: IP address of the interface.
                type: str
              protocol:
                description: Protocol of the interface.
                type: str
            type: list
          interface:
            description: Tunnel interface name.
            type: str
        type: list
      uplinks:
        description: Uplink settings of the device when uplink assignment mode of
          cluster is static.
        elements: dict
        suboptions:
          addresses:
            description: Uplink IP addresses of the device.
            elements: dict
            suboptions:
              address:
                description: IP address of the interface.
                type: str
              protocol:
                description: Protocol of the interface.
                type: str
            type: list
          interface:
            description: Uplink interface name.
            type: str
        type: list
    type: list
  name:
    description: Name of the new cluster.
    type: str
  nameservers:
    description: Nameservers of the cluster.
    suboptions:
      addresses:
        description: Addresses of the nameservers.
        elements: str
        type: list
    type: dict
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  notes:
    description: Notes about cluster with max size of 511 characters allowed.
    type: str
  portChannels:
    description: Port channel settings of the cluster.
    elements: dict
    suboptions:
      allowedVlans:
        description: Allowed VLANs of the port channel.
        type: str
      name:
        description: Name of the port channel.
        type: str
      vlan:
        description: VLAN ID of the port channel.
        type: int
    type: list
  tunnels:
    description: Tunnel interface settings of the cluster Reuse uplink or specify
      tunnel interface.
    elements: dict
    suboptions:
      addresses:
        description: Addresses of the interface.
        elements: dict
        suboptions:
          gateway:
            description: Gateway of the interface.
            type: str
          protocol:
            description: Protocol of the interface.
            type: str
          subnetMask:
            description: Subnet mask of the interface.
            type: str
        type: list
      interface:
        description: Interface identifier, should be set to tun1. Specify this interface
          only if uplink isn't reused as tunnel.
        type: str
      uplink:
        description: Uplink interface details if uplink is reused as tunnel.
        suboptions:
          interface:
            description: Uplink interface identifier.
            type: str
        type: dict
      vlan:
        description: VLAN ID of the interface.
        type: int
    type: list
  uplinks:
    description: Uplink interface settings of the cluster.
    elements: dict
    suboptions:
      addresses:
        description: Addresses of the interface.
        elements: dict
        suboptions:
          assignmentMode:
            description: Assignment mode of the interface.
            type: str
          gateway:
            description: Gateway of the interface when assignment mode is static.
            type: str
          protocol:
            description: Protocol of the interface when assignment mode is static.
            type: str
          subnetMask:
            description: Subnet mask of the interface when assignment mode is static.
            type: str
        type: list
      interface:
        description: Interface identifier, should be set to man1.
        type: str
      vlan:
        description: VLAN ID of the interface.
        type: int
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for campusGateway createNetworkCampusGatewayCluster
    description: Complete reference of the createNetworkCampusGatewayCluster API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-network-campus-gateway-cluster
  - name: Cisco Meraki documentation for campusGateway updateNetworkCampusGatewayCluster
    description: Complete reference of the updateNetworkCampusGatewayCluster API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-campus-gateway-cluster
notes:
  - SDK Method used are
    campus_gateway.CampusGateway.create_network_campus_gateway_cluster,
    campus_gateway.CampusGateway.update_network_campus_gateway_cluster,
  - Paths used are
    post /networks/{networkId}/campusGateway/clusters,
    put /networks/{networkId}/campusGateway/clusters/{clusterId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_campus_gateway_clusters:
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
    devices:
      - serial: Q234-ABCD-0001
        tunnels:
          - addresses:
              - address: 6.2.6.7
                protocol: ipv4
            interface: tun1
        uplinks:
          - addresses:
              - address: 5.1.2.3
                protocol: ipv4
            interface: man1
    name: North Campus
    nameservers:
      addresses:
        - 8.8.8.8
        - 8.8.4.4
    networkId: string
    notes: This cluster is for New York Office
    portChannels:
      - allowedVlans: 10-20
        name: Port-channel1
        vlan: 25
    tunnels:
      - addresses:
          - gateway: 2.3.5.6
            protocol: ipv4
            subnetMask: 255.255.255.0
        interface: tun1
        uplink:
          interface: man1
        vlan: 6
    uplinks:
      - addresses:
          - assignmentMode: static
            gateway: 1.2.3.5
            protocol: ipv4
            subnetMask: 255.255.255.0
        interface: man1
        vlan: 5
- name: Update by id
  cisco.meraki.networks_campus_gateway_clusters:
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
    clusterId: string
    devices:
      - serial: Q234-ABCD-0001
        tunnels:
          - addresses:
              - address: 6.2.6.7
                protocol: ipv4
            interface: tun1
        uplinks:
          - addresses:
              - address: 5.1.2.3
                protocol: ipv4
            interface: man1
    name: North Campus
    nameservers:
      addresses:
        - 8.8.8.8
        - 8.8.4.4
    networkId: string
    notes: This cluster is for New York Office
    portChannels:
      - allowedVlans: 10-20
        name: Port-channel1
        vlan: 25
    tunnels:
      - addresses:
          - gateway: 2.3.5.6
            protocol: ipv4
            subnetMask: 255.255.255.0
        interface: tun1
        uplink:
          interface: man1
        vlan: 6
    uplinks:
      - addresses:
          - assignmentMode: static
            gateway: 1.2.3.5
            protocol: ipv4
            subnetMask: 255.255.255.0
        interface: man1
        vlan: 5
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "clusterId": "string",
      "name": "string",
      "uplinks": [
        {
          "interface": "string",
          "vlan": 0,
          "addresses": [
            {
              "assignmentMode": "string",
              "protocol": "string",
              "gateway": "string",
              "subnetMask": "string"
            }
          ]
        }
      ],
      "tunnels": [
        {
          "uplink": {
            "interface": "string"
          },
          "interface": "string",
          "vlan": 0,
          "addresses": [
            {
              "protocol": "string",
              "gateway": "string",
              "subnetMask": "string"
            }
          ]
        }
      ],
      "nameservers": {
        "addresses": [
          "string"
        ]
      },
      "portChannels": [
        {
          "id": "string",
          "name": "string",
          "vlan": 0,
          "allowedVlans": "string"
        }
      ],
      "devices": [
        {
          "serial": "string",
          "memberId": "string",
          "uplinks": [
            {
              "interface": "string",
              "addresses": [
                {
                  "protocol": "string",
                  "address": "string"
                }
              ]
            }
          ],
          "tunnels": [
            {
              "interface": "string",
              "addresses": [
                {
                  "protocol": "string",
                  "address": "string"
                }
              ]
            }
          ]
        }
      ],
      "notes": "string",
      "url": "string"
    }
"""
