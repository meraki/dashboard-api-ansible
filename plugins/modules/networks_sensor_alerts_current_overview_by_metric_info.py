#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_sensor_alerts_current_overview_by_metric_info
short_description: Information module for networks _sensor _alerts _current _overview _bymetric
description:
- Get all networks _sensor _alerts _current _overview _bymetric.
- Return an overview of currently alerting sensors by metric.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  networkId:
    description:
    - NetworkId path parameter. Network ID.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for sensor getNetworkSensorAlertsCurrentOverviewByMetric
  description: Complete reference of the getNetworkSensorAlertsCurrentOverviewByMetric API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-current-overview-by-metric
notes:
  - SDK Method used are
    sensor.Sensor.get_network_sensor_alerts_current_overview_by_metric,

  - Paths used are
    get /networks/{networkId}/sensor/alerts/current/overview/byMetric,
"""

EXAMPLES = r"""
- name: Get all networks _sensor _alerts _current _overview _bymetric
  cisco.meraki.networks_sensor_alerts_current_overview_by_metric_info:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    networkId: string
  register: result

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "counts": {
        "apparentPower": 0,
        "co2": 0,
        "current": 0,
        "door": 0,
        "frequency": 0,
        "humidity": 0,
        "indoorAirQuality": 0,
        "noise": {
          "ambient": 0
        },
        "pm25": 0,
        "powerFactor": 0,
        "realPower": 0,
        "temperature": 0,
        "tvoc": 0,
        "upstreamPower": 0,
        "voltage": 0,
        "water": 0
      },
      "supportedMetrics": [
        "string"
      ]
    }
"""
