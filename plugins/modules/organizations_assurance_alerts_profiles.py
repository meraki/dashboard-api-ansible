#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_assurance_alerts_profiles
short_description: Resource module for organizations _assurance _alerts _profiles
description:
  - Manage operations create, update and delete of the resource organizations _assurance
    _alerts _profiles.
  - Create an alert profile.
  - Delete an alert profile for this organization.
  - Update an alert profile.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  alertScheduleId:
    description: ID of the alert schedule associated with this profile.
    type: str
  alertTypes:
    description: Alert types associated with this alert profile.
    elements: str
    type: list
  configuration:
    description: Alert configuration for this profile.
    suboptions:
      alertDestinations:
        description: List of alert channels and destinations for the alert type.
        suboptions:
          email:
            description: Email channel configuration.
            suboptions:
              enabled:
                description: Whether or not the email channel is enabled for this
                  alert type.
                type: bool
              recipients:
                description: List of email addresses to receive the notifications.
                elements: str
                type: list
            type: dict
          sms:
            description: SMS channel configuration.
            suboptions:
              enabled:
                description: Whether or not the sms channel is enabled for this alert
                  type.
                type: bool
              recipients:
                description: List of sms recipient phone numbers to receive the notifications.
                elements: str
                type: list
            type: dict
          webhook:
            description: Webhook channel configuration.
            suboptions:
              enabled:
                description: Whether or not the webhook channel is enabled for this
                  alert type.
                type: bool
              recipients:
                description: List of webhook recipient ids.
                elements: str
                type: list
            type: dict
        type: dict
      enabled:
        description: Whether the alerts are enabled.
        type: bool
      maintenance:
        description: Maintenance configuration for this profile.
        suboptions:
          silencing:
            description: Silencing configuration for maintenance.
            suboptions:
              enabled:
                description: Whether silencing is enabled in maintenance mode.
                type: bool
            type: dict
        type: dict
    type: dict
  name:
    description: Name of the alert profile.
    type: str
  networkIds:
    description: Networks associated with this alert profile.
    elements: str
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  profileId:
    description: ProfileId path parameter. Profile ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations createOrganizationAssuranceAlertsProfile
    description: Complete reference of the createOrganizationAssuranceAlertsProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-assurance-alerts-profile
  - name: Cisco Meraki documentation for organizations deleteOrganizationAssuranceAlertsProfile
    description: Complete reference of the deleteOrganizationAssuranceAlertsProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-assurance-alerts-profile
  - name: Cisco Meraki documentation for organizations updateOrganizationAssuranceAlertsProfile
    description: Complete reference of the updateOrganizationAssuranceAlertsProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-assurance-alerts-profile
notes:
  - SDK Method used are
    organizations.Organizations.create_organization_assurance_alerts_profile,
    organizations.Organizations.delete_organization_assurance_alerts_profile,
    organizations.Organizations.update_organization_assurance_alerts_profile,
  - Paths used are
    post /organizations/{organizationId}/assurance/alerts/profiles,
    delete /organizations/{organizationId}/assurance/alerts/profiles/{profileId},
    put /organizations/{organizationId}/assurance/alerts/profiles/{profileId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_assurance_alerts_profiles:
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
    alertScheduleId: '9876543210'
    alertTypes:
      - unreachable
      - vlan_mismatch
    configuration:
      alertDestinations:
        email:
          enabled: true
          recipients:
            - miles@meraki.net
        sms:
          enabled: true
          recipients:
            - +1 (999) 999-1111
        webhook:
          enabled: true
          recipients:
            - aHR0cHM6Ly9nb29nbGUuY29tL2Zha2U=
      enabled: true
      maintenance:
        silencing:
          enabled: true
    name: alert_profile_1
    networkIds:
      - N_123657123
      - N_9876143
    organizationId: string
- name: Update by id
  cisco.meraki.organizations_assurance_alerts_profiles:
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
    alertScheduleId: '9876543210'
    alertTypes:
      - unreachable
      - vlan_mismatch
    configuration:
      alertDestinations:
        email:
          enabled: true
          recipients:
            - miles@meraki.net
        sms:
          enabled: true
          recipients:
            - +1 (999) 999-1111
        webhook:
          enabled: true
          recipients:
            - aHR0cHM6Ly9nb29nbGUuY29tL2Zha2U=
      enabled: true
      maintenance:
        silencing:
          enabled: true
    name: alert_profile_1
    networkIds:
      - N_123657123
      - N_9876143
    organizationId: string
    profileId: string
- name: Delete by id
  cisco.meraki.organizations_assurance_alerts_profiles:
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
    organizationId: string
    profileId: string
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "profileId": "string",
      "name": "string",
      "organizationId": "string",
      "networkIds": [
        "string"
      ],
      "alertTypes": [
        "string"
      ],
      "alertScheduleId": {},
      "configuration": {
        "enabled": true,
        "maintenance": {
          "silencing": {
            "enabled": true
          }
        },
        "alertDestinations": {
          "email": {
            "enabled": true,
            "recipients": [
              "string"
            ]
          },
          "sms": {
            "enabled": true,
            "recipients": [
              "string"
            ]
          },
          "webhook": {
            "enabled": true,
            "recipients": [
              {
                "id": "string",
                "name": "string",
                "url": "string"
              }
            ]
          }
        }
      }
    }
"""
