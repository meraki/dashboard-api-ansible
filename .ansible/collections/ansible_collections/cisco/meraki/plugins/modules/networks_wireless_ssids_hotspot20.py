#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
author: Francisco Munoz (@fmunoz)
description:
  - Manage operation update of the resource networks _wireless _ssids _hotspot20.
  - Update the Hotspot 2.0 settings of an SSID.
extends_documentation_fragment:
  - cisco.meraki.module
module: networks_wireless_ssids_hotspot20
notes:
  - SDK Method used are wireless.Wireless.update_network_wireless_ssid_hotspot20,
  - Paths used are put /networks/{networkId}/wireless/ssids/{number}/hotspot20,
options:
  domains:
    description: An array of domain names.
    elements: str
    type: list
  enabled:
    description: Whether or not Hotspot 2.0 for this SSID is enabled.
    type: bool
  mccMncs:
    description: An array of MCC/MNC pairs.
    elements: dict
    suboptions:
      mcc:
        description: MCC value.
        type: str
      mnc:
        description: MNC value.
        type: str
    type: list
  naiRealms:
    description: An array of NAI realms.
    elements: dict
    suboptions:
      format:
        description: The format for the realm ('1' or '0').
        type: str
      methods:
        description: An array of EAP methods for the realm.
        elements: dict
        suboptions:
          authenticationTypes:
            description: The authentication types for the method. These should be
              formatted as an object with the EAP method category in camelcase as
              the key and the list of types as the value (nonEapInnerAuthentication
              Reserved, PAP, CHAP, MSCHAP, MSCHAPV2; eapInnerAuthentication EAP-TLS,
              EAP-SIM, EAP-AKA, EAP-TTLS with MSCHAPv2; credentials SIM, USIM, NFC
              Secure Element, Hardware Token, Softoken, Certificate, username/password,
              none, Reserved, Vendor Specific; tunneledEapMethodCredentials SIM, USIM,
              NFC Secure Element, Hardware Token, Softoken, Certificate, username/password,
              Reserved, Anonymous, Vendor Specific).
            type: dict
          id:
            description: ID of method.
            type: str
        type: list
      realm:
        description: The name of the realm.
        type: str
    type: list
  networkAccessType:
    description: The network type of this SSID ('Private network', 'Private network
      with guest access', 'Chargeable public network', 'Free public network', 'Personal
      device network', 'Emergency services only network', 'Test or experimental',
      'Wildcard').
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  number:
    description: Number path parameter.
    type: str
  operator:
    description: Operator settings for this SSID.
    suboptions:
      name:
        description: Operator name.
        type: str
    type: dict
  roamConsortOis:
    description: An array of roaming consortium OIs (hexadecimal number 3-5 octets
      in length).
    elements: str
    type: list
  venue:
    description: Venue settings for this SSID.
    suboptions:
      name:
        description: Venue name.
        type: str
      type:
        description: Venue type ('Unspecified', 'Unspecified Assembly', 'Arena', 'Stadium',
          'Passenger Terminal', 'Amphitheater', 'Amusement Park', 'Place of Worship',
          'Convention Center', 'Library', 'Museum', 'Restaurant', 'Theater', 'Bar',
          'Coffee Shop', 'Zoo or Aquarium', 'Emergency Coordination Center', 'Unspecified
          Business', 'Doctor or Dentist office', 'Bank', 'Fire Station', 'Police Station',
          'Post Office', 'Professional Office', 'Research and Development Facility',
          'Attorney Office', 'Unspecified Educational', 'School, Primary', 'School,
          Secondary', 'University or College', 'Unspecified Factory and Industrial',
          'Factory', 'Unspecified Institutional', 'Hospital', 'Long-Term Care Facility',
          'Alcohol and Drug Rehabilitation Center', 'Group Home', 'Prison or Jail',
          'Unspecified Mercantile', 'Retail Store', 'Grocery Market', 'Automotive
          Service Station', 'Shopping Mall', 'Gas Station', 'Unspecified Residential',
          'Private Residence', 'Hotel or Motel', 'Dormitory', 'Boarding House', 'Unspecified
          Storage', 'Unspecified Utility and Miscellaneous', 'Unspecified Vehicular',
          'Automobile or Truck', 'Airplane', 'Bus', 'Ferry', 'Ship or Boat', 'Train',
          'Motor Bike', 'Unspecified Outdoor', 'Muni-mesh Network', 'City Park', 'Rest
          Area', 'Traffic Control', 'Bus Stop', 'Kiosk').
        type: str
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
seealso:
  - description: Complete reference of the updateNetworkWirelessSsidHotspot20 API.
    link: https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-hotspot20
    name: Cisco Meraki documentation for wireless updateNetworkWirelessSsidHotspot20
short_description: Resource module for networks _wireless _ssids _hotspot20
version_added: 2.16.0
"""

EXAMPLES = r"""
- name: Update all
  cisco.meraki.networks_wireless_ssids_hotspot20:
    meraki_api_key: '{{ meraki_api_key }}'
    meraki_base_url: '{{ meraki_base_url }}'
    meraki_single_request_timeout: '{{ meraki_single_request_timeout }}'
    meraki_certificate_path: '{{ meraki_certificate_path }}'
    meraki_requests_proxy: '{{ meraki_requests_proxy }}'
    meraki_wait_on_rate_limit: '{{ meraki_wait_on_rate_limit }}'
    meraki_nginx_429_retry_wait_time: '{{ meraki_nginx_429_retry_wait_time }}'
    meraki_action_batch_retry_wait_time: '{{ meraki_action_batch_retry_wait_time }}'
    meraki_retry_4xx_error: '{{ meraki_retry_4xx_error }}'
    meraki_retry_4xx_error_wait_time: '{{ meraki_retry_4xx_error_wait_time }}'
    meraki_maximum_retries: '{{ meraki_maximum_retries }}'
    meraki_output_log: '{{ meraki_output_log }}'
    meraki_log_file_prefix: '{{ meraki_log_file_prefix }}'
    meraki_log_path: '{{ meraki_log_path }}'
    meraki_print_console: '{{ meraki_print_console }}'
    meraki_suppress_logging: '{{ meraki_suppress_logging }}'
    meraki_simulate: '{{ meraki_simulate }}'
    meraki_be_geo_id: '{{ meraki_be_geo_id }}'
    meraki_use_iterator_for_get_pages: '{{ meraki_use_iterator_for_get_pages }}'
    meraki_inherit_logging_config: '{{ meraki_inherit_logging_config }}'
    state: present
    domains:
      - meraki.local
      - domain2.com
    enabled: true
    mccMncs:
      - mcc: '123'
        mnc: '456'
      - mcc: '563'
        mnc: '232'
    naiRealms:
      - format: '1'
        methods:
          - authenticationTypes:
              credentials: []
              eapInnerAuthentication:
                - EAP-TTLS with MSCHAPv2
              nonEapInnerAuthentication:
                - MSCHAP
              tunneledEapMethodCredentials: []
            id: '1'
        name: Realm 1
    networkAccessType: Private network
    networkId: string
    number: string
    operator:
      name: Meraki Product Management
    roamConsortOis:
      - ABC123
      - 456EFG
    venue:
      name: SF Branch
      type: Unspecified Assembly
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
