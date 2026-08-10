#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_appliance_umbrella_policies_add
short_description: Resource module for networks _appliance _umbrella _policies _add
description:
  - Manage operation create of the resource networks _appliance _umbrella _policies
    _add. - > Add one Cisco Umbrella DNS security policy to an MX network by policy
    ID. Idempotent — if the policy is already applied, the request succeeds and returns
    the current policy set unchanged.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  policy:
    description: Umbrella policy to add.
    suboptions:
      id:
        description: Umbrella policy ID.
        type: str
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance addNetworkApplianceUmbrellaPolicies
    description: Complete reference of the addNetworkApplianceUmbrellaPolicies API.
    link: https://developer.cisco.com/meraki/api-v1/#!add-network-appliance-umbrella-policies
notes:
  - SDK Method used are
    appliance.Appliance.add_network_appliance_umbrella_policies,
  - Paths used are
    post /networks/{networkId}/appliance/umbrella/policies/add,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_appliance_umbrella_policies_add:
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
    networkId: string
    policy:
      id: '13408726'
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "network": {
        "id": "string"
      },
      "policies": [
        {
          "id": "string"
        }
      ]
    }
"""
