#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_policies_global_firewall_rulesets_rules
short_description: Resource module for organizations _policies _global _firewall _rulesets
  _rules
description:
  - Manage operations create, update and delete of the resource organizations _policies
    _global _firewall _rulesets _rules.
  - Create an Organization-Wide Policy Firewall Rule.
  - Delete an Organization-Wide Policy Firewall Rule.
  - Update an Organization-Wide Policy Firewall Rule.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  description:
    description: Description of the firewall rule.
    type: str
  destinations:
    description: Destination traffic criteria. Each source or destination bloc is
      capped separately per rule at 100 total segment values. The count is segments_values_count
      the sum of all values across every segment type in that bloc. Ports use a separate
      cap of 100.
    suboptions:
      criteria:
        description: Destination criteria values (not present if 'any' is in matchCriteria).
        suboptions:
          addressRanges:
            description: Address ranges or addresses.
            elements: str
            type: list
          applianceVlans:
            description: Appliance VLANs.
            elements: dict
            suboptions:
              interfaceId:
                description: Interface ID.
                type: str
            type: list
          applicationCategories:
            description: Application categories.
            elements: dict
            suboptions:
              applications:
                description: Applications in this category.
                elements: dict
                suboptions:
                  id:
                    description: Application ID.
                    type: str
                  name:
                    description: Application name.
                    type: str
                type: list
              id:
                description: Category ID.
                type: str
              name:
                description: Category name.
                type: str
            type: list
          applications:
            description: Applications.
            elements: dict
            suboptions:
              id:
                description: Application ID.
                type: str
              name:
                description: Application name.
                type: str
            type: list
          policyObjectGroups:
            description: Policy object groups.
            elements: dict
            suboptions:
              id:
                description: Policy object group ID.
                type: str
            type: list
          policyObjects:
            description: Policy objects.
            elements: dict
            suboptions:
              id:
                description: Policy object ID.
                type: str
            type: list
          ports:
            description: Port numbers or ranges.
            elements: str
            type: list
          services:
            description: Protocol and port services.
            elements: dict
            suboptions:
              ports:
                description: Port numbers or ranges.
                elements: str
                type: list
              protocol:
                description: Protocol (tcp, udp, etc).
                type: str
            type: list
        type: dict
      matchCriteria:
        description: Destination match criteria types.
        elements: str
        type: list
    type: dict
  enabled:
    description: Whether the rule is enabled.
    type: bool
  name:
    description: Name of the firewall rule.
    type: str
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  policy:
    description: Rule policy - allow or deny traffic.
    type: str
  priority:
    description: Rule priority (lower numbers = higher priority).
    type: int
  ruleId:
    description: RuleId path parameter. Rule ID.
    type: str
  rulesetId:
    description: Firewall ruleset ID to associate the rule with.
    type: str
  sources:
    description: Source traffic criteria. Each source or destination bloc is capped
      separately per rule at 100 total segment values. The count is segments_values_count
      the sum of all values across every segment type in that bloc. Ports use a separate
      cap of 100.
    suboptions:
      criteria:
        description: Source criteria values (not present if 'any' is in matchCriteria).
        suboptions:
          addressRanges:
            description: Address ranges or addresses.
            elements: str
            type: list
          applianceVlans:
            description: Appliance VLANs.
            elements: dict
            suboptions:
              interfaceId:
                description: Interface ID.
                type: str
            type: list
          policyObjectGroups:
            description: Policy object groups.
            elements: dict
            suboptions:
              id:
                description: Policy object group ID.
                type: str
            type: list
          policyObjects:
            description: Policy objects.
            elements: dict
            suboptions:
              id:
                description: Policy object ID.
                type: str
            type: list
          ports:
            description: Port numbers or ranges.
            elements: str
            type: list
        type: dict
      matchCriteria:
        description: Source match criteria types.
        elements: str
        type: list
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for organizations createOrganizationPoliciesGlobalFirewallRulesetsRule
    description: Complete reference of the createOrganizationPoliciesGlobalFirewallRulesetsRule
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-firewall-rulesets-rule
  - name: Cisco Meraki documentation for organizations deleteOrganizationPoliciesGlobalFirewallRulesetsRule
    description: Complete reference of the deleteOrganizationPoliciesGlobalFirewallRulesetsRule
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-firewall-rulesets-rule
  - name: Cisco Meraki documentation for organizations updateOrganizationPoliciesGlobalFirewallRulesetsRule
    description: Complete reference of the updateOrganizationPoliciesGlobalFirewallRulesetsRule
      API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-firewall-rulesets-rule
