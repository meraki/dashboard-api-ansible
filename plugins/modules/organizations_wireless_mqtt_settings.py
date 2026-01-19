#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_mqtt_settings
short_description: Resource module for organizations _wireless _mqtt _settings
description:
  - Manage operation update of the resource organizations _wireless _mqtt _settings.
  - Add new broker config for wireless MQTT.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  ble:
    description: MQTT BLE Settings for network.
    suboptions:
      allowLists:
        description: Allowed List for MAC and UUID.
        suboptions:
          macs:
            description: Allowed MAC List.
            elements: str
            type: list
          uuids:
            description: Allowed UUID List.
            elements: str
            type: list
        type: dict
      enabled:
        description: BLE Enabled.
        type: bool
      flush:
        description: BLE Flush frequency.
        suboptions:
          frequency:
            description: BLE Flush frequency in seconds. Will be between 1 and 2147483647.
              Default is 60 seconds.
            type: int
        type: dict
      hysteresis:
        description: BLE Hysteresis Settings for network.
        suboptions:
          enabled:
            description: BLE Hysteresis Enabled.
            type: bool
          threshold:
            description: BLE Threshold. Will be between 1 and 2147483647. Default
              is 1 second.
            type: int
        type: dict
      type:
        description: BLE type of clients to publish telemetry. Valid types are all,
          ibeacon, eddystone, unknown.
        type: str
    type: dict
  mqtt:
    description: MQTT Settings for network.
    suboptions:
      broker:
        description: MQTT Broker Settings for network.
        suboptions:
          name:
            description: Broker Config Name.
            type: str
        type: dict
      enabled:
        description: MQTT Enabled.
        type: bool
      messageFields:
        description: Select fields to populate in MQTT messages. Valid types are RSSI,
          AP MAC address, Client MAC address, Timestamp, Radio, Network ID, Beacon
          type, Raw payload, Client UUID, Client major value, Client minor value,
          Signal power, Band, Slot ID.
        elements: str
        type: list
      publishing:
        description: MQTT Publishing Settings.
        suboptions:
          frequency:
            description: MQTT Publishing Frequency in seconds. Will be between 1 and
              2147483647. Default is 1 second.
            type: int
          qos:
            description: MQTT Publishing QoS. Valid types are 0, 1, 2.
            type: int
        type: dict
      topic:
        description: MQTT Topic.
        type: str
    type: dict
  network:
    description: Add MQTT Settings for network.
    suboptions:
      id:
        description: Network ID.
        type: str
    type: dict
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  wifi:
    description: MQTT Wi-Fi Settings for network.
    suboptions:
      allowLists:
        description: Allowed List for MAC and UUID.
        suboptions:
          macs:
            description: Allowed MAC List.
            elements: str
            type: list
        type: dict
      enabled:
        description: Wi-Fi Enabled.
        type: bool
      flush:
        description: BLE Flush frequency.
        suboptions:
          frequency:
            description: Wi-Fi Flush frequency in seconds. Will be between 1 and 2147483647.
              Default is 60 seconds.
            type: int
        type: dict
      hysteresis:
        description: Wi-Fi Hysteresis Settings for network.
        suboptions:
          enabled:
            description: Wi-Fi Hysteresis Enabled.
            type: bool
          threshold:
            description: Wi-Fi Threshold. Will be between 1 and 2147483647. Default
              is 1 second.
            type: int
        type: dict
      type:
        description: Wi-Fi client type. Valid types are visible, associated.
        type: str
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless updateOrganizationWirelessMqttSettings
    description: Complete reference of the updateOrganizationWirelessMqttSettings
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-mqtt-settings
notes:
  - SDK Method used are
    wireless.Wireless.update_organization_wireless_mqtt_settings,
  - Paths used are
    put /organizations/{organizationId}/wireless/mqtt/settings,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.organizations_wireless_mqtt_settings:
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
    ble:
      allowLists:
        macs: []
        uuids: []
      enabled: false
      flush:
        frequency: 60
      hysteresis:
        enabled: true
        threshold: 1
      type: ibeacon
    mqtt:
      broker:
        name: My Broker
      enabled: true
      messageFields:
        - RSSI
        - AP MAC address
        - Client MAC address
        - Timestamp
        - Radio
        - Network ID
        - Beacon type
        - Raw payload
        - Client UUID
        - Client major value
        - Client minor value
        - Signal power
        - Band
        - Slot ID
      publishing:
        frequency: 1
        qos: 1
      topic: Test Topic
    network:
      id: L_1234
    organizationId: string
    wifi:
      allowLists:
        macs: []
      enabled: false
      flush:
        frequency: 60
      hysteresis:
        enabled: false
        threshold: 1
      type: associated
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "network": {
        "id": "string",
        "name": "string"
      },
      "mqtt": {
        "settingsId": "string",
        "enabled": true,
        "topic": "string",
        "messageFields": [
          "string"
        ],
        "publishing": {
          "frequency": 0,
          "qos": 0
        },
        "broker": {
          "id": "string",
          "name": "string"
        }
      },
      "ble": {
        "enabled": true,
        "type": "string",
        "flush": {
          "frequency": 0
        },
        "allowLists": {
          "uuids": [
            "string"
          ],
          "macs": [
            "string"
          ]
        },
        "hysteresis": {
          "enabled": true,
          "threshold": 0
        }
      },
      "wifi": {
        "enabled": true,
        "type": "string",
        "flush": {
          "frequency": 0
        },
        "allowLists": {
          "macs": [
            "string"
          ]
        },
        "hysteresis": {
          "enabled": true,
          "threshold": 0
        }
      }
    }
"""
