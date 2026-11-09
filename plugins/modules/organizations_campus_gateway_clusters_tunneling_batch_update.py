#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_campus_gateway_clusters_tunneling_batch_update
short_description: Resource module for organizations _campus _gateway _clusters _tunneling
  _batch _update
description:
  - Manage operation create of the resource organizations _campus _gateway _clusters
    _tunneling _batch _update.
  - Update MCG cluster-network tunnel settings for multiple networks.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  items:
    description: MCG cluster-network tunnel settings.
    elements: dict
    suboptions:
      cluster:
        description: MCG cluster information.
        suboptions:
          id:
            description: Cluster ID.
            type: str
        type: dict
      data:
        description: Attributes related to the data plane.
        suboptions:
          encryption:
            description: Encryption settings of the data plane to be configured.
            suboptions:
              enabled:
                description: Whether or not tunnel traffic should be encrypted.
                type: bool
            type: dict
        type: dict
      network:
        description: Network information.
        suboptions:
          id:
            description: Network ID.
            type: str
        type: dict
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for campusGateway batchOrganizationCampusGatewayClustersTunnelingUpdate
    description: Complete reference of the batchOrganizationCampusGatewayClustersTunnelingUpdate
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!batch-organization-campus-gateway-clusters-tunneling-update
notes:
  - SDK Method used are
    campus_gateway.CampusGateway.batch_organization_campus_gateway_clusters_tunneling_update,
  - Paths used are
    post /organizations/{organizationId}/campusGateway/clusters/tunneling/batchUpdate,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_campus_gateway_clusters_tunneling_batch_update:
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
    meraki_caller: "{{ meraki_caller }}"
    meraki_use_iterator_for_get_pages: "{{ meraki_use_iterator_for_get_pages }}"
    meraki_inherit_logging_config: "{{ meraki_inherit_logging_config }}"
    items:
      - cluster:
          id: '10'
        data:
          encryption:
            enabled: true
        network:
          id: N_1
    organizationId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "items": [
        {
          "cluster": {
            "id": "string"
          },
          "network": {
            "id": "string"
          },
          "data": {
            "encryption": {
              "enabled": true
            }
          }
        }
      ]
    }
"""
