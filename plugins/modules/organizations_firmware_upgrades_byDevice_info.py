#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_firmware_upgrades_byDevice_info
short_description: Information module for organizations _firmware _upgrades _bydevice
description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
  - Get all organizations _firmware _upgrades _bydevice.
  - >
    Get firmware upgrade status for the filtered devices. This endpoint currently
    only supports Meraki switches and access points.
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
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - OrganizationId path parameter. Organization ID.
    type: str
  perPage:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 50.
    type: int
  startingAfter:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - >
        StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.
    type: str
  endingBefore:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - >
        EndingBefore query parameter. A token used by the server to indicate the end
        of the page. Often this is a timestamp or an ID but it is not limited to those.
        This parameter should not be defined by client applications. The link for
        the first, last, prev, or next page in the HTTP Link header should define
        it.
    type: str
  networkIds:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - NetworkIds query parameter. Optional parameter to filter by network.
    elements: str
    type: list
  serials:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - >
        Serials query parameter. Optional parameter to filter by serial number. All
        returned devices will have a serial number that is an exact match.
    elements: str
    type: list
  macs:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - >
        Macs query parameter. Optional parameter to filter by one or more MAC addresses
        belonging to devices. All devices returned belong to MAC addresses that are
        an exact match.
    elements: str
    type: list
  firmwareUpgradeBatchIds:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - FirmwareUpgradeBatchIds query parameter. Optional parameter to filter by firmware
        upgrade batch ids.
    elements: str
    type: list
  upgradeStatuses:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - UpgradeStatuses query parameter. Optional parameter to filter by firmware
        upgrade statuses.
    elements: str
    type: list
  currentUpgradesOnly:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - CurrentUpgradesOnly query parameter. Optional parameter to filter to only
        current or pending upgrade statuses.
    type: bool
  limitPerDevice:
    description:
  - Information module for Organizations Firmware Upgrades Bydevice Info.
      - >
        LimitPerDevice query parameter. Optional parameter to limit the number of
        upgrade statuses returned per device. If omitted, a value of 5 is used.
    type: int
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations getOrganizationFirmwareUpgradesByDevice
    description: Complete reference of the getOrganizationFirmwareUpgradesByDevice
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades-by-device
notes:
  - SDK Method used are
    organizations.Organizations.get_organization_firmware_upgrades_by_device,
  - Paths used are
    get /organizations/{organizationId}/firmware/upgrades/byDevice,
"""

EXAMPLES = r"""
- name: Get all organizations _firmware _upgrades _bydevice
  cisco.meraki.organizations_firmware_upgrades_by_device_info:
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
    serials: []
    macs: []
    firmwareUpgradeBatchIds: []
    upgradeStatuses: []
    currentUpgradesOnly: True
    limitPerDevice: 0
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
        "serial": "string",
        "name": "string",
        "deviceStatus": "string",
        "checkinFinishedAt": {},
        "checkinStartedAt": {},
        "detailedStatus": {},
        "downloadFinishedAt": {},
        "downloadStartedAt": {},
        "downloadStatus": {},
        "installFinishedAt": {},
        "installStartedAt": {},
        "installStatus": {},
        "verifyFinishedAt": {},
        "verifyStartedAt": {},
        "verifyStatus": {},
        "upgrade": {
          "time": "string",
          "fromVersion": {
            "id": "string",
            "shortName": "string",
            "releaseDate": "string"
          },
          "toVersion": {
            "id": "string",
            "shortName": "string",
            "releaseDate": "string"
          },
          "status": "string",
          "id": "string",
          "upgradeBatchId": "string",
          "staged": {
            "group": {
              "id": "string"
            }
          }
        }
      }
    ]
"""
