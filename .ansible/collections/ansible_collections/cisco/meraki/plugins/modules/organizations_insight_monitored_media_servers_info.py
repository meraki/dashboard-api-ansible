#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all organizations _insight _monitored _media _servers.
  - Get organizations _insight _monitored _media _servers by id.
  - List the monitored media servers for this organization. Only valid for organizations
    with Meraki Insight.
  - Return a monitored media server for this organization. Only valid for organizations
    with Meraki Insight.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: organizations_insight_monitored_media_servers_info
notes:
  - SDK Method used are insight.Insight.get_organization_insight_monitored_media_server,
    insight.Insight.get_organization_insight_monitored_media_servers,
  - Paths used are get /organizations/{organizationId}/insight/monitoredMediaServers,
    get /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId},
options:
  headers:
    description: Additional headers.
    type: dict
  monitoredMediaServerId:
    description:
      - MonitoredMediaServerId path parameter. Monitored media server ID.
    type: str
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getOrganizationInsightMonitoredMediaServer
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-server
    name: Cisco Meraki documentation for insight getOrganizationInsightMonitoredMediaServer
  - description: Complete reference of the getOrganizationInsightMonitoredMediaServers
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-servers
    name: Cisco Meraki documentation for insight getOrganizationInsightMonitoredMediaServers
short_description: Information module for organizations _insight _monitored _media
  _servers
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all organizations _insight _monitored _media _servers
  cisco.meraki.organizations_insight_monitored_media_servers_info:
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
    organizationId: string
  register: result
- name: Get organizations _insight _monitored _media _servers by id
  cisco.meraki.organizations_insight_monitored_media_servers_info:
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
    organizationId: string
    monitoredMediaServerId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "address": "string",
      "bestEffortMonitoringEnabled": true,
      "id": "string",
      "name": "string"
    }
"""
