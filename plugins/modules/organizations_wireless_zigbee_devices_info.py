#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_zigbee_devices_info
short_description: Information module for organizations _wireless _zigbee _devices
description:
  - Information module for Organizations Wireless Zigbee Devices Info.
  - Get all organizations _wireless _zigbee _devices.
  - List the Zigbee wireless devices for an organization or the supplied networks.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
      - Information module for Organizations Wireless Zigbee Devices Info.
      - OrganizationId path parameter. Organization ID.
    type: str
  perPage:
    description:
      - Information module for Organizations Wireless Zigbee Devices Info.
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 10.
    type: int
  startingAfter:
    description:
      - Information module for Organizations Wireless Zigbee Devices Info.
      - >
        StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.
    type: str
  endingBefore:
    description:
      - Information module for Organizations Wireless Zigbee Devices Info.
      - >
        EndingBefore query parameter. A token used by the server to indicate the end
        of the page. Often this is a timestamp or an ID but it is not limited to those.
        This parameter should not be defined by client applications. The link for
        the first, last, prev, or next page in the HTTP Link header should define
        it.
    type: str
  networkIds:
    description:
      - Information module for Organizations Wireless Zigbee Devices Info.
      - >
        NetworkIds query parameter. Parameter of networks you want the zigbee devices
        for. E.g. NetworkIds=N_12345678&networkIds=N_3456.
    elements: str
    type: list
  isEnrolled:
    description:
      - Information module for Organizations Wireless Zigbee Devices Info.
      - IsEnrolled query parameter. Filter devices based on if they are enrolled or
        not.
    type: bool
  search:
    description:
      - Information module for Organizations Wireless Zigbee Devices Info.
      - Search query parameter. Filter devices by their name, tag or serial.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getOrganizationWirelessZigbeeDevices
    description: Complete reference of the getOrganizationWirelessZigbeeDevices API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-devices
notes:
  - SDK Method used are
    wireless.Wireless.get_organization_wireless_zigbee_devices,
  - Paths used are
    get /organizations/{organizationId}/wireless/zigbee/devices,
"""

EXAMPLES = r"""
- name: Get all organizations _wireless _zigbee _devices
  cisco.meraki.organizations_wireless_zigbee_devices_info:
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
    perPage: 0
    startingAfter: string
    endingBefore: string
    networkIds: []
    isEnrolled: True
    search: string
    organizationId: string
    total_pages: -1
    direction: next
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "network": {
          "id": "string",
          "name": "string"
        },
        "panId": "string",
        "channel": "string",
        "transmitPowerLevel": 0,
        "enrolled": true,
        "status": "string",
        "gateway": {
          "name": "string",
          "mac": "string",
          "serial": "string",
          "tags": [
            "string"
          ]
        },
        "counts": {
          "doorLocks": {
            "byStatus": {
              "online": 0,
              "offline": 0,
              "dormant": 0
            }
          }
        }
      }
    ]
"""
