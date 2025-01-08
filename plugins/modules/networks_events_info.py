#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_events_info
short_description: Information module for networks _events
description:
  - Get all networks _events.
  - List the events for the network.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
    - NetworkId path parameter. Network ID.
    type: str
  productType:
    description:
    - >
      ProductType query parameter. The product type to fetch events for. This parameter is required for networks
      with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera,
      cellularGateway, wirelessController, and secureConnect.
    type: str
  includedEventTypes:
    description:
    - >
      IncludedEventTypes query parameter. A list of event types. The returned events will be filtered to only
      include events with these types.
    elements: str
    type: list
  excludedEventTypes:
    description:
    - >
      ExcludedEventTypes query parameter. A list of event types. The returned events will be filtered to exclude
      events with these types.
    elements: str
    type: list
  deviceMac:
    description:
    - DeviceMac query parameter. The MAC address of the Meraki device which the list of events will be filtered with.
    type: str
  deviceSerial:
    description:
    - DeviceSerial query parameter. The serial of the Meraki device which the list of events will be filtered with.
    type: str
  deviceName:
    description:
    - DeviceName query parameter. The name of the Meraki device which the list of events will be filtered with.
    type: str
  clientIp:
    description:
    - >
      ClientIp query parameter. The IP of the client which the list of events will be filtered with. Only
      supported for track-by-IP networks.
    type: str
  clientMac:
    description:
    - >
      ClientMac query parameter. The MAC address of the client which the list of events will be filtered with.
      Only supported for track-by-MAC networks.
    type: str
  clientName:
    description:
    - >
      ClientName query parameter. The name, or partial name, of the client which the list of events will be
      filtered with.
    type: str
  smDeviceMac:
    description:
    - >
      SmDeviceMac query parameter. The MAC address of the Systems Manager device which the list of events will be
      filtered with.
    type: str
  smDeviceName:
    description:
    - >
      SmDeviceName query parameter. The name of the Systems Manager device which the list of events will be
      filtered with.
    type: str
  eventDetails:
    description:
    - >
      EventDetails query parameter. The details of the event(Catalyst device only) which the list of events will
      be filtered with.
    type: str
  eventSeverity:
    description:
    - >
      EventSeverity query parameter. The severity of the event(Catalyst device only) which the list of events will
      be filtered with.
    type: str
  isCatalyst:
    description:
    - >
      IsCatalyst query parameter. Boolean indicating that whether it is a Catalyst device. For Catalyst device,
      eventDetails and eventSeverity can be used to filter events.
    type: bool
  perPage:
    description:
    - PerPage query parameter. The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
    type: int
  startingAfter:
    description:
    - >
      StartingAfter query parameter. A token used by the server to indicate the start of the page. Often this is a
      timestamp or an ID but it is not limited to those. This parameter should not be defined by client
      applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    type: str
  endingBefore:
    description:
    - >
      EndingBefore query parameter. A token used by the server to indicate the end of the page. Often this is a
      timestamp or an ID but it is not limited to those. This parameter should not be defined by client
      applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for networks getNetworkEvents
    description: Complete reference of the getNetworkEvents API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-events
notes:
  - SDK Method used are
    networks.Networks.get_network_events,

  - Paths used are
    get /networks/{networkId}/events,
"""

EXAMPLES = r"""
- name: Get all networks _events
  cisco.meraki.networks_events_info:
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
    meraki_use_iterator_for_get_pages: "{{ meraki_use_iterator_for_get_pages }}"
    meraki_inherit_logging_config: "{{ meraki_inherit_logging_config }}"
    productType: string
    includedEventTypes: []
    excludedEventTypes: []
    deviceMac: string
    deviceSerial: string
    deviceName: string
    clientIp: string
    clientMac: string
    clientName: string
    smDeviceMac: string
    smDeviceName: string
    eventDetails: string
    eventSeverity: string
    isCatalyst: True
    perPage: 0
    startingAfter: string
    endingBefore: string
    networkId: string
    total_pages: -1
    direction: next
  register: result

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "events": [
        {
          "category": "string",
          "clientDescription": "string",
          "clientId": "string",
          "clientMac": "string",
          "description": "string",
          "deviceName": "string",
          "deviceSerial": "string",
          "eventData": {
            "aid": "string",
            "channel": "string",
            "client_ip": "string",
            "client_mac": "string",
            "radio": "string",
            "rssi": "string",
            "vap": "string"
          },
          "networkId": "string",
          "occurredAt": "string",
          "ssidNumber": 0,
          "type": "string"
        }
      ],
      "message": "string",
      "pageEndAt": "string",
      "pageStartAt": "string"
    }
"""
