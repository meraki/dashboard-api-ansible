#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource networks _cellular _gateway _subnet _pool.
  - Update the subnet pool and mask configuration for MGs in the network.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_cellular_gateway_subnet_pool
notes:
  - SDK Method used are cellular_gateway.CellularGateway.update_network_cellular_gateway_subnet_pool,
  - Paths used are put /networks/{networkId}/cellularGateway/subnetPool,
options:
  cidr:
    description: CIDR of the pool of subnets. Each MG in this network will automatically
      pick a subnet from this pool.
    type: str
  mask:
    description: Mask used for the subnet of all MGs in this network.
    type: int
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateNetworkCellularGatewaySubnetPool
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-subnet-pool
    name: Cisco Meraki documentation for cellularGateway updateNetworkCellularGatewaySubnetPool
short_description: Resource module for networks _cellular _gateway _subnet _pool
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_cellular_gateway_subnet_pool:
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
    cidr: 192.168.0.0/16
    mask: 24
    networkId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "cidr": "string",
      "deploymentMode": "string",
      "mask": 0,
      "subnets": [
        {
          "applianceIp": "string",
          "name": "string",
          "serial": "string",
          "subnet": "string"
        }
      ]
    }
"""
