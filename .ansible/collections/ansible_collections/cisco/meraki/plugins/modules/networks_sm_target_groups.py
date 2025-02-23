#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operations create, update and delete of the resource networks _sm _target
    _groups.
  - Add a target group.
  - Delete a target group from a network.
  - Update a target group.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_sm_target_groups
notes:
  - SDK Method used are sm.Sm.create_network_sm_target_group, sm.Sm.delete_network_sm_target_group,
    sm.Sm.update_network_sm_target_group,
  - Paths used are post /networks/{networkId}/sm/targetGroups, delete /networks/{networkId}/sm/targetGroups/{targetGroupId},
    put /networks/{networkId}/sm/targetGroups/{targetGroupId},
options:
  name:
    description: The name of this target group.
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  scope:
    description: The scope and tag options of the target group. Comma separated values
      beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed
      by tags. Default to none if empty.
    type: str
  targetGroupId:
    description: TargetGroupId path parameter. Target group ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the createNetworkSmTargetGroup API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-network-sm-target-group
    name: Cisco Meraki documentation for sm createNetworkSmTargetGroup
  - description: Complete reference of the deleteNetworkSmTargetGroup API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-target-group
    name: Cisco Meraki documentation for sm deleteNetworkSmTargetGroup
  - description: Complete reference of the updateNetworkSmTargetGroup API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-sm-target-group
    name: Cisco Meraki documentation for sm updateNetworkSmTargetGroup
short_description: Resource module for networks _sm _target _groups
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_sm_target_groups:
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
    name: Target group name
    networkId: string
    scope: withAny, tag1, tag2
- name: Delete by id
  cisco.meraki.networks_sm_target_groups:
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
    state: absent
    networkId: string
    targetGroupId: string
- name: Update by id
  cisco.meraki.networks_sm_target_groups:
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
    name: Target group name
    networkId: string
    scope: withAny, tag1, tag2
    targetGroupId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "scope": "string",
      "tags": [
        "string"
      ]
    }
"""
