#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all devices.
  - Get devices by id.
  - List the devices in an organization that have been assigned to a network.
  - Return a single device.
  - Returns a historical log of all commands.
  - Returns information about the command's execution, including the status.
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
module: devices_info
notes:
  - SDK Method used are devices.Devices.get_device_sensor_command, devices.Devices.get_organization_devices,
  - Paths used are get /devices/{serial}, get /devices/{serial}/sensor/commands, get
    /devices/{serial}/sensor/commands/{commandId}, get /organizations/{organizationId}/devices,
options:
  commandId:
    description:
      - CommandId path parameter. Command ID.
    type: str
  configurationUpdatedAfter:
    description:
      - 'ConfigurationUpdatedAfter query parameter. Filter results by whether or not
        the device''s configuration has been updated after the given timestamp.

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
      - 'Mac query parameter. Optional parameter to filter devices by MAC address.
        All returned devices will have a MAC address that contains the search term
        or is an exact match.

        '
    type: str
  macs:
    description:
      - 'Macs query parameter. Optional parameter to filter devices by one or more
        MAC addresses. All returned devices will have a MAC address that is an exact
        match.

        '
    elements: str
    type: list
  model:
    description:
      - 'Model query parameter. Optional parameter to filter devices by model. All
        returned devices will have a model that contains the search term or is an
        exact match.

        '
    type: str
  models:
    description:
      - 'Models query parameter. Optional parameter to filter devices by one or more
        models. All returned devices will have a model that is an exact match.

        '
    elements: str
    type: list
  name:
    description:
      - 'Name query parameter. Optional parameter to filter devices by name. All returned
        devices will have a name that contains the search term or is an exact match.

        '
    type: str
  networkIds:
    description:
      - NetworkIds query parameter. Optional parameter to filter devices by network.
    elements: str
    type: list
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 1000.
    type: int
  productTypes:
    description:
      - 'ProductTypes query parameter. Optional parameter to filter devices by product
        type. Valid types are wireless, appliance, switch, systemsManager, camera,
        cellularGateway, sensor, wirelessController, and secureConnect.

        '
    elements: str
    type: list
  sensorAlertProfileIds:
    description:
      - 'SensorAlertProfileIds query parameter. Optional parameter to filter devices
        by the alert profiles that are bound to them. Only applies to sensor devices.

        '
    elements: str
    type: list
  sensorMetrics:
    description:
      - 'SensorMetrics query parameter. Optional parameter to filter devices by the
        metrics that they provide. Only applies to sensor devices.

        '
    elements: str
    type: list
  serial:
    description:
      - Serial path parameter.
    type: str
  serials:
    description:
      - 'Serials query parameter. Optional parameter to filter devices by one or more
        serial numbers. All returned devices will have a serial number that is an
        exact match.

        '
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
  tags:
    description:
      - Tags query parameter. Optional parameter to filter devices by tags.
    elements: str
    type: list
  tagsFilterType:
    description:
      - 'TagsFilterType query parameter. Optional parameter of value ''withAnyTags''
        or ''withAllTags'' to indicate whether to return networks which contain ANY
        or ALL of the included tags. If no type is included, ''withAnyTags'' will
        be selected.

        '
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getDevice API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device
    name: Cisco Meraki documentation for devices getDevice
  - description: Complete reference of the getDeviceSensorCommand API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-command
    name: Cisco Meraki documentation for devices getDeviceSensorCommand
  - description: Complete reference of the getDeviceSensorCommands API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-commands
    name: Cisco Meraki documentation for devices getDeviceSensorCommands
  - description: Complete reference of the getOrganizationDevices API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-devices
    name: Cisco Meraki documentation for devices getOrganizationDevices
short_description: Information module for devices
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all devices
  cisco.meraki.devices_info:
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
    perPage: 0
    startingAfter: string
    endingBefore: string
    configurationUpdatedAfter: string
    networkIds: []
    productTypes: []
    tags: []
    tagsFilterType: string
    name: string
    mac: string
    serial: string
    model: string
    macs: []
    serials: []
    sensorMetrics: []
    sensorAlertProfileIds: []
    models: []
    organizationId: string
    total_pages: -1
    direction: next
  register: result
- name: Get devices by id
  cisco.meraki.devices_info:
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
    serial: string
    commandId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "commandId": "string",
      "completedAt": "string",
      "createdAt": "string",
      "createdBy": {
        "adminId": "string",
        "email": "string",
        "name": "string"
      },
      "errors": [
        "string"
      ],
      "operation": "string",
      "status": "string"
    }
"""
