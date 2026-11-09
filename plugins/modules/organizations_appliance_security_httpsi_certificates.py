#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_appliance_security_httpsi_certificates
short_description: Resource module for organizations _appliance _security _httpsi
  _certificates
description:
  - Manage operation create of the resource organizations _appliance _security _httpsi
    _certificates.
  - Upload an HTTPS Inspection certificate to MX devices in the same organization.
    HTTPS Inspection must be supported.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  contents:
    description: The private key and certificate used to inspect HTTPS traffic. The
      certificate must be in .pem format.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  serials:
    description: Serial numbers of the security appliances that will receive the new
      HTTPS certificate for HTTPS Inspection.
    elements: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for appliance certificatesOrganizationApplianceSecurityHttpsi
    description: Complete reference of the certificatesOrganizationApplianceSecurityHttpsi
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!certificates-organization-appliance-security-httpsi
notes:
  - SDK Method used are
    appliance.Appliance.certificates_organization_appliance_security_httpsi,
  - Paths used are
    post /organizations/{organizationId}/appliance/security/httpsi/certificates,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_appliance_security_httpsi_certificates:
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
    contents: '---BEGIN PRIVATE KEY--- #magic___^_^___line hello world #magic___^_^___line
      ---END PRIVATE KEY--- #magic___^_^___line ---BEGIN CERTIFICATE--- #magic___^_^___line
      hello world #magic___^_^___line ---END CERTIFICATE--- #magic___^_^___line '
    organizationId: string
    serials:
      - Q234-ABCD-0001
      - Q234-ABCD-0002
      - Q234-ABCD-0003
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "success": true
    }
"""
