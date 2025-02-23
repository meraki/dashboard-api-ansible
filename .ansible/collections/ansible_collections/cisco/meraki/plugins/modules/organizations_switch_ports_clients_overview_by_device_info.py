#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all organizations _switch _ports _clients _overview _by _device.
  - List the number of clients for all switchports with at least one online client
    in an organization.
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
module: organizations_switch_ports_clients_overview_by_device_info
notes:
  - SDK Method used are switch.Switch.get_organization_switch_ports_clients_overview_by_device,
  - Paths used are get /organizations/{organizationId}/switch/ports/clients/overview/byDevice,
options:
  configurationUpdatedAfter:
    description:
      - 'ConfigurationUpdatedAfter query parameter. Optional parameter to filter items
        to switches where the configuration has been updated after the given timestamp.

        '
    type: str
  endingBefore:
    description:
      - 'EndingBefore query parameter. A token used by the server to indicate the
        end of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.

        '
    type: str
  headers:
    description: Additional headers.
    type: dict
  mac:
    description:
      - 'Mac query parameter. Optional parameter to filter items to switches with
        MAC addresses that contain the search term or are an exact match.

        '
    type: str
  macs:
    description:
      - Macs query parameter. Optional parameter to filter items to switches that
        have one of the provided MAC addresses.
    elements: str
    type: list
  name:
    description:
      - 'Name query parameter. Optional parameter to filter items to switches with
        names that contain the search term or are an exact match.

        '
    type: str
  networkIds:
    description:
      - NetworkIds query parameter. Optional parameter to filter items to switches
        in one of the provided networks.
    elements: str
    type: list
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 20. Default is 20.
    type: int
  portProfileIds:
    description:
      - 'PortProfileIds query parameter. Optional parameter to filter items to switches
        that contain switchports belonging to one of the specified port profiles.

        '
    elements: str
    type: list
  serial:
    description:
      - 'Serial query parameter. Optional parameter to filter items to switches with
        serial number that contains the search term or are an exact match.

        '
    type: str
  serials:
    description:
      - Serials query parameter. Optional parameter to filter items to switches that
        have one of the provided serials.
    elements: str
    type: list
  startingAfter:
    description:
      - 'StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.

        '
    type: str
  t0:
    description:
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 31 days from today.
    type: str
  timespan:
    description:
      - 'Timespan query parameter. The timespan for which the information will be
        fetched. If specifying timespan, do not specify parameter t0. The value must
        be in seconds and be less than or equal to 31 days. The default is 1 day.

        '
    type: float
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getOrganizationSwitchPortsClientsOverviewByDevice
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-clients-overview-by-device
    name: Cisco Meraki documentation for switch getOrganizationSwitchPortsClientsOverviewByDevice
short_description: Information module for organizations _switch _ports _clients _overview
  _by _device
version_added: 2.20.0
"""

EXAMPLES = r"""
- name: Get all organizations _switch _ports _clients _overview _by _device
  cisco.meraki.organizations_switch_ports_clients_overview_by_device_info:
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
    t0: string
    timespan: 0
    perPage: 0
    startingAfter: string
    endingBefore: string
    configurationUpdatedAfter: string
    mac: string
    macs: []
    name: string
    networkIds: []
    portProfileIds: []
    serial: string
    serials: []
    organizationId: string
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
      "items": [
        {
          "mac": "string",
          "model": "string",
          "name": "string",
          "network": {
            "id": "string",
            "name": "string"
          },
          "ports": [
            {
              "counts": {
                "byStatus": {
                  "online": 0
                }
              },
              "portId": "string"
            }
          ],
          "serial": "string"
        }
      ],
      "meta": {
        "counts": {
          "items": {
            "remaining": 0,
            "total": 0
          }
        }
      }
    }
"""
