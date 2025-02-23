#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource networks _firmware _upgrades _staged _events
    _defer.
  - Postpone by 1 week all pending staged upgrade stages for a network.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_firmware_upgrades_staged_events_defer
notes:
  - SDK Method used are networks.Networks.defer_network_firmware_upgrades_staged_events,
  - Paths used are post /networks/{networkId}/firmwareUpgrades/staged/events/defer,
options:
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the deferNetworkFirmwareUpgradesStagedEvents
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!defer-network-firmware-upgrades-staged-events
    name: Cisco Meraki documentation for networks deferNetworkFirmwareUpgradesStagedEvents
short_description: Resource module for networks _firmware _upgrades _staged _events
  _defer
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_firmware_upgrades_staged_events_defer:
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
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "products": {
        "switch": {
          "nextUpgrade": {
            "toVersion": {
              "id": "string",
              "shortName": "string"
            }
          }
        }
      },
      "reasons": [
        {
          "category": "string",
          "comment": "string"
        }
      ],
      "stages": [
        {
          "group": {
            "description": "string",
            "id": "string",
            "name": "string"
          },
          "milestones": {
            "canceledAt": "string",
            "completedAt": "string",
            "scheduledFor": "string",
            "startedAt": "string"
          },
          "status": "string"
        }
      ]
    }
"""