notes:
  - SDK Method used are
    organizations.Organizations.create_organization_policies_global_firewall_rulesets_rule,
    organizations.Organizations.delete_organization_policies_global_firewall_rulesets_rule,
    organizations.Organizations.update_organization_policies_global_firewall_rulesets_rule,
  - Paths used are
    post /organizations/{organizationId}/policies/global/firewall/rulesets/rules,
    delete /organizations/{organizationId}/policies/global/firewall/rulesets/rules/{ruleId},
    put /organizations/{organizationId}/policies/global/firewall/rulesets/rules/{ruleId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_policies_global_firewall_rulesets_rules:
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
    description: This is rule 1
    destinations:
      criteria:
        addressRanges:
          - 1.1.1.1
          - 2.2.2.2
        applianceVlans:
          - interfaceId: L_123456789012345678_vlan_200
        applicationCategories:
          - applications:
              - id: meraki:layer7/application/5
                name: Advertising.com
            id: meraki:layer7/category/24
            name: Advertising
        applications:
          - id: meraki:layer7/application/5
            name: Advertising.com
        policyObjectGroups:
          - id: '45'
        policyObjects:
          - id: '23'
        ports:
          - '22'
          - 42-46
        services:
          - ports:
              - '80'
              - '443'
            protocol: tcp
      matchCriteria:
        - addressRanges
        - services
        - applicationCategories
        - applications
        - policyObjects
        - policyObjectGroups
        - applianceVlans
    enabled: true
    name: Allow developers
    organizationId: string
    policy: deny
    priority: 100
    rulesetId: '32'
    sources:
      criteria:
        addressRanges:
          - 1.1.1.1
          - 2.2.2.2
        applianceVlans:
          - interfaceId: L_123456789012345678_vlan_200
        policyObjectGroups:
          - id: '45'
        policyObjects:
          - id: '23'
        ports:
          - '22'
          - 42-46
      matchCriteria:
        - addressRanges
        - ports
        - policyObjects
        - policyObjectGroups
        - applianceVlans
- name: Delete by id
  cisco.meraki.organizations_policies_global_firewall_rulesets_rules:
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
    ruleId: string
- name: Update by id
  cisco.meraki.organizations_policies_global_firewall_rulesets_rules:
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
    description: This is rule 1
    destinations:
      criteria:
        addressRanges:
          - 1.1.1.1
          - 2.2.2.2
        applianceVlans:
          - interfaceId: L_123456789012345678_vlan_200
        applicationCategories:
          - applications:
              - id: meraki:layer7/application/5
                name: Advertising.com
            id: meraki:layer7/category/24
            name: Advertising
        applications:
          - id: meraki:layer7/application/5
            name: Advertising.com
        policyObjectGroups:
          - id: '45'
        policyObjects:
          - id: '23'
        ports:
          - '22'
          - 42-46
        services:
          - ports:
              - '80'
              - '443'
            protocol: tcp
      matchCriteria:
        - addressRanges
        - services
        - applicationCategories
        - applications
        - policyObjects
        - policyObjectGroups
        - applianceVlans
    enabled: true
    name: Allow developers
    organizationId: string
    policy: deny
    priority: 100
    ruleId: string
    rulesetId: '32'
    sources:
      criteria:
        addressRanges:
          - 1.1.1.1
          - 2.2.2.2
        applianceVlans:
          - interfaceId: L_123456789012345678_vlan_200
        policyObjectGroups:
          - id: '45'
        policyObjects:
          - id: '23'
        ports:
          - '22'
          - 42-46
      matchCriteria:
        - addressRanges
        - ports
        - policyObjects
        - policyObjectGroups
        - applianceVlans
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "ruleId": "string",
      "name": "string",
      "rulesetId": "string",
      "policy": "string",
      "enabled": true,
      "priority": 0,
      "description": "string",
      "sources": {
        "matchCriteria": [
          "string"
        ],
        "criteria": {
          "addressRanges": [
            "string"
          ],
          "ports": [
            "string"
          ],
          "policyObjects": [
            {
              "id": "string"
            }
          ],
          "policyObjectGroups": [
            {
              "id": "string"
            }
          ],
          "applianceVlans": [
            {
              "interfaceId": "string"
            }
          ],
          "siteSpecificVlans": [
            {
              "id": 0,
              "address": {
                "offsets": {
                  "ipv4": 0,
                  "ipv6": "string"
                }
              }
            }
          ]
        }
      },
      "destinations": {
        "matchCriteria": [
          "string"
        ],
        "criteria": {
          "addressRanges": [
            "string"
          ],
          "ports": [
            "string"
          ],
          "services": [
            {
              "protocol": "string",
              "ports": [
                "string"
              ]
            }
          ],
          "applicationCategories": [
            {
              "id": "string"
            }
          ],
          "applications": [
            {
              "id": "string",
              "name": "string"
            }
          ],
          "policyObjects": [
            {
              "id": "string"
            }
          ],
          "policyObjectGroups": [
            {
              "id": "string"
            }
          ],
          "applianceVlans": [
            {
              "interfaceId": "string"
            }
          ],
          "countries": [
            {
              "code": "string"
            }
          ],
          "fqdns": [
            "string"
          ],
          "siteSpecificVlans": [
            {
              "id": 0,
              "address": {
                "offsets": {
                  "ipv4": 0,
                  "ipv6": "string"
                }
              }
            }
          ]
        }
      },
      "createdAt": "string",
      "lastUpdatedAt": "string"
    }
"""
