#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_sase_sites
short_description: Resource module for organizations _sase _sites
description:
  - Manage operation update of the resource organizations _sase _sites.
  - Update the configuration for a site. Currently, only supports updating default
    route enablement.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  routing:
    description: Routing configuration for the site.
    suboptions:
      defaultRoute:
        description: Default route configuration for the site.
        suboptions:
          enabled:
            description: Whether the site has default route enabled.
            type: bool
        type: dict
    type: dict
  siteId:
    description: Site ID of the site to update.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations updateOrganizationSaseSite
    description: Complete reference of the updateOrganizationSaseSite API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-sase-site
notes:
  - SDK Method used are
    organizations.Organizations.update_organization_sase_site,
  - Paths used are
    put /organizations/{organizationId}/sase/sites/{siteId},
"""

EXAMPLES = r"""
- name: Update by id
  cisco.meraki.organizations_sase_sites:
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
    routing:
      defaultRoute:
        enabled: true
    siteId: '1234'
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "siteId": "string",
      "network": {
        "id": "string"
      },
      "type": "string",
      "name": "string",
      "region": {
        "slug": "string"
      },
      "model": "string",
      "address": {
        "street": "string"
      },
      "vpn": {
        "type": "string"
      },
      "routing": {
        "defaultRoute": {
          "enabled": true
        }
      }
    }
"""
