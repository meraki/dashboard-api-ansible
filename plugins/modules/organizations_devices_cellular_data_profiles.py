#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_devices_cellular_data_profiles
short_description: Resource module for organizations _devices _cellular _data _profiles
description:
  - Manage operations create, update and delete of the resource organizations _devices
    _cellular _data _profiles. - > Add a cellular data management profile to this
    organization. Creates a cellular data management profile in this organization
    and returns the created profile, including its rules and actions. - > Delete a
    cellular data management profile from this organization. Removes the profile,
    including its associated rules and node assignments, and notifies affected devices
    of the resulting configuration change. - > Update a Cellular Data Management Profile.
    Note that changes made to this endpoint will overwrite existing settings for the
    profile so the entire profile, rules and actions should be sent when making an
    update.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  description:
    description: Description of the profile to be added.
    type: str
  name:
    description: Name of the profile to be added. This must be unique.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  profileId:
    description: ID of the profile.
    type: str
  rules:
    description: The rules associated with this profile. At least one rule and no
      more than two rules may be defined for a profile.
    elements: dict
    suboptions:
      actions:
        description: The defined actions that will occur when the profile rule is
          triggered. No more than two actions may be defined for a rule.
        elements: dict
        suboptions:
          type:
            description: The type of action to be undertaken. One of 'send_message'
              or 'failover'.
            type: str
        type: list
      cap:
        description: The data cap values to be set with this rule.
        suboptions:
          term:
            description: The data usage term configuration that determines when the
              aggregated data count resets on the device.
            suboptions:
              resets:
                description: How often the device resets the aggregated data count.
                  One of 'daily', 'weekly', or 'monthly'.
                type: str
              starts:
                description: The reset point for the selected term. Exactly one of
                  the nested values must be set depending on the selected reset frequency.
                  Use 'hourOfDay' for a daily reset, 'dayOfWeek' for a weekly reset,
                  and 'dayOfMonth' for a monthly reset.
                suboptions:
                  dayOfMonth:
                    description: When the data usage term is to be reset monthly,
                      the day of month that the accounted bandwidth usage for the
                      term should be reset. This can be between 1 and 31 (months that
                      have a number of days less than the value for dayOfMonth will
                      begin on the last day of the month).
                    type: int
                  dayOfWeek:
                    description: When the data usage term resets weekly, the day of
                      week that the accounted bandwidth usage should reset. Uses the
                      lowercase three-letter weekday abbreviation 'mon', 'tue', 'wed',
                      'thu', 'fri', 'sat', or 'sun'. Requests are normalized case-insensitively
                      to this form.
                    type: str
                  hourOfDay:
                    description: When the data usage term is to be reset daily, the
                      hour the accounted bandwidth usage for the term should be reset.
                      This can be between 0 and 23 (where 0 is 0 00 GMT and 23 is
                      23 00 GMT).
                    type: int
                type: dict
            type: dict
          threshold:
            description: The data usage threshold at which the rule should be triggered.
              This is expressed as a float between 0.01 and 1.0 (where 0.01 is equal
              to 1% of total and 1.0 is equal to 100%). By default this will be 1.0.
            type: float
          value:
            description: The total bandwidth available for the specified term in megabytes.
            type: int
        type: dict
      slot:
        description: The SIM slot that the rule is applied to. One of 'sim1', 'sim2',
          or 'sim3'. Devices included in this group must have an active card/profile
          with the defined SIM slot in order to use this rule.
        type: str
      uplink:
        description: Configuration for the uplink governed by this rule.
        suboptions:
          isPreferred:
            description: Whether this uplink is the preferred one to use once all
              rules have been exhausted.
            type: bool
          priority:
            description: The uplink priority for this rule. One of 1 or 2, where 1
              is the highest priority.
            type: int
        type: dict
    type: list
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations createOrganizationDevicesCellularDataProfile
    description: Complete reference of the createOrganizationDevicesCellularDataProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-cellular-data-profile
  - name: Cisco Meraki documentation for organizations deleteOrganizationDevicesCellularDataProfile
    description: Complete reference of the deleteOrganizationDevicesCellularDataProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-cellular-data-profile
  - name: Cisco Meraki documentation for organizations updateOrganizationDevicesCellularDataProfile
    description: Complete reference of the updateOrganizationDevicesCellularDataProfile
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-devices-cellular-data-profile
notes:
  - SDK Method used are
    organizations.Organizations.create_organization_devices_cellular_data_profile,
    organizations.Organizations.delete_organization_devices_cellular_data_profile,
    organizations.Organizations.update_organization_devices_cellular_data_profile,
  - Paths used are
    post /organizations/{organizationId}/devices/cellular/data/profiles,
    delete /organizations/{organizationId}/devices/cellular/data/profiles/{profileId},
    put /organizations/{organizationId}/devices/cellular/data/profiles/{profileId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_devices_cellular_data_profiles:
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
    description: some description
    name: some unique profile name
    organizationId: string
    rules:
      - actions:
          - type: failover
        cap:
          term:
            resets: daily
            starts:
              dayOfMonth: 2
              dayOfWeek: mon
              hourOfDay: 12
          threshold: 0.9
          value: 42
        slot: sim1
        uplink:
          isPreferred: true
          priority: 1
- name: Update by id
  cisco.meraki.organizations_devices_cellular_data_profiles:
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
    description: some description
    organizationId: string
    profileId: '42'
    rules:
      - actions:
          - type: failover
        cap:
          term:
            resets: daily
            starts:
              dayOfMonth: 2
              dayOfWeek: mon
              hourOfDay: 12
          threshold: 0.9
          value: 42
        slot: sim1
        uplink:
          isPreferred: true
          priority: 1
- name: Delete by id
  cisco.meraki.organizations_devices_cellular_data_profiles:
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
      "lastUpdatedAt": "string",
      "name": "string",
      "description": "string",
      "rules": [
        {
          "ruleId": "string",
          "slot": "string",
          "uplink": {
            "priority": 0,
            "isPreferred": true
          },
          "cap": {
            "value": 0,
            "threshold": 0,
            "term": {
              "resets": "string",
              "starts": {
                "hourOfDay": 0,
                "dayOfWeek": "string",
                "dayOfMonth": 0
              }
            }
          },
          "actions": [
            {
              "type": "string"
            }
          ]
        }
      ]
    }
"""
