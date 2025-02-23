#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource organizations _switch _devices _clone.
  - 'Clone port-level and some switch-level configuration settings from a source switch
    to one or more target switches. Cloned settings include Aggregation Groups, Power
    Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring.

    '
extends_documentation_fragment:
  - cisco.meraki.module
module: organizations_switch_devices_clone
notes:
  - SDK Method used are switch.Switch.clone_organization_switch_devices,
  - Paths used are post /organizations/{organizationId}/switch/devices/clone,
options:
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  sourceSerial:
    description: Serial number of the source switch (must be on a network not bound
      to a template).
    type: str
  targetSerials:
    description: Array of serial numbers of one or more target switches (must be on
      a network not bound to a template).
    elements: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the cloneOrganizationSwitchDevices API.
    link: https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices
    name: Cisco Meraki documentation for switch cloneOrganizationSwitchDevices
short_description: Resource module for organizations _switch _devices _clone
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_switch_devices_clone:
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
    organizationId: string
    sourceSerial: Q234-ABCD-5678
    targetSerials:
      - Q234-ABCD-0001
      - Q234-ABCD-0002
      - Q234-ABCD-0003
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "sourceSerial": "string",
      "targetSerials": [
        "string"
      ]
    }
"""
