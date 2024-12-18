#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: administered_identities_me_api_keys_revoke
short_description: Resource module for administered _identities _me _api _keys _revoke
description:
- Manage operation create of the resource administered _identities _me _api _keys _revoke.
- >
   Revokes an identity's API key, using the last four characters of the key. For users who have access to more than
   one organization, the change will take up to five minutes to propagate. If one of the organizations is currently
   under maintenance, the change may not propagate fully until after the maintenance has been completed.
version_added: '2.20.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  suffix:
    description: Suffix path parameter.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for administered revokeAdministeredIdentitiesMeApiKeys
  description: Complete reference of the revokeAdministeredIdentitiesMeApiKeys API.
  link: https://developer.cisco.com/meraki/api-v1/#!revoke-administered-identities-me-api-keys
notes:
  - SDK Method used are
    administered.Administered.revoke_administered_identities_me_api_keys,

  - Paths used are
    post /administered/identities/me/api/keys/{suffix}/revoke,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.administered_identities_me_api_keys_revoke:
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
    suffix: string

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""