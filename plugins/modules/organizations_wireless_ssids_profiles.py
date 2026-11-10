#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_ssids_profiles
short_description: Resource module for organizations _wireless _ssids _profiles
description:
  - Manage operations create, update and delete of the resource organizations _wireless
    _ssids _profiles.
  - Create a new SSID profile in an organization.
  - Delete an SSID profile.
  - Update this SSID profile.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  id:
    description: Id path parameter.
    type: str
  name:
    description: Name of the SSID profile.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  precedence:
    description: Precedence configuration for the SSID profile.
    suboptions:
      radius:
        description: Source of RADIUS configuration - 'profile' means profile-level
          config takes precedence, 'network' means SSID-level config takes precedence.
        type: str
    type: dict
  ssid:
    description: SSID configuration for the profile.
    suboptions:
      addressing:
        description: Addressing settings for the SSID.
        suboptions:
          bonjourForwarding:
            description: Bonjour forwarding settings.
            suboptions:
              enabled:
                description: Whether Bonjour forwarding is enabled.
                type: bool
              rules:
                description: Bonjour forwarding rules.
                elements: dict
                suboptions:
                  description:
                    description: Description of the rule.
                    type: str
                  services:
                    description: Services.
                    elements: str
                    type: list
                  vlan:
                    description: VLAN settings for the rule.
                    suboptions:
                      id:
                        description: VLAN ID.
                        type: int
                    type: dict
                type: list
            type: dict
          mdns:
            description: MDNS gateway settings and rules for an SSID and cluster.
            suboptions:
              enabled:
                description: If true, mDNS is enabled for the SSID or cluster.
                type: bool
              rules:
                description: List of mDNS forwarding rules.
                elements: dict
                suboptions:
                  services:
                    description: Predefined or same-organization custom mDNS service
                      keys.
                    elements: str
                    type: list
                type: list
            type: dict
          mode:
            description: Addressing mode.
            type: str
          radius:
            description: RADIUS addressing settings.
            suboptions:
              guest:
                description: Guest VLAN settings.
                suboptions:
                  vlan:
                    description: VLAN settings for guest networks.
                    suboptions:
                      enabled:
                        description: Whether guest VLAN is enabled.
                        type: bool
                    type: dict
                type: dict
              overrideVlanTag:
                description: Whether to override VLAN tag.
                type: bool
            type: dict
        type: dict
      advertisement:
        description: SSID advertisement settings.
        suboptions:
          enabled:
            description: Whether the SSID is advertised.
            type: bool
        type: dict
      name:
        description: SSID name.
        type: str
      radius:
        description: RADIUS settings for the SSID.
        suboptions:
          accounting:
            description: RADIUS accounting settings.
            suboptions:
              enabled:
                description: Whether RADIUS accounting is enabled.
                type: bool
              updateInterval:
                description: Update interval for RADIUS accounting.
                type: int
            type: dict
          das:
            description: Direct Access Server settings.
            suboptions:
              coa:
                description: Change of Authorization settings.
                suboptions:
                  enabled:
                    description: Whether CoA is enabled.
                    type: bool
                type: dict
            type: dict
          eapTimers:
            description: Update the EAP timers settings.
            suboptions:
              eapolKey:
                description: EAPOL Key settings.
                suboptions:
                  maxRetries:
                    description: Maximum number of EAPOL key retries.
                    type: int
                  timeoutInMs:
                    description: EAPOL Key timeout in milliseconds.
                    type: int
                type: dict
              identity:
                description: EAP settings for identity requests.
                suboptions:
                  maxRetries:
                    description: Maximum number of EAP retries.
                    type: int
                  timeout:
                    description: EAP timeout in seconds.
                    type: int
                type: dict
              maxRetries:
                description: Maximum number of general EAP retries.
                type: int
              timeout:
                description: General EAP timeout in seconds.
                type: int
            type: dict
          identifiers:
            description: RADIUS identifiers.
            suboptions:
              calledStation:
                description: Called station identifier.
                type: str
              nas:
                description: NAS identifier.
                type: str
            type: dict
          policies:
            description: RADIUS policies.
            suboptions:
              attribute:
                description: RADIUS attribute for policies.
                type: str
              failover:
                description: Failover policy.
                suboptions:
                  mode:
                    description: Failover mode.
                    type: str
                type: dict
              fallback:
                description: Fallback policy.
                suboptions:
                  enabled:
                    description: Whether fallback is enabled.
                    type: bool
                type: dict
              loadBalancing:
                description: Load balancing policy.
                suboptions:
                  mode:
                    description: Load balancing mode.
                    type: str
                type: dict
            type: dict
          proxy:
            description: RADIUS proxy settings.
            suboptions:
              enabled:
                description: Whether RADIUS proxy is enabled.
                type: bool
            type: dict
          servers:
            description: Organization RADIUS servers, ordered by priority.
            elements: dict
            suboptions:
              id:
                description: RADIUS server ID.
                type: str
            type: list
          testing:
            description: RADIUS testing settings.
            suboptions:
              enabled:
                description: Whether RADIUS testing is enabled.
                type: bool
            type: dict
        type: dict
      security:
        description: Security settings for the SSID.
        suboptions:
          encryption:
            description: Encryption settings for the SSID.
            suboptions:
              akms:
                description: Authentication key management systems used by the SSID
                  (applicable for WPA3 only).
                elements: str
                type: list
              ciphers:
                description: Encryption ciphers used by the SSID (applicable for WPA3
                  only).
                elements: str
                type: list
              dot11r:
                description: 802.11r settings.
                suboptions:
                  adaptive:
                    description: Whether 802.11r is adaptive.
                    type: bool
                  enabled:
                    description: Whether 802.11r is enabled.
                    type: bool
                type: dict
              dot11w:
                description: 802.11w settings.
                suboptions:
                  enabled:
                    description: Whether 802.11w is enabled.
                    type: bool
                  required:
                    description: Whether 802.11w is required.
                    type: bool
                type: dict
              passphrase:
                description: Passphrase for the SSID.
                type: str
            type: dict
          identityPassphrase:
            description: Identity passphrase settings.
            suboptions:
              personalNetwork:
                description: Personal network settings.
                suboptions:
                  enabled:
                    description: Whether personal network is enabled.
                    type: bool
                type: dict
            type: dict
          mode:
            description: Security mode of the SSID.
            type: str
          protocol:
            description: Security protocol used by the SSID.
            type: str
        type: dict
      splash:
        description: Splash settings for the SSID.
        suboptions:
          auth:
            description: Authentication-related splash settings.
            suboptions:
              oauth:
                description: OAuth settings.
                suboptions:
                  domains:
                    description: Email domains allowed by OAuth.
                    elements: str
                    type: list
                type: dict
              simultaneousLogins:
                description: Simultaneous login settings.
                suboptions:
                  enabled:
                    description: Allow the same credentials to be used on multiple
                      devices simultaneously.
                    type: bool
                type: dict
            type: dict
          captivePortal:
            description: Captive portal configuration.
            suboptions:
              external:
                description: External captive portal configuration.
                suboptions:
                  url:
                    description: External captive portal URL.
                    type: str
                type: dict
              hosted:
                description: Hosted splash configuration.
                suboptions:
                  consent:
                    description: User consent settings.
                    suboptions:
                      message:
                        description: Consent message displayed to users.
                        type: str
                      required:
                        description: Whether users must provide consent.
                        type: bool
                    type: dict
                  language:
                    description: Splash page language.
                    suboptions:
                      code:
                        description: Language code.
                        type: str
                    type: dict
                  theme:
                    description: Hosted theme.
                    suboptions:
                      id:
                        description: Splash theme identifier.
                        type: str
                    type: dict
                type: dict
              provider:
                description: Captive portal provider selection.
                type: str
            type: dict
          controllerUnreachable:
            description: Behavior when the Meraki Cloud Splash controller is unreachable.
            suboptions:
              mode:
                description: How authentication attempts are handled when the controller
                  is unreachable.
                type: str
            type: dict
          mode:
            description: Splash mode.
            type: str
          preAccess:
            description: Pre-access settings before splash completion.
            suboptions:
              mode:
                description: Pre-access mode.
                type: str
              walledGarden:
                description: Walled garden settings.
                suboptions:
                  enabled:
                    description: Allow access to specific IP ranges and domains before
                      Splash.
                    type: bool
                  ranges:
                    description: List of IP address ranges and domains accessible
                      before Splash.
                    elements: str
                    type: list
                type: dict
            type: dict
          redirect:
            description: Post-Splash redirect settings.
            suboptions:
              override:
                description: Override settings for post-Splash redirection.
                suboptions:
                  enabled:
                    description: Whether users will be redirected to a configured
                      URL after completing the Splash or to the their originally requested
                      URL.
                    type: bool
                  url:
                    description: Custom URL where users will be redirected after completing
                      the Splash.
                    type: str
                type: dict
            type: dict
          timeout:
            description: Splash timeout in minutes. How often users must complete
              the Splash.
            type: int
        type: dict
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless createOrganizationWirelessSsidsProfile
    description: Complete reference of the createOrganizationWirelessSsidsProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-ssids-profile
  - name: Cisco Meraki documentation for wireless deleteOrganizationWirelessSsidsProfile
    description: Complete reference of the deleteOrganizationWirelessSsidsProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-ssids-profile
  - name: Cisco Meraki documentation for wireless updateOrganizationWirelessSsidsProfile
    description: Complete reference of the updateOrganizationWirelessSsidsProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-ssids-profile
