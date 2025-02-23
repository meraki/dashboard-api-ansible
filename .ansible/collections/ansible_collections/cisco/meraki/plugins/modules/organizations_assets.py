#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource organizations _assets.
  - Create a Splash Theme Asset.
extends_documentation_fragment:
  - cisco.meraki.module
module: organizations_assets
notes:
  - SDK Method used are organizations.Organizations.create_organization_splash_theme_asset,
  - Paths used are post /organizations/{organizationId}/splash/themes/{themeIdentifier}/assets,
options:
  content:
    description: A file containing the asset content.
    type: str
  name:
    description: File name. Will overwrite files with same name.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  themeIdentifier:
    description: ThemeIdentifier path parameter. Theme identifier.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the createOrganizationSplashThemeAsset API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme-asset
    name: Cisco Meraki documentation for organizations createOrganizationSplashThemeAsset
short_description: Resource module for organizations _assets
version_added: 2.20.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_assets:
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
    content: string
    name: string
    organizationId: string
    themeIdentifier: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "fileData": "string",
      "id": "string",
      "name": "string"
    }
"""
