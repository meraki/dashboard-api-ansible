#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_nac_certificates_authorities_crls
short_description: Resource module for organizations _nac _certificates _authorities
  _crls
description:
  - Manage operation create of the resource organizations _nac _certificates _authorities
    _crls.
  - Create a new CRL either base or delta for an existing CA.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  caId:
    description: ID of the CRL issuer.
    type: str
  content:
    description: CRL content in PEM format.
    type: str
  isDelta:
    description: Whether it's a delta CRL or not.
    type: bool
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for nac createOrganizationNacCertificatesAuthoritiesCrl
    description: Complete reference of the createOrganizationNacCertificatesAuthoritiesCrl
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-certificates-authorities-crl
notes:
  - SDK Method used are
    nac.Nac.create_organization_nac_certificates_authorities_crl,
  - Paths used are
    post /organizations/{organizationId}/nac/certificates/authorities/crls,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_nac_certificates_authorities_crls:
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
    caId: '12345'
    content: '-----BEGIN X509 CRL----- MIIDFDCCAfwCAQEwDQYJKoZIhvcNAQEFBQAwXzEjMCEGA1UEChMaU2FtcGxlIFNpZ25lciBPcmdhbml6YXRpb24xGzAZBgNVBAsTElNhbXBsZS...
      -----END X509 CRL-----'
    isDelta: false
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "crlId": "string",
      "data": [
        {
          "serial": "string",
          "revocationDate": "string",
          "reason": "string"
        }
      ],
      "isDelta": true,
      "caId": "string",
      "createdAt": "string",
      "lastUpdatedAt": "string"
    }
"""
