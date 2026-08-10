#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_devices_cellular_data_devices_info
short_description: Information module for organizations _devices _cellular _data _devices
description:
  - Get all organizations _devices _cellular _data _devices. - > List devices eligible
    for Cellular Data Management profile assignment in this organization. Returns
    paginated device assignment candidates with current profile, software version,
    modem, and SIM details. Supports filtering by device serials, profile IDs, device
    types, and supported SIM slots.
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
      - OrganizationId path parameter. Organization ID.
    type: str
  includeAssigned:
    description:
      - >
        IncludeAssigned query parameter. Whether to include devices that have already
        been assigned to a Cellular Data Management Profile.
    type: bool
  includedSerials:
    description:
      - >
        IncludedSerials query parameter. List of device serials to force-include in
        the response when the devices would otherwise be filtered out. This override
        is primarily useful for keeping selected devices visible while paging through
        results. Maximum 1000 serials.
    elements: str
    type: list
  excludedSerials:
    description:
      - >
        ExcludedSerials query parameter. List of device serials to force-exclude from
        the response when the devices would otherwise be returned. This override is
        primarily useful for hiding selected devices while paging through results.
        Maximum 1000 serials.
    elements: str
    type: list
  includedProfileIds:
    description:
      - >
        IncludedProfileIds query parameter. List of Cellular Data Management Profile
        IDs to include in the results. Maximum 1000 profile IDs.
    elements: str
    type: list
  excludedProfileIds:
    description:
      - >
        ExcludedProfileIds query parameter. List of Cellular Data Management Profile
        IDs to exclude from the results. Maximum 1000 profile IDs.
    elements: str
    type: list
  deviceTypes:
    description:
      - DeviceTypes query parameter. List of device types to filter by. Maximum 1000
        device types.
    elements: str
    type: list
  slots:
    description:
      - >
        Slots query parameter. List of SIM slot types that devices must support. Accepted
        values are sim1, sim2, and esim. Maximum 3 slots.
    elements: str
    type: list
  name:
    description:
      - Name query parameter. Name of the device to filter by (partial matches allowed).
    type: str
  serials:
    description:
      - Serials query parameter. List of device serials to filter by. Maximum 1000
        serials.
    elements: str
    type: list
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 100.
    type: int
  startingAfter:
    description:
      - >
        StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.
    type: str
  endingBefore:
    description:
      - >
        EndingBefore query parameter. A token used by the server to indicate the end
        of the page. Often this is a timestamp or an ID but it is not limited to those.
        This parameter should not be defined by client applications. The link for
        the first, last, prev, or next page in the HTTP Link header should define
        it.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations getOrganizationDevicesCellularDataDevices
    description: Complete reference of the getOrganizationDevicesCellularDataDevices
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-cellular-data-devices
notes:
  - SDK Method used are
    organizations.Organizations.get_organization_devices_cellular_data_devices,
  - Paths used are
    get /organizations/{organizationId}/devices/cellular/data/devices,
"""

EXAMPLES = r"""
- name: Get all organizations _devices _cellular _data _devices
  cisco.meraki.organizations_devices_cellular_data_devices_info:
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
    includeAssigned: true
    includedSerials: []
    excludedSerials: []
    includedProfileIds: []
    excludedProfileIds: []
    deviceTypes: []
    slots: []
    name: string
    serials: []
    perPage: 0
    startingAfter: string
    endingBefore: string
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
          "serial": "string",
          "name": "string",
          "url": "string",
          "model": "string",
          "software": {
            "currentVersion": {
              "shortName": "string"
            }
          },
          "modems": [
            {
              "index": 0,
              "sims": [
                {
                  "slot": "string",
                  "type": "string",
                  "active": true
                }
              ]
            }
          ],
          "profile": {
            "assigned": true,
            "id": {},
            "name": {}
          },
          "network": {
            "name": "string",
            "id": "string"
          }
        }
      ],
      "meta": {
        "counts": {
          "items": {
            "total": 0,
            "remaining": 0
          }
        }
      }
    }
"""
