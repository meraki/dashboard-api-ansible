#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_location_scanning_receivers
short_description: Resource module for organizations _wireless _location _scanning
  _receivers
description:
  - Manage operations create, update and delete of the resource organizations _wireless
    _location _scanning _receivers.
  - Add new receiver for scanning API.
  - Delete a scanning API receiver.
  - Change scanning API receiver settings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  network:
    description: Add scanning API receiver for network.
    suboptions:
      id:
        description: Network ID.
        type: str
    type: dict
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  radio:
    description: Add scanning API Radio.
    suboptions:
      type:
        description: Radio Type whether WiFi or Bluetooth.
        type: str
    type: dict
  receiverId:
    description: ReceiverId path parameter. Receiver ID.
    type: str
  sharedSecret:
    description: Secret Value for Receiver.
    type: str
  url:
    description: Receiver Url.
    type: str
  version:
    description: Scanning API Version.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless createOrganizationWirelessLocationScanningReceiver
    description: Complete reference of the createOrganizationWirelessLocationScanningReceiver
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-location-scanning-receiver
  - name: Cisco Meraki documentation for wireless deleteOrganizationWirelessLocationScanningReceiver
    description: Complete reference of the deleteOrganizationWirelessLocationScanningReceiver
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-location-scanning-receiver
  - name: Cisco Meraki documentation for wireless updateOrganizationWirelessLocationScanningReceiver
    description: Complete reference of the updateOrganizationWirelessLocationScanningReceiver
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-location-scanning-receiver
notes:
  - SDK Method used are
    wireless.Wireless.create_organization_wireless_location_scanning_receiver,
    wireless.Wireless.delete_organization_wireless_location_scanning_receiver,
    wireless.Wireless.update_organization_wireless_location_scanning_receiver,
  - Paths used are
    post /organizations/{organizationId}/wireless/location/scanning/receivers,
    delete /organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId},
    put /organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_wireless_location_scanning_receivers:
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
    network:
      id: L_1234
    organizationId: string
    radio:
      type: Wi-Fi
    sharedSecret: mysecretvalue
    url: https://www.myreceiver.com
    version: '3'
- name: Update by id
  cisco.meraki.organizations_wireless_location_scanning_receivers:
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
    organizationId: string
    radio:
      type: Wi-Fi
    receiverId: string
    url: https://www.myreceiver.com
    version: '3'
- name: Delete by id
  cisco.meraki.organizations_wireless_location_scanning_receivers:
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
    state: absent
    organizationId: string
    receiverId: string
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
      "receiverId": "string",
      "url": "string",
      "version": "string",
      "radio": {
        "type": "string"
      }
    }
"""
