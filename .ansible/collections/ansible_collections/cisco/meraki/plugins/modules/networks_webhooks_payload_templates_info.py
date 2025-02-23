#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all networks _webhooks _payload _templates.
  - Get networks _webhooks _payload _templates by id.
  - Get the webhook payload template for a network.
  - List the webhook payload templates for a network.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: networks_webhooks_payload_templates_info
notes:
  - SDK Method used are networks.Networks.get_network_webhooks_payload_template, networks.Networks.get_network_webhooks_payload_templates,
  - Paths used are get /networks/{networkId}/webhooks/payloadTemplates, get /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId},
options:
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
      - NetworkId path parameter. Network ID.
    type: str
  payloadTemplateId:
    description:
      - PayloadTemplateId path parameter. Payload template ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getNetworkWebhooksPayloadTemplate API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-template
    name: Cisco Meraki documentation for networks getNetworkWebhooksPayloadTemplate
  - description: Complete reference of the getNetworkWebhooksPayloadTemplates API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-templates
    name: Cisco Meraki documentation for networks getNetworkWebhooksPayloadTemplates
short_description: Information module for networks _webhooks _payload _templates
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all networks _webhooks _payload _templates
  cisco.meraki.networks_webhooks_payload_templates_info:
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
    networkId: string
  register: result
- name: Get networks _webhooks _payload _templates by id
  cisco.meraki.networks_webhooks_payload_templates_info:
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
    networkId: string
    payloadTemplateId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "body": "string",
      "headers": [
        {
          "name": "string",
          "template": "string"
        }
      ],
      "name": "string",
      "payloadTemplateId": "string",
      "sharing": {
        "byNetwork": {
          "adminsCanModify": true
        }
      },
      "type": "string"
    }
"""