notes:
  - SDK Method used are
    wireless.Wireless.create_organization_wireless_ssids_profile,
    wireless.Wireless.delete_organization_wireless_ssids_profile,
    wireless.Wireless.update_organization_wireless_ssids_profile,
  - Paths used are
    post /organizations/{organizationId}/wireless/ssids/profiles,
    delete
    /organizations/{organizationId}/wireless/ssids/profiles/{id},
    put /organizations/{organizationId}/wireless/ssids/profiles/{id},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_wireless_ssids_profiles:
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
    state: present
    name: Guest Profile
    organizationId: string
    precedence:
      radius: profile
    ssid:
      addressing:
        bonjourForwarding:
          enabled: true
          rules:
            - description: Desc
              services:
                - All Services
              vlan:
                id: 1
        mdns:
          enabled: true
          rules:
            - services:
                - airplay
                - custom_42
        mode: Bridge mode
        radius:
          guest:
            vlan:
              enabled: true
          overrideVlanTag: false
      advertisement:
        enabled: true
      name: SSID name
      radius:
        accounting:
          enabled: true
          updateInterval: 60
        das:
          coa:
            enabled: true
        eapTimers:
          eapolKey:
            maxRetries: 2
            timeoutInMs: 5000
          identity:
            maxRetries: 5
            timeout: 5
          maxRetries: 2
          timeout: 5
        identifiers:
          calledStation: '1'
          nas: some-nas-identifier
        policies:
          attribute: Filter-Id
          failover:
            mode: deny
          fallback:
            enabled: false
          loadBalancing:
            mode: priority
        proxy:
          enabled: false
        servers:
          - id: '1'
        testing:
          enabled: true
      security:
        encryption:
          akms:
            - SAE
            - SAE-EXT
          ciphers:
            - GCMP 256
          dot11r:
            adaptive: false
            enabled: false
          dot11w:
            enabled: true
            required: true
          passphrase: example-passphrase
        identityPassphrase:
          personalNetwork:
            enabled: true
        mode: psk
        protocol: WPA3 only
      splash:
        auth:
          oauth:
            domains:
              - example.com
              - subdomain.example.com
          simultaneousLogins:
            enabled: false
        captivePortal:
          external:
            url: https://example.com/splash
          hosted:
            consent:
              message: By continuing, you agree to our terms and conditions.
              required: true
            language:
              code: EN
            theme:
              id: c3ddcb4f16785ee747ab5ffc10867d6c8ea704be
          provider: hosted
        controllerUnreachable:
          mode: default
        mode: click-through
        preAccess:
          mode: block-all
          walledGarden:
            enabled: true
            ranges:
              - 192.168.1.0/24
              - 10.0.0.0/8
        redirect:
          override:
            enabled: true
            url: https://example.com/redirect
        timeout: 1440
