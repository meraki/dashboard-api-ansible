#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: networks_clients_info
short_description: Information module for networks _clients
description:
  - Information module for Networks Clients Info.
  - Get all networks _clients.
  - Get networks _clients by id.
  - List the clients that have used this network in the timespan. The data is updated
    at most once every five minutes.
  - >
    Return the client associated with the given identifier. Clients can be identified
    by a client key or either the MAC or IP depending on whether the network uses
    Track-by-IP.
version_added: '1.0.0'
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
  - Information module for Networks Clients Info.
      - NetworkId path parameter. Network ID.
    type: str
  t0:
    description:
  - Information module for Networks Clients Info.
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 31 days from today.
    type: str
  timespan:
    description:
  - Information module for Networks Clients Info.
      - >
        Timespan query parameter. The timespan for which the information will be fetched.
        If specifying timespan, do not specify parameter t0. The value must be in
        seconds and be less than or equal to 31 days. The default is 1 day.
    type: float
  perPage:
    description:
  - Information module for Networks Clients Info.
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 5000. Default is 10.
    type: int
  startingAfter:
    description:
  - Information module for Networks Clients Info.
      - >
        StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.
    type: str
  endingBefore:
    description:
  - Information module for Networks Clients Info.
      - >
        EndingBefore query parameter. A token used by the server to indicate the end
        of the page. Often this is a timestamp or an ID but it is not limited to those.
        This parameter should not be defined by client applications. The link for
        the first, last, prev, or next page in the HTTP Link header should define
        it.
    type: str
  statuses:
    description:
  - Information module for Networks Clients Info.
      - Statuses query parameter. Filters clients based on status. Can be one of 'Online'
        or 'Offline'.
    elements: str
    type: list
  ip:
    description:
  - Information module for Networks Clients Info.
      - Ip query parameter. Filters clients based on a partial or full match for the
        ip address field.
    type: str
  ip6:
    description:
  - Information module for Networks Clients Info.
      - Ip6 query parameter. Filters clients based on a partial or full match for
        the ip6 address field.
    type: str
  ip6Local:
    description:
  - Information module for Networks Clients Info.
      - Ip6Local query parameter. Filters clients based on a partial or full match
        for the ip6Local address field.
    type: str
  mac:
    description:
  - Information module for Networks Clients Info.
      - Mac query parameter. Filters clients based on a partial or full match for
        the mac address field.
    type: str
  os:
    description:
  - Information module for Networks Clients Info.
      - Os query parameter. Filters clients based on a partial or full match for the
        os (operating system) field.
    type: str
  pskGroup:
    description:
  - Information module for Networks Clients Info.
      - PskGroup query parameter. Filters clients based on partial or full match for
        the iPSK name field.
    type: str
  description:
  - Information module for Networks Clients Info.
    description:
  - Information module for Networks Clients Info.
      - Description query parameter. Filters clients based on a partial or full match
        for the description field.
    type: str
  vlan:
    description:
  - Information module for Networks Clients Info.
      - Vlan query parameter. Filters clients based on the full match for the VLAN
        field.
    type: str
  namedVlan:
    description:
  - Information module for Networks Clients Info.
      - NamedVlan query parameter. Filters clients based on the partial or full match
        for the named VLAN field.
    type: str
  recentDeviceConnections:
    description:
  - Information module for Networks Clients Info.
      - >
        RecentDeviceConnections query parameter. Filters clients based on recent connection
        type. Can be one of 'Wired' or 'Wireless'.
    elements: str
    type: list
  clientId:
    description:
  - Information module for Networks Clients Info.
      - ClientId path parameter. Client ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for networks getNetworkClient
    description: Complete reference of the getNetworkClient API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-client
  - name: Cisco Meraki documentation for networks getNetworkClients
    description: Complete reference of the getNetworkClients API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-clients
notes:
  - SDK Method used are
    networks.Networks.get_network_client,
    networks.Networks.get_network_clients,
  - Paths used are
    get /networks/{networkId}/clients,
    get /networks/{networkId}/clients/{clientId},
"""

EXAMPLES = r"""
- name: Get all networks _clients
  cisco.meraki.networks_clients_info:
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
    t0: string
    timespan: 0
    perPage: 0
    startingAfter: string
    endingBefore: string
    statuses: []
    ip: string
    ip6: string
    ip6Local: string
    mac: string
    os: string
    pskGroup: string
    description: string
    vlan: string
    namedVlan: string
    recentDeviceConnections: []
    networkId: string
    total_pages: -1
    direction: next
  register: result
- name: Get networks _clients by id
  cisco.meraki.networks_clients_info:
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
    clientId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "mac": "string",
      "ip": "string",
      "ip6": "string",
      "ip6Local": "string",
      "description": "string",
      "firstSeen": 0,
      "lastSeen": 0,
      "manufacturer": "string",
      "os": "string",
      "user": "string",
      "vlan": "string",
      "namedVlan": "string",
      "ssid": "string",
      "switchport": "string",
      "wirelessCapabilities": "string",
      "smInstalled": true,
      "recentDeviceMac": "string",
      "recentDeviceName": "string",
      "recentDeviceSerial": "string",
      "recentDeviceConnection": "string",
      "clientVpnConnections": [
        {
          "remoteIp": "string",
          "connectedAt": 0,
          "disconnectedAt": 0
        }
      ],
      "lldp": [
        [
          "string"
        ]
      ],
      "cdp": [
        [
          "string"
        ]
      ],
      "status": "string",
      "notes": "string",
      "deviceTypePrediction": "string"
    }
"""
