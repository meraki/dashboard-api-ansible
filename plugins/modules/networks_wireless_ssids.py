#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_wireless_ssids
short_description: Resource module for networks _wireless _ssids
description:
- Manage operation update of the resource networks _wireless _ssids.
- Update the attributes of an MR SSID.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  activeDirectory:
    description: The current setting for Active Directory. Only valid if splashPage
      is 'Password-protected with Active Directory'.
    suboptions:
      credentials:
        description: (Optional) The credentials of the user account to be used by the
          AP to bind to your Active Directory server. The Active Directory account should
          have permissions on all your Active Directory servers. Only valid if the splashPage
          is 'Password-protected with Active Directory'.
        suboptions:
          logonName:
            description: The logon name of the Active Directory account.
            type: str
          password:
            description: The password to the Active Directory user account.
            type: str
        type: dict
      servers:
        description: The Active Directory servers to be used for authentication.
        elements: dict
        suboptions:
          host:
            description: IP address of your Active Directory server.
            type: str
          port:
            description: (Optional) UDP port the Active Directory server listens on.
              By default, uses port 3268.
            type: int
        type: list
    type: dict
  adultContentFilteringEnabled:
    description: Boolean indicating whether or not adult content will be blocked.
    type: bool
  apTagsAndVlanIds:
    description: The list of tags and VLAN IDs used for VLAN tagging. This param is
      only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'.
    elements: dict
    suboptions:
      tags:
        description: Array of AP tags.
        elements: str
        type: list
      vlanId:
        description: Numerical identifier that is assigned to the VLAN.
        type: int
    type: list
  authMode:
    description: The association control method for the SSID ('open', 'open-enhanced',
      'psk', 'open-with-radius', 'open-with-nac', '8021x-meraki', '8021x-nac', '8021x-radius',
      '8021x-google', '8021x-localradius', 'ipsk-with-radius' or 'ipsk-without-radius').
    type: str
  availabilityTags:
    description: Accepts a list of tags for this SSID. If availableOnAllAps is false,
      then the SSID will only be broadcast by APs with tags matching any of the tags
      in this list.
    elements: str
    type: list
  availableOnAllAps:
    description: Boolean indicating whether all APs should broadcast the SSID or if
      it should be restricted to APs matching any availability tags. Can only be false
      if the SSID has availability tags.
    type: bool
  bandSelection:
    description: The client-serving radio frequencies of this SSID in the default indoor
      RF profile. ('Dual band operation', '5 GHz band only' or 'Dual band operation
      with Band Steering').
    type: str
  concentratorNetworkId:
    description: The concentrator to use when the ipAssignmentMode is 'Layer 3 roaming
      with a concentrator' or 'VPN'.
    type: str
  defaultVlanId:
    description: The default VLAN ID used for 'all other APs'. This param is only valid
      when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'.
    type: int
  disassociateClientsOnVpnFailover:
    description: Disassociate clients when 'VPN' concentrator failover occurs in order
      to trigger clients to re-associate and generate new DHCP requests. This param
      is only valid if ipAssignmentMode is 'VPN'.
    type: bool
  dnsRewrite:
    description: DNS servers rewrite settings.
    suboptions:
      dnsCustomNameservers:
        description: User specified DNS servers (up to two servers).
        elements: str
        type: list
      enabled:
        description: Boolean indicating whether or not DNS server rewrite is enabled.
          If disabled, upstream DNS will be used.
        type: bool
    type: dict
  dot11r:
    description: The current setting for 802.11r.
    suboptions:
      adaptive:
        description: (Optional) Whether 802.11r is adaptive or not.
        type: bool
      enabled:
        description: Whether 802.11r is enabled or not.
        type: bool
    type: dict
  dot11w:
    description: The current setting for Protected Management Frames (802.11w).
    suboptions:
      enabled:
        description: Whether 802.11w is enabled or not.
        type: bool
      required:
        description: (Optional) Whether 802.11w is required or not.
        type: bool
    type: dict
  enabled:
    description: Whether or not the SSID is enabled.
    type: bool
  encryptionMode:
    description: The psk encryption mode for the SSID ('wep' or 'wpa'). This param is
      only valid if the authMode is 'psk'.
    type: str
  enterpriseAdminAccess:
    description: Whether or not an SSID is accessible by 'enterprise' administrators
      ('access disabled' or 'access enabled').
    type: str
  gre:
    description: Ethernet over GRE settings.
    suboptions:
      concentrator:
        description: The EoGRE concentrator's settings.
        suboptions:
          host:
            description: The EoGRE concentrator's IP or FQDN. This param is required
              when ipAssignmentMode is 'Ethernet over GRE'.
            type: str
        type: dict
      key:
        description: Optional numerical identifier that will add the GRE key field to
          the GRE header. Used to identify an individual traffic flow within a tunnel.
        type: int
    type: dict
  ipAssignmentMode:
    description: The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3
      roaming', 'Ethernet over GRE', 'Layer 3 roaming with a concentrator' or 'VPN').
    type: str
  lanIsolationEnabled:
    description: Boolean indicating whether Layer 2 LAN isolation should be enabled
      or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
    type: bool
  ldap:
    description: The current setting for LDAP. Only valid if splashPage is 'Password-protected
      with LDAP'.
    suboptions:
      baseDistinguishedName:
        description: The base distinguished name of users on the LDAP server.
        type: str
      credentials:
        description: (Optional) The credentials of the user account to be used by the
          AP to bind to your LDAP server. The LDAP account should have permissions on
          all your LDAP servers.
        suboptions:
          distinguishedName:
            description: The distinguished name of the LDAP user account (example cn=user,dc=meraki,dc=com).
            type: str
          password:
            description: The password of the LDAP user account.
            type: str
        type: dict
      serverCaCertificate:
        description: The CA certificate used to sign the LDAP server's key.
        suboptions:
          contents:
            description: The contents of the CA certificate. Must be in PEM or DER format.
            type: str
        type: dict
      servers:
        description: The LDAP servers to be used for authentication.
        elements: dict
        suboptions:
          host:
            description: IP address of your LDAP server.
            type: str
          port:
            description: UDP port the LDAP server listens on.
            type: int
        type: list
    type: dict
  localRadius:
    description: The current setting for Local Authentication, a built-in RADIUS server
      on the access point. Only valid if authMode is '8021x-localradius'.
    suboptions:
      cacheTimeout:
        description: The duration (in seconds) for which LDAP and OCSP lookups are cached.
        type: int
      certificateAuthentication:
        description: The current setting for certificate verification.
        suboptions:
          clientRootCaCertificate:
            description: The Client CA Certificate used to sign the client certificate.
            suboptions:
              contents:
                description: The contents of the Client CA Certificate. Must be in PEM
                  or DER format.
                type: str
            type: dict
          enabled:
            description: Whether or not to use EAP-TLS certificate-based authentication
              to validate wireless clients.
            type: bool
          ocspResponderUrl:
            description: (Optional) The URL of the OCSP responder to verify client certificate
              status.
            type: str
          useLdap:
            description: Whether or not to verify the certificate with LDAP.
            type: bool
          useOcsp:
            description: Whether or not to verify the certificate with OCSP.
            type: bool
        type: dict
      passwordAuthentication:
        description: The current setting for password-based authentication.
        suboptions:
          enabled:
            description: Whether or not to use EAP-TTLS/PAP or PEAP-GTC password-based
              authentication via LDAP lookup.
            type: bool
        type: dict
    type: dict
  mandatoryDhcpEnabled:
    description: If true, Mandatory DHCP will enforce that clients connecting to this
      SSID must use the IP address assigned by the DHCP server. Clients who use a static
      IP address won't be able to associate.
    type: bool
  minBitrate:
    description: The minimum bitrate in Mbps of this SSID in the default indoor RF profile.
      ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54').
    type: float
  name:
    description: The name of the SSID.
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  number:
    description: Number path parameter.
    type: str
  oauth:
    description: The OAuth settings of this SSID. Only valid if splashPage is 'Google
      OAuth'.
    suboptions:
      allowedDomains:
        description: (Optional) The list of domains allowed access to the network.
        elements: str
        type: list
    type: dict
  perClientBandwidthLimitDown:
    description: The download bandwidth limit in Kbps. (0 represents no limit.).
    type: int
  perClientBandwidthLimitUp:
    description: The upload bandwidth limit in Kbps. (0 represents no limit.).
    type: int
  perSsidBandwidthLimitDown:
    description: The total download bandwidth limit in Kbps. (0 represents no limit.).
    type: int
  perSsidBandwidthLimitUp:
    description: The total upload bandwidth limit in Kbps. (0 represents no limit.).
    type: int
  psk:
    description: The passkey for the SSID. This param is only valid if the authMode
      is 'psk'.
    type: str
  radiusAccountingEnabled:
    description: Whether or not RADIUS accounting is enabled. This param is only valid
      if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'.
    type: bool
  radiusAccountingInterimInterval:
    description: The interval (in seconds) in which accounting information is updated
      and sent to the RADIUS accounting server.
    type: int
  radiusAccountingServers:
    description: The RADIUS accounting 802.1X servers to be used for authentication.
      This param is only valid if the authMode is 'open-with-radius', '8021x-radius'
      or 'ipsk-with-radius' and radiusAccountingEnabled is 'true'.
    elements: dict
    suboptions:
      caCertificate:
        description: Certificate used for authorization for the RADSEC Server.
        type: str
      host:
        description: IP address to which the APs will send RADIUS accounting messages.
        type: str
      port:
        description: Port on the RADIUS server that is listening for accounting messages.
        type: int
      radsecEnabled:
        description: Use RADSEC (TLS over TCP) to connect to this RADIUS accounting
          server. Requires radiusProxyEnabled.
        type: bool
      secret:
        description: Shared key used to authenticate messages between the APs and RADIUS
          server.
        type: str
    type: list
  radiusAttributeForGroupPolicies:
    description: Specify the RADIUS attribute used to look up group policies ('Filter-Id',
      'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-User-Role'). Access points must
      receive this attribute in the RADIUS Access-Accept message.
    type: str
  radiusAuthenticationNasId:
    description: The template of the NAS identifier to be used for RADIUS authentication
      (ex. $NODE_MAC$ $VAP_NUM$).
    type: str
  radiusCalledStationId:
    description: The template of the called station identifier to be used for RADIUS
      (ex. $NODE_MAC$ $VAP_NUM$).
    type: str
  radiusCoaEnabled:
    description: If true, Meraki devices will act as a RADIUS Dynamic Authorization
      Server and will respond to RADIUS Change-of-Authorization and Disconnect messages
      sent by the RADIUS server.
    type: bool
  radiusFailoverPolicy:
    description: This policy determines how authentication requests should be handled
      in the event that all of the configured RADIUS servers are unreachable ('Deny
      access' or 'Allow access').
    type: str
  radiusFallbackEnabled:
    description: Whether or not higher priority RADIUS servers should be retried after
      60 seconds.
    type: bool
  radiusGuestVlanEnabled:
    description: Whether or not RADIUS Guest VLAN is enabled. This param is only valid
      if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated'
      or 'nat' mode.
    type: bool
  radiusGuestVlanId:
    description: VLAN ID of the RADIUS Guest VLAN. This param is only valid if the authMode
      is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode.
    type: int
  radiusLoadBalancingPolicy:
    description: This policy determines which RADIUS server will be contacted first
      in an authentication attempt and the ordering of any necessary retry attempts
      ('Strict priority order' or 'Round robin').
    type: str
  radiusOverride:
    description: If true, the RADIUS response can override VLAN tag. This is not valid
      when ipAssignmentMode is 'NAT mode'.
    type: bool
  radiusProxyEnabled:
    description: If true, Meraki devices will proxy RADIUS messages through the Meraki
      cloud to the configured RADIUS auth and accounting servers.
    type: bool
  radiusServerAttemptsLimit:
    description: The maximum number of transmit attempts after which a RADIUS server
      is failed over (must be between 1-5).
    type: int
  radiusServerTimeout:
    description: The amount of time for which a RADIUS client waits for a reply from
      the RADIUS server (must be between 1-10 seconds).
    type: int
  radiusServers:
    description: The RADIUS 802.1X servers to be used for authentication. This param
      is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'.
    elements: dict
    suboptions:
      caCertificate:
        description: Certificate used for authorization for the RADSEC Server.
        type: str
      host:
        description: IP address of your RADIUS server.
        type: str
      openRoamingCertificateId:
        description: The ID of the Openroaming Certificate attached to radius server.
        type: int
      port:
        description: UDP port the RADIUS server listens on for Access-requests.
        type: int
      radsecEnabled:
        description: Use RADSEC (TLS over TCP) to connect to this RADIUS server. Requires
          radiusProxyEnabled.
        type: bool
      secret:
        description: RADIUS client shared secret.
        type: str
    type: list
  radiusTestingEnabled:
    description: If true, Meraki devices will periodically send Access-Request messages
      to configured RADIUS servers using identity 'meraki_8021x_test' to ensure that
      the RADIUS servers are reachable.
    type: bool
  secondaryConcentratorNetworkId:
    description: The secondary concentrator to use when the ipAssignmentMode is 'VPN'.
      If configured, the APs will switch to using this concentrator if the primary concentrator
      is unreachable. This param is optional. ('disabled' represents no secondary concentrator.).
    type: str
  speedBurst:
    description: The SpeedBurst setting for this SSID'.
    suboptions:
      enabled:
        description: Boolean indicating whether or not to allow users to temporarily
          exceed the bandwidth limit for short periods while still keeping them under
          the bandwidth limit over time.
        type: bool
    type: dict
  splashGuestSponsorDomains:
    description: Array of valid sponsor email domains for sponsored guest splash type.
    elements: str
    type: list
  splashPage:
    description: The type of splash page for the SSID ('None', 'Click-through splash
      page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected
      with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected
      with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi',
      'Google OAuth', 'Sponsored guest', 'Cisco ISE' or 'Google Apps domain'). This
      attribute is not supported for template children.
    type: str
  useVlanTagging:
    description: Whether or not traffic should be directed to use specific VLANs. This
      param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'.
    type: bool
  visible:
    description: Boolean indicating whether APs should advertise or hide this SSID.
      APs will only broadcast this SSID if set to true.
    type: bool
  vlanId:
    description: The VLAN ID used for VLAN tagging. This param is only valid when the
      ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
    type: int
  walledGardenEnabled:
    description: Allow access to a configurable list of IP ranges, which users may access
      prior to sign-on.
    type: bool
  walledGardenRanges:
    description: Specify your walled garden by entering an array of addresses, ranges
      using CIDR notation, domain names, and domain wildcards (e.g. '192.168.1.1/24',
      '192.168.37.10/32', 'www.yahoo.com', '*.google.com'). Meraki's splash page is
      automatically included in your walled garden.
    elements: str
    type: list
  wpaEncryptionMode:
    description: The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only',
      'WPA3 Transition Mode', 'WPA3 only' or 'WPA3 192-bit Security').
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for wireless updateNetworkWirelessSsid
  description: Complete reference of the updateNetworkWirelessSsid API.
  link: https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid
notes:
  - SDK Method used are
    wireless.Wireless.update_network_wireless_ssid,

  - Paths used are
    put /networks/{networkId}/wireless/ssids/{number},
"""

EXAMPLES = r"""
- name: Update by id
  cisco.meraki.networks_wireless_ssids:
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
    enabled: true
    name: My SSID
    networkId: string
    number: string

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
