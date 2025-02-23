#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Get all networks _camera _quality _retention _profiles.
  - Get networks _camera _quality _retention _profiles by id.
  - List the quality retention profiles for this network.
  - Retrieve a single quality retention profile.
extends_documentation_fragment:
  - cisco.meraki.module_info
module: networks_camera_quality_retention_profiles_info
notes:
  - SDK Method used are camera.Camera.get_network_camera_quality_retention_profile,
    camera.Camera.get_network_camera_quality_retention_profiles,
  - Paths used are get /networks/{networkId}/camera/qualityRetentionProfiles, get
    /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId},
options:
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
      - NetworkId path parameter. Network ID.
    type: str
  qualityRetentionProfileId:
    description:
      - QualityRetentionProfileId path parameter. Quality retention profile ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the getNetworkCameraQualityRetentionProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profile
    name: Cisco Meraki documentation for camera getNetworkCameraQualityRetentionProfile
  - description: Complete reference of the getNetworkCameraQualityRetentionProfiles
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profiles
    name: Cisco Meraki documentation for camera getNetworkCameraQualityRetentionProfiles
short_description: Information module for networks _camera _quality _retention _profiles
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Get all networks _camera _quality _retention _profiles
  cisco.meraki.networks_camera_quality_retention_profiles_info:
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
- name: Get networks _camera _quality _retention _profiles by id
  cisco.meraki.networks_camera_quality_retention_profiles_info:
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
    qualityRetentionProfileId: string
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "audioRecordingEnabled": true,
      "cloudArchiveEnabled": true,
      "id": "string",
      "maxRetentionDays": 0,
      "motionBasedRetentionEnabled": true,
      "motionDetectorVersion": 0,
      "name": "string",
      "networkId": "string",
      "restrictedBandwidthModeEnabled": true,
      "scheduleId": "string",
      "smartRetention": {
        "enabled": true
      },
      "videoSettings": {
        "MV12/MV22/MV72": {
          "quality": "string",
          "resolution": "string"
        },
        "MV12WE": {
          "quality": "string",
          "resolution": "string"
        },
        "MV21/MV71": {
          "quality": "string",
          "resolution": "string"
        },
        "MV32": {
          "quality": "string",
          "resolution": "string"
        }
      }
    }
"""
