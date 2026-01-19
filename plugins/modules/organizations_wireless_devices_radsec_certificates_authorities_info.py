#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_devices_radsec_certificates_authorities_info
short_description: Information module for organizations _wireless _devices _radsec
  _certificates _authorities
description:
  - Information module for Organizations Wireless Devices Radsec Certificates Authorities Info.
  - Get all organizations _wireless _devices _radsec _certificates _authorities.
  - >
    Query for details on the organization's RADSEC device Certificate Authority certificates
    CAs. The primary CA signs all the certificates that devices present when establishing
    a secure connection to RADIUS servers via RADSEC protocol. This API returns an
    array of the status of all of the CAs as well as their contents, if they've been
    generated. An organization will have at most one CA unless the CA is being rotated.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
      - Information module for Organizations Wireless Devices Radsec Certificates Authorities Info.
      - OrganizationId path parameter. Organization ID.
    type: str
  certificateAuthorityIds:
    description:
      - Information module for Organizations Wireless Devices Radsec Certificates Authorities Info.
      - >
        CertificateAuthorityIds query parameter. Optional parameter to filter CAs
        by one or more CA IDs. All returned CAs will have an ID that is an exact match.
    elements: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getOrganizationWirelessDevicesRadsecCertificatesAuthorities
    description: Complete reference of the getOrganizationWirelessDevicesRadsecCertificatesAuthorities
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities
notes:
  - SDK Method used are
    wireless.Wireless.get_organization_wireless_devices_radsec_certificates_authorities,
  - Paths used are
    get /organizations/{organizationId}/wireless/devices/radsec/certificates/authorities,
"""

EXAMPLES = r"""
- name: Get all organizations _wireless _devices _radsec _certificates _authorities
  cisco.meraki.organizations_wireless_devices_radsec_certificates_authorities_info:
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
    certificateAuthorityIds: []
    organizationId: string
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
        "items": [
          {
            "certificateAuthorityId": "string",
            "status": "string",
            "contents": "string"
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
    ]
"""
