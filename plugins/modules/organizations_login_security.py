#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: organizations_login_security
short_description: Resource module for organizations _login _security
description:
- Manage operation update of the resource organizations _login _security.
- Update the login security settings for an organization.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  accountLockoutAttempts:
    description: Number of consecutive failed login attempts after which users' accounts
      will be locked.
    type: int
  apiAuthentication:
    description: Details for indicating whether organization will restrict access to
      API (but not Dashboard) to certain IP addresses.
    suboptions:
      ipRestrictionsForKeys:
        description: Details for API-only IP restrictions.
        suboptions:
          enabled:
            description: Boolean indicating whether the organization will restrict API
              key (not Dashboard GUI) usage to a specific list of IP addresses or CIDR
              ranges.
            type: bool
          ranges:
            description: List of acceptable IP ranges. Entries can be single IP addresses,
              IP address ranges, and CIDR subnets.
            elements: str
            type: list
        type: dict
    type: dict
  enforceAccountLockout:
    description: Boolean indicating whether users' Dashboard accounts will be locked
      out after a specified number of consecutive failed login attempts.
    type: bool
  enforceDifferentPasswords:
    description: Boolean indicating whether users, when setting a new password, are
      forced to choose a new password that is different from any past passwords.
    type: bool
  enforceIdleTimeout:
    description: Boolean indicating whether users will be logged out after being idle
      for the specified number of minutes.
    type: bool
  enforceLoginIpRanges:
    description: Boolean indicating whether organization will restrict access to Dashboard
      (including the API) from certain IP addresses.
    type: bool
  enforcePasswordExpiration:
    description: Boolean indicating whether users are forced to change their password
      every X number of days.
    type: bool
  enforceStrongPasswords:
    description: Boolean indicating whether users will be forced to choose strong passwords
      for their accounts. Strong passwords are at least 8 characters that contain 3
      of the following number, uppercase letter, lowercase letter, and symbol.
    type: bool
  enforceTwoFactorAuth:
    description: Boolean indicating whether users in this organization will be required
      to use an extra verification code when logging in to Dashboard. This code will
      be sent to their mobile phone via SMS, or can be generated by the authenticator
      application.
    type: bool
  idleTimeoutMinutes:
    description: Number of minutes users can remain idle before being logged out of
      their accounts.
    type: int
  loginIpRanges:
    description: List of acceptable IP ranges. Entries can be single IP addresses, IP
      address ranges, and CIDR subnets.
    elements: str
    type: list
  numDifferentPasswords:
    description: Number of recent passwords that new password must be distinct from.
    type: int
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
  passwordExpirationDays:
    description: Number of days after which users will be forced to change their password.
    type: int
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for organizations updateOrganizationLoginSecurity
  description: Complete reference of the updateOrganizationLoginSecurity API.
  link: https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security
notes:
  - SDK Method used are
    organizations.Organizations.update_organization_login_security,

  - Paths used are
    put /organizations/{organizationId}/loginSecurity,
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.organizations_login_security:
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
    state: present
    accountLockoutAttempts: 3
    apiAuthentication:
      ipRestrictionsForKeys:
        enabled: true
        ranges:
        - 192.195.83.1
        - 192.168.33.33
    enforceAccountLockout: true
    enforceDifferentPasswords: true
    enforceIdleTimeout: true
    enforceLoginIpRanges: true
    enforcePasswordExpiration: true
    enforceStrongPasswords: true
    enforceTwoFactorAuth: true
    idleTimeoutMinutes: 30
    loginIpRanges:
    - 192.195.83.1
    - 192.195.83.255
    numDifferentPasswords: 3
    organizationId: string
    passwordExpirationDays: 90

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {
      "accountLockoutAttempts": 0,
      "apiAuthentication": {
        "ipRestrictionsForKeys": {
          "enabled": true,
          "ranges": [
            "string"
          ]
        }
      },
      "enforceAccountLockout": true,
      "enforceDifferentPasswords": true,
      "enforceIdleTimeout": true,
      "enforceLoginIpRanges": true,
      "enforcePasswordExpiration": true,
      "enforceStrongPasswords": true,
      "enforceTwoFactorAuth": true,
      "idleTimeoutMinutes": 0,
      "loginIpRanges": [
        "string"
      ],
      "numDifferentPasswords": 0,
      "passwordExpirationDays": 0
    }
"""
