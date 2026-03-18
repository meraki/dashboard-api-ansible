#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_wireless_radio_rrm
short_description: Resource module for networks _wireless _radio _rrm
description:
  - Manage operation update of the resource networks _wireless _radio _rrm.
  - Update the AutoRF settings for a wireless network.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  ai:
    description: AI settings.
    suboptions:
      enabled:
        description: Toggle for enabling or disabling AI in a network.
        type: bool
    type: dict
  busyHour:
    description: Busy Hour settings.
    suboptions:
      minimizeChanges:
        description: Minimize Changes settings.
        suboptions:
          enabled:
            description: Toggle for enabling or disabling Busy Hour in a network.
            type: bool
        type: dict
      schedule:
        description: Busy hour mode settings.
        suboptions:
          manual:
            description: Manual Busy Hour settings.
            suboptions:
              end:
                description: The hour that Manual Busy Hour ends each day, in the network
                  time zone.
                type: str
              start:
                description: The hour that Manual Busy Hour starts each day, in the
                  network time zone.
                type: str
            type: dict
          mode:
            description: The Busy Hour mode applied to the network when minimizeChanges
              is enabled. Must be one of 'automatic' or 'manual'. Automatic busy hour
              is only available on firmware versions >= MR 27.0.
            type: str
        type: dict
    type: dict
  channel:
    description: Channel settings.
    suboptions:
      avoidance:
        description: Avoidance settings.
        suboptions:
          enabled:
            description: Toggle for enabling or disabling channel avoidance in a network.
            type: bool
        type: dict
    type: dict
  fra:
    description: FRA settings.
    suboptions:
      enabled:
        description: Toggle to activate or deactivate FRA in a network, contingent on
          AI-RRM being enabled.
        type: bool
    type: dict
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless updateNetworkWirelessRadioRrm
    description: Complete reference of the updateNetworkWirelessRadioRrm API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-radio-rrm
notes:
  - SDK Method used are
    wireless.Wireless.update_network_wireless_radio_rrm,

  - Paths used are
    put /networks/{networkId}/wireless/radio/rrm,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_wireless_radio_rrm:
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

    ai:
      enabled: true
    busyHour:
      minimizeChanges:
        enabled: true
      schedule:
        manual:
          end: '15:00'
          start: '10:00'
        mode: automatic
    channel:
      avoidance:
        enabled: true
    fra:
      enabled: false
    networkId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "networkId": "string",
      "name": "string",
      "timeZone": "string",
      "busyHour": {
        "schedule": {
          "mode": "string",
          "automatic": {
            "start": "string",
            "end": "string"
          },
          "manual": {
            "start": "string",
            "end": "string"
          }
        },
        "minimizeChanges": {
          "enabled": true
        }
      },
      "channel": {
        "avoidance": {
          "enabled": true
        }
      },
      "fra": {
        "enabled": true
      },
      "ai": {
        "enabled": true,
        "lastEnabledAt": "string"
      }
    }
"""
