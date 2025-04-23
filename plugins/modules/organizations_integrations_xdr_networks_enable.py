#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_integrations_xdr_networks_enable
short_description: Resource module for organizations _integrations _xdr _networks _enable
description:
  - Manage operation create of the resource organizations _integrations _xdr _networks _enable.
  - Enable XDR on networks.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  networks:
    description: List containing the network ID and the product type to enable XDR on.
    elements: dict
    suboptions:
      networkId:
        description: Network ID.
        type: str
      productTypes:
        description: List of products for which to enable XDR.
        elements: str
        type: list
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations enableOrganizationIntegrationsXdrNetworks
    description: Complete reference of the enableOrganizationIntegrationsXdrNetworks API.
    link: https://developer.cisco.com/meraki/api-v1/#!enable-organization-integrations-xdr-networks
notes:
  - SDK Method used are
    organizations.Organizations.enable_organization_integrations_xdr_networks,
  - Paths used are
    post /organizations/{organizationId}/integrations/xdr/networks/enable,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_integrations_xdr_networks_enable:
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
    networks:
      - networkId: N_1234567
        productTypes:
          - appliance
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "networks": [
        {
          "enabled": true,
          "isEligible": true,
          "name": "string",
          "networkId": "string",
          "productTypes": [
            "string"
          ]
        }
      ]
    }
"""
