#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: organizations_wireless_devices_provisioning_deployments
short_description: Resource module for organizations _wireless _devices _provisioning _deployments
description:
  - Manage operations create, update and delete of the resource organizations _wireless _devices _provisioning _deployments.
  - Create a zero touch deployment for a wireless access point.
  - Delete a zero touch deployment.
  - Update a zero touch deployment.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  deploymentId:
    description: DeploymentId path parameter. Deployment ID.
    type: str
  items:
    description: List of zero touch deployments to create.
    elements: dict
    suboptions:
      completedAt:
        description: Timestamp of when the zero touch deployment request was completed.
        type: str
      createdAt:
        description: Timestamp of when the zero touch deployment request was created.
        type: str
      deploymentId:
        description: Zero touch deployment request identifier.
        type: str
      devices:
        description: An array composed of old and new devices.
        suboptions:
          new:
            description: New device.
            suboptions:
              mac:
                description: MAC address of the new device.
                type: str
              model:
                description: Model of the new device.
                type: str
              name:
                description: Name of the new device or serial number if not named.
                type: str
              rfProfile:
                description: RF profile of the new device.
                suboptions:
                  id:
                    description: ID of RfProfile for new device.
                    type: str
                  name:
                    description: Name of RfProfile for new device.
                    type: str
                type: dict
              serial:
                description: Serial number of the new device.
                type: str
              tags:
                description: Tag(s) of the new device.
                elements: str
                type: list
            type: dict
          old:
            description: Old device.
            suboptions:
              afterAction:
                description: Action to be taken on the old device.
                type: str
              mac:
                description: MAC address of the old device.
                type: str
              model:
                description: Model of the old device.
                type: str
              name:
                description: Name of the old device.
                type: str
              rfProfile:
                description: RF profile of the old device.
                suboptions:
                  id:
                    description: ID of the RF profile.
                    type: str
                  name:
                    description: Name of the RF profile.
                    type: str
                type: dict
              serial:
                description: Serial number of the old device.
                type: str
              tags:
                description: Tag(s) of the old device.
                elements: str
                type: list
            type: dict
        type: dict
      errors:
        description: Array of error message(s) if any.
        elements: str
        type: list
      lastUpdatedAt:
        description: Timestamp of when the zero touch deployment request was last updated.
        type: str
      network:
        description: Network information.
        suboptions:
          id:
            description: ID of the network the device is being added to.
            type: str
          name:
            description: Name of the network the device is being added to.
            type: str
        type: dict
      requestedAt:
        description: Timestamp of when the zero touch deployment request was created.
        type: str
      status:
        description: Status of the zero touch deployment request. Enum = ready, in progress,
          completed, failed.
        type: str
      type:
        description: Type of the zero touch deployment request. Enum = deploy, replace.
        type: str
    type: list
  meta:
    description: Metadata relevant to the paginated dataset.
    suboptions:
      counts:
        description: Counts relating to the paginated dataset.
        suboptions:
          items:
            description: Counts relating to the paginated items.
            suboptions:
              remaining:
                description: The number of items in the dataset that are available on
                  subsequent pages.
                type: int
              total:
                description: The total number of items in the dataset.
                type: int
            type: dict
        type: dict
    type: dict
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco Meraki documentation for wireless createOrganizationWirelessDevicesProvisioningDeployment
    description: Complete reference of the createOrganizationWirelessDevicesProvisioningDeployment API.
    link: https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-devices-provisioning-deployment
  - name: Cisco Meraki documentation for wireless deleteOrganizationWirelessDevicesProvisioningDeployment
    description: Complete reference of the deleteOrganizationWirelessDevicesProvisioningDeployment API.
    link: https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-devices-provisioning-deployment
  - name: Cisco Meraki documentation for wireless updateOrganizationWirelessDevicesProvisioningDeployments
    description: Complete reference of the updateOrganizationWirelessDevicesProvisioningDeployments API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-devices-provisioning-deployments
notes:
  - SDK Method used are
    wireless.Wireless.create_organization_wireless_devices_provisioning_deployment,
    wireless.Wireless.delete_organization_wireless_devices_provisioning_deployment,
    wireless.Wireless.update_organization_wireless_devices_provisioning_deployments,

  - Paths used are
    post /organizations/{organizationId}/wireless/devices/provisioning/deployments,
    delete /organizations/{organizationId}/wireless/devices/provisioning/deployments/{deploymentId},
    put /organizations/{organizationId}/wireless/devices/provisioning/deployments,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_wireless_devices_provisioning_deployments:
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

    items:
      - completedAt: "2018-02-11T00:00:00.090210Z"
        createdAt: "2018-02-11T00:00:00.090210Z"
        deploymentId: "1284392014819"
        devices:
          new:
            mac: 00:11:22:33:44:55
            model: CW9166I
            name: My AP
            rfProfile:
              id: "1284392014819"
              name: RF Profile Name
            serial: Q234-ABCD-5678
            tags:
              - tag1
              - tag2
          old:
            afterAction: unclaim
            mac: 00:11:22:33:44:55
            model: MR34
            name: My AP
            rfProfile:
              id: "1284392014819"
              name: RF Profile Name
            serial: Q234-ABCD-5678
            tags:
              - tag1
              - tag2
        errors:
          - error message1
          - error message2
        lastUpdatedAt: "2018-02-11T00:00:00.090210Z"
        network:
          id: N_24329156
          name: Main Office
        requestedAt: "2018-02-11T00:00:00.090210Z"
        status: ready
        type: replace
    meta:
      counts:
        items:
          remaining: 0
          total: 20
    organizationId: string

- name: Update all
  cisco.meraki.organizations_wireless_devices_provisioning_deployments:
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

    items:
      - completedAt: "2018-02-11T00:00:00.090210Z"
        createdAt: "2018-02-11T00:00:00.090210Z"
        deploymentId: "1284392014819"
        devices:
          new:
            mac: 00:11:22:33:44:55
            model: CW9166I
            name: My AP
            rfProfile:
              id: "1284392014819"
              name: RF Profile Name
            serial: Q234-ABCD-5678
            tags:
              - tag1
              - tag2
          old:
            afterAction: unclaim
            mac: 00:11:22:33:44:55
            model: MR34
            name: My AP
            rfProfile:
              id: "1284392014819"
              name: RF Profile Name
            serial: Q234-ABCD-5678
            tags:
              - tag1
              - tag2
        errors:
          - error message1
          - error message2
        lastUpdatedAt: "2018-02-11T00:00:00.090210Z"
        network:
          id: N_24329156
          name: Main Office
        requestedAt: "2018-02-11T00:00:00.090210Z"
        status: ready
        type: replace
    meta:
      counts:
        items:
          remaining: 0
          total: 20
    organizationId: string

- name: Delete by id
  cisco.meraki.organizations_wireless_devices_provisioning_deployments:
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

    deploymentId: string
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
          "deploymentId": "string",
          "devices": {
            "old": {
              "serial": "string",
              "afterAction": "string",
              "name": "string",
              "model": "string",
              "mac": "string",
              "tags": [
                "string"
              ],
              "rfProfile": {
                "id": "string",
                "name": "string"
              }
            },
            "new": {
              "serial": "string",
              "name": "string",
              "model": "string",
              "mac": "string",
              "tags": [
                "string"
              ],
              "rfProfile": {
                "id": "string",
                "name": "string"
              }
            }
          },
          "status": "string",
          "type": "string",
          "network": {
            "id": "string",
            "name": "string"
          },
          "createdAt": "string",
          "requestedAt": "string",
          "lastUpdatedAt": "string",
          "completedAt": "string",
          "errors": [
            "string"
          ]
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
