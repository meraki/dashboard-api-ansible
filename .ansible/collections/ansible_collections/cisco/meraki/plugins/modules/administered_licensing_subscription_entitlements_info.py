#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all administered _licensing _subscription _entitlements.
  - Retrieve the list of purchasable entitlements.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: administered_licensing_subscription_entitlements_info
notes:
  - SDK Method used are licensing.Licensing.get_administered_licensing_subscription_entitlements,
  - Paths used are get /administered/licensing/subscription/entitlements,
options:
  headers:
    description: Additional headers.
    type: dict
  skus:
    description:
      - Skus query parameter. Filter to entitlements with the specified SKUs.
    elements: str
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getAdministeredLicensingSubscriptionEntitlements
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-administered-licensing-subscription-entitlements
    name: Cisco Meraki documentation for licensing getAdministeredLicensingSubscriptionEntitlements
short_description: Information module for administered _licensing _subscription _entitlements
version_added: 2.18.0
"""

EXAMPLES = r"""
- name: Get all administered _licensing _subscription _entitlements
  cisco.meraki.administered_licensing_subscription_entitlements_info:
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
    skus: []
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "featureTier": "string",
      "isAddOn": true,
      "name": "string",
      "productClass": "string",
      "productType": "string",
      "sku": "string"
    }
"""