- name: Update by id
  cisco.meraki.organizations_wireless_ssids_profiles:
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
    state: present
    id: string
    name: Guest Profile
    organizationId: string
    ssid:
      addressing:
        bonjourForwarding:
          enabled: true
          rules:
            - description: Desc
              services:
                - All Services
              vlan:
                id: 1
        mdns:
          enabled: true
          rules:
            - services:
                - airplay
                - custom_42
        radius:
          guest:
            vlan:
              enabled: true
          overrideVlanTag: false
      advertisement:
        enabled: true
      name: SSID name
      radius:
        accounting:
          enabled: true
          updateInterval: 60
        das:
          coa:
            enabled: true
        eapTimers:
          eapolKey:
            maxRetries: 2
            timeoutInMs: 5000
          identity:
            maxRetries: 5
            timeout: 5
          maxRetries: 2
          timeout: 5
        identifiers:
          calledStation: '1'
          nas: some-nas-identifier
        policies:
          attribute: Filter-Id
          failover:
            mode: deny
          fallback:
            enabled: false
          loadBalancing:
            mode: priority
        proxy:
          enabled: false
        servers:
          - id: '1'
        testing:
          enabled: true
      security:
        encryption:
          akms:
            - SAE
            - SAE-EXT
          ciphers:
            - GCMP 256
          dot11r:
            adaptive: false
            enabled: false
          dot11w:
            enabled: true
            required: true
          passphrase: example-passphrase
        identityPassphrase:
          personalNetwork:
            enabled: true
        mode: psk
        protocol: WPA3 only
      splash:
        auth:
          oauth:
            domains:
              - example.com
              - subdomain.example.com
          simultaneousLogins:
            enabled: false
        captivePortal:
          external:
            url: https://example.com/splash
          hosted:
            consent:
              message: By continuing, you agree to our terms and conditions.
              required: true
            language:
              code: EN
            theme:
              id: c3ddcb4f16785ee747ab5ffc10867d6c8ea704be
          provider: hosted
        controllerUnreachable:
          mode: default
        mode: click-through
        preAccess:
          mode: block-all
          walledGarden:
            enabled: true
            ranges:
              - 192.168.1.0/24
              - 10.0.0.0/8
        redirect:
          override:
            enabled: true
            url: https://example.com/redirect
        timeout: 1440
- name: Delete by id
  cisco.meraki.organizations_wireless_ssids_profiles:
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
    state: absent
    id: string
    organizationId: string
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
