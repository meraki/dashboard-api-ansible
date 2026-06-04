#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_sase_sites_attach
short_description: Resource module for organizations _sase _sites _attach
description:
  - Manage operation create of the resource organizations _sase _sites _attach. -
    > Attach sites in this organization to Secure Access. For an organization, a maximum
    of 2500 sites can be attached if they are in spoke mode or a maximum of 10 sites
    can be attached in hub mode.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
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
  items:
    description: List of Meraki SD-WAN sites with the associated regions to be attached.
    elements: dict
    suboptions:
      network:
        description: Meraki SD-WAN Network to be attached.
        suboptions:
          id:
            description: Network ID of the site to attach.
            type: str
        type: dict
      region:
        description: Region metadata for the site.
        suboptions:
          slug:
            description: Unique identifying slug for the region to attach the site
              in.
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
  - name: Cisco Meraki documentation for organizations attachOrganizationSaseSites
    description: Complete reference of the attachOrganizationSaseSites API.
    link: https://developer.cisco.com/meraki/api-v1/#!attach-organization-sase-sites
notes:
  - SDK Method used are
    organizations.Organizations.attach_organization_sase_sites,
  - Paths used are
    post /organizations/{organizationId}/sase/sites/attach,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_sase_sites_attach:
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
    callback:
      httpServer:
        id: aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=
      payloadTemplate:
        id: wpt_2100
      sharedSecret: secret
      url: https://webhook.site/28efa24e-f830-4d9f-a12b-fbb9e5035031
    items:
      - network:
          id: N_1234567890
        region:
          slug: us-west-1
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
          "pipelineId": "string",
          "operation": {
            "id": "string"
          },
          "status": "string",
          "counts": {
            "jobs": {
              "total": 0,
              "byStatus": {
                "completed": 0,
                "failed": 0,
                "pending": 0
              }
            }
          }
        }
      ],
      "meta": {
        "counts": {
          "items": {
            "total": 0,
            "remaining": 0
          }
        }
      }
    }
"""
