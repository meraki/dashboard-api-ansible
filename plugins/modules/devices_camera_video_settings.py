#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource devices _camera _video _settings.
  - Update video settings for the given camera.
extends_documentation_fragment:
  - cisco.meraki.module
module: devices_camera_video_settings
notes:
  - SDK Method used are camera.Camera.update_device_camera_video_settings,
  - Paths used are put /devices/{serial}/camera/video/settings,
options:
  externalRtspEnabled:
    description: Boolean indicating if external rtsp stream is exposed.
    type: bool
  serial:
    description: Serial path parameter.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateDeviceCameraVideoSettings API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-device-camera-video-settings
    name: Cisco Meraki documentation for camera updateDeviceCameraVideoSettings
short_description: Resource module for devices _camera _video _settings
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.devices_camera_video_settings:
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
    state: present
    externalRtspEnabled: true
    serial: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "externalRtspEnabled": true,
      "rtspUrl": "string"
    }
"""
