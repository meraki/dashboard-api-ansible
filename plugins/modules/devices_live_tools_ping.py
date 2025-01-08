#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation create of the resource devices _live _tools _ping.
  - 'Enqueue a job to ping a target host from the device. This endpoint has a sustained
    rate limit of one request every five seconds per device, with an allowed burst
    of five requests.

    '
extends_documentation_fragment:
  - cisco.meraki.module
module: devices_live_tools_ping
notes:
  - SDK Method used are devices.Devices.create_device_live_tools_ping,
  - Paths used are post /devices/{serial}/liveTools/ping,
options:
  callback:
    description: Details for the callback. Please include either an httpServerId OR
      url and sharedSecret.
    suboptions:
      httpServer:
        description: The webhook receiver used for the callback webhook.
        suboptions:
          id:
            description: The webhook receiver ID that will receive information. If
              specifying this, please leave the url and sharedSecret fields blank.
            type: str
        type: dict
      payloadTemplate:
        description: The payload template of the webhook used for the callback.
        suboptions:
          id:
            description: The ID of the payload template. Defaults to 'wpt_00005' for
              the Callback (included) template.
            type: str
        type: dict
      sharedSecret:
        description: A shared secret that will be included in the requests sent to
          the callback URL. It can be used to verify that the request was sent by
          Meraki. If using this field, please also specify an url.
        type: str
      url:
        description: The callback URL for the webhook target. If using this field,
          please also specify a sharedSecret.
        type: str
    type: dict
  count:
    description: Count parameter to pass to ping. 1..5, default 5.
    type: int
  serial:
    description: Serial path parameter.
    type: str
  target:
    description: FQDN, IPv4 or IPv6 address.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the createDeviceLiveToolsPing API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ping
    name: Cisco Meraki documentation for devices createDeviceLiveToolsPing
short_description: Resource module for devices _live _tools _ping
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.devices_live_tools_ping:
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
    state: present
    callback:
      httpServer:
        id: aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=
      payloadTemplate:
        id: wpt_2100
      sharedSecret: secret
      url: https://webhook.site/28efa24e-f830-4d9f-a12b-fbb9e5035031
    count: 2
    serial: string
    target: 75.75.75.75
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "callback": {
        "id": "string",
        "status": "string",
        "url": "string"
      },
      "pingId": "string",
      "request": {
        "count": 0,
        "serial": "string",
        "target": "string"
      },
      "status": "string",
      "url": "string"
    }
"""
