#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_recalculate
short_description: Resource module for networks _recalculate
description:
  - Manage operation create of the resource networks _recalculate.
  - Trigger auto locate recalculation for a job, and optionally set anchors.
version_added: '2.20.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  devices:
    description: The list of devices to update anchor positions for.
    elements: dict
    suboptions:
      autoLocate:
        description: The auto locate position for this device.
        suboptions:
          isAnchor:
            description: Whether or not this location should be saved as a user-defined
              anchor.
            type: bool
          lat:
            description: Latitude.
            type: float
          lng:
            description: Longitude.
            type: float
        type: dict
      serial:
        description: Serial for device to update.
        type: str
    type: list
  jobId:
    description: JobId path parameter. Job ID.
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for networks recalculateNetworkFloorPlansAutoLocateJob
    description: Complete reference of the recalculateNetworkFloorPlansAutoLocateJob API.
    link: https://developer.cisco.com/meraki/api-v1/#!recalculate-network-floor-plans-auto-locate-job
notes:
  - SDK Method used are
    networks.Networks.recalculate_network_floor_plans_auto_locate_job,

  - Paths used are
    post /networks/{networkId}/floorPlans/autoLocate/jobs/{jobId}/recalculate,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_recalculate:
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
    meraki_use_iterator_for_get_pages: "{{ meraki_use_iterator_for_get_pages }}"
    meraki_inherit_logging_config: "{{ meraki_inherit_logging_config }}"
    devices:
    - autoLocate:
        isAnchor: true
        lat: 37.4180951010362
        lng: -122.098531723022
      serial: Q234-ABCD-5678
    jobId: string
    networkId: string

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
