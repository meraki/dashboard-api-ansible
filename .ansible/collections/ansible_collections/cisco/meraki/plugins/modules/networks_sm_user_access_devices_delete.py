#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation delete of the resource networks _sm _user _access _devices _delete.
  - Delete a User Access Device.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_sm_user_access_devices_delete
notes:
  - SDK Method used are sm.Sm.delete_network_sm_user_access_device,
  - Paths used are delete /networks/{networkId}/sm/userAccessDevices/{userAccessDeviceId},
options:
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  userAccessDeviceId:
    description: UserAccessDeviceId path parameter. User access device ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the deleteNetworkSmUserAccessDevice API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device
    name: Cisco Meraki documentation for sm deleteNetworkSmUserAccessDevice
short_description: Resource module for networks _sm _user _access _devices _delete
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Delete by id
  cisco.meraki.networks_sm_user_access_devices_delete:
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
    networkId: string
    userAccessDeviceId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
