#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_ssids_profiles_info
short_description: Information module for organizations _wireless _ssids _profiles
description:
  - Get all organizations _wireless _ssids _profiles.
  - Returns the SSID profiles for an organization.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
      - OrganizationId path parameter. Organization ID.
    type: str
  name:
    description:
      - Name query parameter. (Optional) Filter results by name. Case insensitive
        substring match.
    type: str
  sortBy:
    description:
      - SortBy query parameter. Column to sort results by. Default is `name`.
    type: str
  sortOrder:
    description:
      - SortOrder query parameter. Direction to sort results by. Default is `asc`.
    type: str
  profileIds:
    description:
      - ProfileIds query parameter. (Optional) Filter results by a list of SSID profile
        IDs.
    elements: int
    type: list
  perPage:
    description:
      - PerPage query parameter. The number of entries per page returned. Acceptable
        range is 3 - 1000. Default is 1000.
    type: int
  startingAfter:
    description:
      - >
        StartingAfter query parameter. A token used by the server to indicate the
        start of the page. Often this is a timestamp or an ID but it is not limited
        to those. This parameter should not be defined by client applications. The
        link for the first, last, prev, or next page in the HTTP Link header should
        define it.
    type: str
  endingBefore:
    description:
      - >
        EndingBefore query parameter. A token used by the server to indicate the end
        of the page. Often this is a timestamp or an ID but it is not limited to those.
        This parameter should not be defined by client applications. The link for
        the first, last, prev, or next page in the HTTP Link header should define
        it.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless getOrganizationWirelessSsidsProfiles
    description: Complete reference of the getOrganizationWirelessSsidsProfiles API.
    link: https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_organization_wireless_ssids_profiles,
  - Paths used are
    get /organizations/{organizationId}/wireless/ssids/profiles,
"""

EXAMPLES = r"""
- name: Get all organizations _wireless _ssids _profiles
  cisco.meraki.organizations_wireless_ssids_profiles_info:
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
    name: string
    sortBy: string
    sortOrder: string
    profileIds: []
    perPage: 0
    startingAfter: string
    endingBefore: string
    organizationId: string
    total_pages: -1
    direction: next
  register: result
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "precedence": {
        "radius": "string"
      },
      "ssid": {
        "name": "string",
        "advertisement": {
          "enabled": true
        },
        "security": {
          "mode": "string",
          "protocol": "string",
          "encryption": {
            "ciphers": [
              "string"
            ],
            "akms": [
              "string"
            ]
          },
          "dhcp": {
            "mandatory": {
              "enabled": true
            }
          }
        },
        "radius": {
          "servers": [
            {
              "id": 0,
              "address": "string",
              "name": "string",
              "modes": [
                {
                  "mode": "string",
                  "port": 0
                }
              ]
            }
          ],
          "accounting": {
            "enabled": true,
            "updateInterval": 0
          },
          "policies": {
            "failover": {
              "mode": "string"
            },
            "loadBalancing": {
              "mode": "string"
            },
            "fallback": {
              "enabled": true
            },
            "attribute": "string",
            "timeout": 0,
            "numAttempts": 0
          },
          "proxy": {
            "enabled": true
          },
          "testing": {
            "enabled": true
          },
          "identifiers": {
            "calledStation": "string",
            "nas": "string"
          },
          "das": {
            "coa": {
              "enabled": true
            }
          },
          "eapTimers": {
            "timeout": 0,
            "maxRetries": 0,
            "identity": {
              "timeout": 0,
              "maxRetries": 0
            },
            "eapolKey": {
              "maxRetries": 0,
              "timeoutInMs": 0
            }
          }
        },
        "addressing": {
          "mode": "string",
          "adultContentFiltering": {
            "enabled": true
          },
          "dnsRewrite": {
            "enabled": true,
            "dnsCustomNameservers": [
              "string"
            ]
          },
          "bonjourForwarding": {
            "enabled": true,
            "rules": [
              {
                "description": "string",
                "vlan": {
                  "id": 0
                },
                "services": [
                  "string"
                ]
              }
            ]
          },
          "mdns": {
            "enabled": true,
            "rules": [
              {
                "services": [
                  "string"
                ]
              }
            ]
          },
          "radius": {
            "guest": {
              "vlan": {
                "enabled": true
              }
            },
            "overrideVlanTag": true
          }
        },
        "splash": {
          "mode": "string",
          "captivePortal": {
            "provider": "string",
            "external": {
              "url": "string"
            },
            "hosted": {
              "theme": {
                "id": "string"
              },
              "language": {
                "code": "string"
              },
              "consent": {
                "required": true,
                "message": "string"
              }
            }
          },
          "redirect": {
            "override": {
              "enabled": true,
              "url": "string"
            }
          },
          "timeout": 0,
          "auth": {
            "simultaneousLogins": {
              "enabled": true
            },
            "oauth": {
              "domains": [
                "string"
              ]
            }
          },
          "controllerUnreachable": {
            "mode": "string"
          },
          "preAccess": {
            "mode": "string",
            "walledGarden": {
              "enabled": true,
              "ranges": [
                "string"
              ]
            }
          }
        }
      }
    }
"""
