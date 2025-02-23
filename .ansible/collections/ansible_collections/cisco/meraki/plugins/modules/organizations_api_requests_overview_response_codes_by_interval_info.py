#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all organizations _api _requests _overview _response _codes _by _interval.
  - Tracks organizations' API requests by response code across a given time period.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: organizations_api_requests_overview_response_codes_by_interval_info
notes:
  - SDK Method used are organizations.Organizations.get_organization_api_requests_overview_response_codes_by_interval,
  - Paths used are get /organizations/{organizationId}/apiRequests/overview/responseCodes/byInterval,
options:
  adminIds:
    description:
      - AdminIds query parameter. Filter by admin ID of user that made the API request.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  interval:
    description:
      - 'Interval query parameter. The time interval in seconds for returned data.
        The valid intervals are 120, 3600, 14400, 21600. The default is 21600. Interval
        is calculated if time params are provided.

        '
    type: int
  operationIds:
    description:
      - OperationIds query parameter. Filter by operation ID of the endpoint.
    elements: str
    type: list
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  sourceIps:
    description:
      - SourceIps query parameter. Filter by source IP that made the API request.
    elements: str
    type: list
  t0:
    description:
      - T0 query parameter. The beginning of the timespan for the data. The maximum
        lookback period is 31 days from today.
    type: str
  t1:
    description:
      - T1 query parameter. The end of the timespan for the data. T1 can be a maximum
        of 31 days after t0.
    type: str
  timespan:
    description:
      - 'Timespan query parameter. The timespan for which the information will be
        fetched. If specifying timespan, do not specify parameters t0 and t1. The
        value must be in seconds and be less than or equal to 31 days. The default
        is 31 days. If interval is provided, the timespan will be autocalculated.

        '
    type: float
  userAgent:
    description:
      - 'UserAgent query parameter. Filter by user agent string for API request. This
        will filter by a complete or partial match.

        '
    type: str
  version:
    description:
      - Version query parameter. Filter by API version of the endpoint. Allowable
        values are 0, 1.
    type: int
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getOrganizationApiRequestsOverviewResponseCodesByInterval
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview-response-codes-by-interval
    name: Cisco Meraki documentation for organizations getOrganizationApiRequestsOverviewResponseCodesByInterval
short_description: Information module for organizations _api _requests _overview _response
  _codes _by _interval
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all organizations _api _requests _overview _response _codes _by _interval
  cisco.meraki.organizations_api_requests_overview_response_codes_by_interval_info:
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
    t0: string
    t1: string
    timespan: 0
    interval: 0
    version: 0
    operationIds: []
    sourceIps: []
    adminIds: []
    userAgent: string
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
        "counts": [
          {
            "code": 0,
            "count": 0
          }
        ],
        "endTs": "string",
        "startTs": "string"
      }
    ]
"""
