#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource networks _wireless _ssids _traffic _shaping
    _rules.
  - Update the traffic shaping rules for an SSID on an MR network.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_wireless_ssids_traffic_shaping_rules
notes:
  - SDK Method used are wireless.Wireless.update_network_wireless_ssid_traffic_shaping_rules,
  - Paths used are put /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules,
options:
  defaultRulesEnabled:
    description: Whether default traffic shaping rules are enabled (true) or disabled
      (false). There are 4 default rules, which can be seen on your network's traffic
      shaping page. Note that default rules count against the rule limit of 8.
    type: bool
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  number:
    description: Number path parameter.
    type: str
  rules:
    description: An array of traffic shaping rules. Rules are applied in the order
      that they are specified in. An empty list (or null) means no rules. Note that
      you are allowed a maximum of 8 rules.
    elements: dict
    suboptions:
      definitions:
        description: A list of objects describing the definitions of your traffic
          shaping rule. At least one definition is required.
        elements: dict
        suboptions:
          type:
            description: The type of definition. Can be one of 'application', 'applicationCategory',
              'host', 'port', 'ipRange' or 'localNet'.
            type: str
          value:
            description: If "type" is 'host', 'port', 'ipRange' or 'localNet', then
              "value" must be a string, matching either a hostname (e.g. "somesite.com"),
              a port (e.g. 8080), or an IP range ("192.1.0.0", "192.1.0.0/16", or
              "10.1.0.0/16 80"). 'localNet' also supports CIDR notation, excluding
              custom ports. If "type" is 'application' or 'applicationCategory', then
              "value" must be an object with the structure { "id" "meraki layer7/..."
              }, where "id" is the application category or application ID (for a list
              of IDs for your network, use the trafficShaping/applicationCategories
              endpoint).
            type: str
        type: list
      dscpTagValue:
        description: The DSCP tag applied by your rule. Null means 'Do not change
          DSCP tag'. For a list of possible tag values, use the trafficShaping/dscpTaggingOptions
          endpoint.
        type: int
      pcpTagValue:
        description: The PCP tag applied by your rule. Can be 0 (lowest priority)
          through 7 (highest priority). Null means 'Do not set PCP tag'.
        type: int
      perClientBandwidthLimits:
        description: An object describing the bandwidth settings for your rule.
        suboptions:
          bandwidthLimits:
            description: The bandwidth limits object, specifying the upload ('limitUp')
              and download ('limitDown') speed in Kbps. These are only enforced if
              'settings' is set to 'custom'.
            suboptions:
              limitDown:
                description: The maximum download limit (integer, in Kbps).
                type: int
              limitUp:
                description: The maximum upload limit (integer, in Kbps).
                type: int
            type: dict
          settings:
            description: How bandwidth limits are applied by your rule. Can be one
              of 'network default', 'ignore' or 'custom'.
            type: str
        type: dict
    type: list
  trafficShapingEnabled:
    description: Whether traffic shaping rules are applied to clients on your SSID.
    type: bool
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateNetworkWirelessSsidTrafficShapingRules
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-traffic-shaping-rules
    name: Cisco Meraki documentation for wireless updateNetworkWirelessSsidTrafficShapingRules
short_description: Resource module for networks _wireless _ssids _traffic _shaping
  _rules
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_wireless_ssids_traffic_shaping_rules:
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
    defaultRulesEnabled: true
    networkId: string
    number: string
    rules:
      - definitions:
          - type: host
            value: google.com
        dscpTagValue: 0
        pcpTagValue: 0
        perClientBandwidthLimits:
          bandwidthLimits:
            limitDown: 1000000
            limitUp: 1000000
          settings: custom
    trafficShapingEnabled: true
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "defaultRulesEnabled": true,
      "rules": [
        {
          "definitions": [
            {
              "type": "string",
              "value": "string"
            }
          ],
          "dscpTagValue": 0,
          "pcpTagValue": 0,
          "perClientBandwidthLimits": {
            "bandwidthLimits": {
              "limitDown": 0,
              "limitUp": 0
            },
            "settings": "string"
          }
        }
      ],
      "trafficShapingEnabled": true
    }
"""
