#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_devices_radsec_certificates_authorities
short_description: Resource module for organizations _wireless _devices _radsec _certificates
  _authorities
description:
  - Manage operations create and update of the resource organizations _wireless _devices
    _radsec _certificates _authorities.
  - >
    Create an organization's RADSEC device Certificate Authority CA. Call this endpoint
    when turning on RADSEC in the firmware for the first time. Calling this endpoint
    starts an asynchronous process to generate the CA; call GET afterwards to retrieve
    the contents of the CA. Note this CA is generated and controlled by Meraki. Subsequent
    calls will not generate a new CA.
  - >
    Update an organization's RADSEC device Certificate Authority CA state. Note this
    CA is generated and controlled by Meraki. Call this endpoint to update the state
    to "trusted", at which point Meraki will generate device certificates. "trusted"
    means the CA is placed on your RADSEC servers and devices establishing a secure
    connection using certs signed by this CA will pass verification.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  certificateAuthorityId:
    description: The ID of the Certificate Authority to update.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  status:
    description: The "status" to update the Certificate Authority to. Only valid option
      is "trusted".
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless createOrganizationWirelessDevicesRadsecCertificatesAuthority
    description: Complete reference of the createOrganizationWirelessDevicesRadsecCertificatesAuthority
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-devices-radsec-certificates-authority
  - name: Cisco Meraki documentation for wireless updateOrganizationWirelessDevicesRadsecCertificatesAuthorities
    description: Complete reference of the updateOrganizationWirelessDevicesRadsecCertificatesAuthorities
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-devices-radsec-certificates-authorities
notes:
  - SDK Method used are
    wireless.Wireless.create_organization_wireless_devices_radsec_certificates_authority,
    wireless.Wireless.update_organization_wireless_devices_radsec_certificates_authorities,
  - Paths used are
    post /organizations/{organizationId}/wireless/devices/radsec/certificates/authorities,
    put /organizations/{organizationId}/wireless/devices/radsec/certificates/authorities,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.organizations_wireless_devices_radsec_certificates_authorities:
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
    certificateAuthorityId: '1234'
    organizationId: string
    status: trusted
- name: Create
  cisco.meraki.organizations_wireless_devices_radsec_certificates_authorities:
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
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "certificateAuthorityId": "string",
      "status": "string",
      "contents": "string"
    }
"""
