#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.meraki.plugins.plugin_utils.meraki import (
    MERAKI,
    meraki_argument_spec,
    meraki_compare_equality,
    get_dict_result,
)
from ansible_collections.cisco.meraki.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = meraki_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present"]),
    name=dict(type="str"),
    enabled=dict(type="bool"),
    authMode=dict(type="str"),
    enterpriseAdminAccess=dict(type="str"),
    encryptionMode=dict(type="str"),
    psk=dict(type="str"),
    wpaEncryptionMode=dict(type="str"),
    dot11w=dict(type="dict"),
    dot11r=dict(type="dict"),
    splashPage=dict(type="str"),
    splashGuestSponsorDomains=dict(type="list"),
    oauth=dict(type="dict"),
    localRadius=dict(type="dict"),
    ldap=dict(type="dict"),
    activeDirectory=dict(type="dict"),
    radiusServers=dict(type="list"),
    radiusProxyEnabled=dict(type="bool"),
    radiusTestingEnabled=dict(type="bool"),
    radiusCalledStationId=dict(type="str"),
    radiusAuthenticationNasId=dict(type="str"),
    radiusServerTimeout=dict(type="int"),
    radiusServerAttemptsLimit=dict(type="int"),
    radiusFallbackEnabled=dict(type="bool"),
    radiusCoaEnabled=dict(type="bool"),
    radiusFailoverPolicy=dict(type="str"),
    radiusLoadBalancingPolicy=dict(type="str"),
    radiusAccountingEnabled=dict(type="bool"),
    radiusAccountingServers=dict(type="list"),
    radiusAccountingInterimInterval=dict(type="int"),
    radiusAttributeForGroupPolicies=dict(type="str"),
    ipAssignmentMode=dict(type="str"),
    useVlanTagging=dict(type="bool"),
    concentratorNetworkId=dict(type="str"),
    secondaryConcentratorNetworkId=dict(type="str"),
    disassociateClientsOnVpnFailover=dict(type="bool"),
    vlanId=dict(type="int"),
    defaultVlanId=dict(type="int"),
    apTagsAndVlanIds=dict(type="list"),
    walledGardenEnabled=dict(type="bool"),
    walledGardenRanges=dict(type="list"),
    gre=dict(type="dict"),
    radiusOverride=dict(type="bool"),
    radiusGuestVlanEnabled=dict(type="bool"),
    radiusGuestVlanId=dict(type="int"),
    minBitrate=dict(type="float"),
    bandSelection=dict(type="str"),
    perClientBandwidthLimitUp=dict(type="int"),
    perClientBandwidthLimitDown=dict(type="int"),
    perSsidBandwidthLimitUp=dict(type="int"),
    perSsidBandwidthLimitDown=dict(type="int"),
    lanIsolationEnabled=dict(type="bool"),
    visible=dict(type="bool"),
    availableOnAllAps=dict(type="bool"),
    availabilityTags=dict(type="list"),
    mandatoryDhcpEnabled=dict(type="bool"),
    adultContentFilteringEnabled=dict(type="bool"),
    dnsRewrite=dict(type="dict"),
    speedBurst=dict(type="dict"),
    networkId=dict(type="str"),
    number=dict(type="str"),
))

required_if = [
    ("state", "present", ["name", "networkId", "number"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NetworksWirelessSsids(object):
    def __init__(self, params, meraki):
        self.meraki = meraki
        self.new_object = dict(
            name=params.get("name"),
            enabled=params.get("enabled"),
            authMode=params.get("authMode"),
            enterpriseAdminAccess=params.get("enterpriseAdminAccess"),
            encryptionMode=params.get("encryptionMode"),
            psk=params.get("psk"),
            wpaEncryptionMode=params.get("wpaEncryptionMode"),
            dot11w=params.get("dot11w"),
            dot11r=params.get("dot11r"),
            splashPage=params.get("splashPage"),
            splashGuestSponsorDomains=params.get("splashGuestSponsorDomains"),
            oauth=params.get("oauth"),
            localRadius=params.get("localRadius"),
            ldap=params.get("ldap"),
            activeDirectory=params.get("activeDirectory"),
            radiusServers=params.get("radiusServers"),
            radiusProxyEnabled=params.get("radiusProxyEnabled"),
            radiusTestingEnabled=params.get("radiusTestingEnabled"),
            radiusCalledStationId=params.get("radiusCalledStationId"),
            radiusAuthenticationNasId=params.get("radiusAuthenticationNasId"),
            radiusServerTimeout=params.get("radiusServerTimeout"),
            radiusServerAttemptsLimit=params.get("radiusServerAttemptsLimit"),
            radiusFallbackEnabled=params.get("radiusFallbackEnabled"),
            radiusCoaEnabled=params.get("radiusCoaEnabled"),
            radiusFailoverPolicy=params.get("radiusFailoverPolicy"),
            radiusLoadBalancingPolicy=params.get("radiusLoadBalancingPolicy"),
            radiusAccountingEnabled=params.get("radiusAccountingEnabled"),
            radiusAccountingServers=params.get("radiusAccountingServers"),
            radiusAccountingInterimInterval=params.get("radiusAccountingInterimInterval"),
            radiusAttributeForGroupPolicies=params.get("radiusAttributeForGroupPolicies"),
            ipAssignmentMode=params.get("ipAssignmentMode"),
            useVlanTagging=params.get("useVlanTagging"),
            concentratorNetworkId=params.get("concentratorNetworkId"),
            secondaryConcentratorNetworkId=params.get("secondaryConcentratorNetworkId"),
            disassociateClientsOnVpnFailover=params.get("disassociateClientsOnVpnFailover"),
            vlanId=params.get("vlanId"),
            defaultVlanId=params.get("defaultVlanId"),
            apTagsAndVlanIds=params.get("apTagsAndVlanIds"),
            walledGardenEnabled=params.get("walledGardenEnabled"),
            walledGardenRanges=params.get("walledGardenRanges"),
            gre=params.get("gre"),
            radiusOverride=params.get("radiusOverride"),
            radiusGuestVlanEnabled=params.get("radiusGuestVlanEnabled"),
            radiusGuestVlanId=params.get("radiusGuestVlanId"),
            minBitrate=params.get("minBitrate"),
            bandSelection=params.get("bandSelection"),
            perClientBandwidthLimitUp=params.get("perClientBandwidthLimitUp"),
            perClientBandwidthLimitDown=params.get("perClientBandwidthLimitDown"),
            perSsidBandwidthLimitUp=params.get("perSsidBandwidthLimitUp"),
            perSsidBandwidthLimitDown=params.get("perSsidBandwidthLimitDown"),
            lanIsolationEnabled=params.get("lanIsolationEnabled"),
            visible=params.get("visible"),
            availableOnAllAps=params.get("availableOnAllAps"),
            availabilityTags=params.get("availabilityTags"),
            mandatoryDhcpEnabled=params.get("mandatoryDhcpEnabled"),
            adultContentFilteringEnabled=params.get("adultContentFilteringEnabled"),
            dnsRewrite=params.get("dnsRewrite"),
            speedBurst=params.get("speedBurst"),
            network_id=params.get("networkId"),
            number=params.get("number"),
        )

    def get_all_params(self, name=None, id=None):
        new_object_params = {}
        if self.new_object.get('networkId') is not None or self.new_object.get('network_id') is not None:
            new_object_params['networkId'] = self.new_object.get('networkId') or \
                self.new_object.get('network_id')
        return new_object_params

    def get_params_by_id(self, name=None, id=None):
        new_object_params = {}
        if self.new_object.get('networkId') is not None or self.new_object.get('network_id') is not None:
            new_object_params['networkId'] = self.new_object.get('networkId') or \
                self.new_object.get('network_id')
        if self.new_object.get('number') is not None or self.new_object.get('number') is not None:
            new_object_params['number'] = self.new_object.get('number')
        return new_object_params

    def update_by_id_params(self):
        new_object_params = {}
        if self.new_object.get('name') is not None or self.new_object.get('name') is not None:
            new_object_params['name'] = self.new_object.get('name') or \
                self.new_object.get('name')
        if self.new_object.get('enabled') is not None or self.new_object.get('enabled') is not None:
            new_object_params['enabled'] = self.new_object.get('enabled')
        if self.new_object.get('authMode') is not None or self.new_object.get('auth_mode') is not None:
            new_object_params['authMode'] = self.new_object.get('authMode') or \
                self.new_object.get('auth_mode')
        if self.new_object.get('enterpriseAdminAccess') is not None or self.new_object.get('enterprise_admin_access') is not None:
            new_object_params['enterpriseAdminAccess'] = self.new_object.get('enterpriseAdminAccess') or \
                self.new_object.get('enterprise_admin_access')
        if self.new_object.get('encryptionMode') is not None or self.new_object.get('encryption_mode') is not None:
            new_object_params['encryptionMode'] = self.new_object.get('encryptionMode') or \
                self.new_object.get('encryption_mode')
        if self.new_object.get('psk') is not None or self.new_object.get('psk') is not None:
            new_object_params['psk'] = self.new_object.get('psk') or \
                self.new_object.get('psk')
        if self.new_object.get('wpaEncryptionMode') is not None or self.new_object.get('wpa_encryption_mode') is not None:
            new_object_params['wpaEncryptionMode'] = self.new_object.get('wpaEncryptionMode') or \
                self.new_object.get('wpa_encryption_mode')
        if self.new_object.get('dot11w') is not None or self.new_object.get('dot11w') is not None:
            new_object_params['dot11w'] = self.new_object.get('dot11w') or \
                self.new_object.get('dot11w')
        if self.new_object.get('dot11r') is not None or self.new_object.get('dot11r') is not None:
            new_object_params['dot11r'] = self.new_object.get('dot11r') or \
                self.new_object.get('dot11r')
        if self.new_object.get('splashPage') is not None or self.new_object.get('splash_page') is not None:
            new_object_params['splashPage'] = self.new_object.get('splashPage') or \
                self.new_object.get('splash_page')
        if self.new_object.get('splashGuestSponsorDomains') is not None or self.new_object.get('splash_guest_sponsor_domains') is not None:
            new_object_params['splashGuestSponsorDomains'] = self.new_object.get('splashGuestSponsorDomains') or \
                self.new_object.get('splash_guest_sponsor_domains')
        if self.new_object.get('oauth') is not None or self.new_object.get('oauth') is not None:
            new_object_params['oauth'] = self.new_object.get('oauth') or \
                self.new_object.get('oauth')
        if self.new_object.get('localRadius') is not None or self.new_object.get('local_radius') is not None:
            new_object_params['localRadius'] = self.new_object.get('localRadius') or \
                self.new_object.get('local_radius')
        if self.new_object.get('ldap') is not None or self.new_object.get('ldap') is not None:
            new_object_params['ldap'] = self.new_object.get('ldap') or \
                self.new_object.get('ldap')
        if self.new_object.get('activeDirectory') is not None or self.new_object.get('active_directory') is not None:
            new_object_params['activeDirectory'] = self.new_object.get('activeDirectory') or \
                self.new_object.get('active_directory')
        if self.new_object.get('radiusServers') is not None or self.new_object.get('radius_servers') is not None:
            new_object_params['radiusServers'] = self.new_object.get('radiusServers') or \
                self.new_object.get('radius_servers')
        if self.new_object.get('radiusProxyEnabled') is not None or self.new_object.get('radius_proxy_enabled') is not None:
            new_object_params['radiusProxyEnabled'] = self.new_object.get('radiusProxyEnabled')
        if self.new_object.get('radiusTestingEnabled') is not None or self.new_object.get('radius_testing_enabled') is not None:
            new_object_params['radiusTestingEnabled'] = self.new_object.get('radiusTestingEnabled')
        if self.new_object.get('radiusCalledStationId') is not None or self.new_object.get('radius_called_station_id') is not None:
            new_object_params['radiusCalledStationId'] = self.new_object.get('radiusCalledStationId') or \
                self.new_object.get('radius_called_station_id')
        if self.new_object.get('radiusAuthenticationNasId') is not None or self.new_object.get('radius_authentication_nas_id') is not None:
            new_object_params['radiusAuthenticationNasId'] = self.new_object.get('radiusAuthenticationNasId') or \
                self.new_object.get('radius_authentication_nas_id')
        if self.new_object.get('radiusServerTimeout') is not None or self.new_object.get('radius_server_timeout') is not None:
            new_object_params['radiusServerTimeout'] = self.new_object.get('radiusServerTimeout') or \
                self.new_object.get('radius_server_timeout')
        if self.new_object.get('radiusServerAttemptsLimit') is not None or self.new_object.get('radius_server_attempts_limit') is not None:
            new_object_params['radiusServerAttemptsLimit'] = self.new_object.get('radiusServerAttemptsLimit') or \
                self.new_object.get('radius_server_attempts_limit')
        if self.new_object.get('radiusFallbackEnabled') is not None or self.new_object.get('radius_fallback_enabled') is not None:
            new_object_params['radiusFallbackEnabled'] = self.new_object.get('radiusFallbackEnabled')
        if self.new_object.get('radiusCoaEnabled') is not None or self.new_object.get('radius_coa_enabled') is not None:
            new_object_params['radiusCoaEnabled'] = self.new_object.get('radiusCoaEnabled')
        if self.new_object.get('radiusFailoverPolicy') is not None or self.new_object.get('radius_failover_policy') is not None:
            new_object_params['radiusFailoverPolicy'] = self.new_object.get('radiusFailoverPolicy') or \
                self.new_object.get('radius_failover_policy')
        if self.new_object.get('radiusLoadBalancingPolicy') is not None or self.new_object.get('radius_load_balancing_policy') is not None:
            new_object_params['radiusLoadBalancingPolicy'] = self.new_object.get('radiusLoadBalancingPolicy') or \
                self.new_object.get('radius_load_balancing_policy')
        if self.new_object.get('radiusAccountingEnabled') is not None or self.new_object.get('radius_accounting_enabled') is not None:
            new_object_params['radiusAccountingEnabled'] = self.new_object.get('radiusAccountingEnabled')
        if self.new_object.get('radiusAccountingServers') is not None or self.new_object.get('radius_accounting_servers') is not None:
            new_object_params['radiusAccountingServers'] = self.new_object.get('radiusAccountingServers') or \
                self.new_object.get('radius_accounting_servers')
        if self.new_object.get('radiusAccountingInterimInterval') is not None or self.new_object.get('radius_accounting_interim_interval') is not None:
            new_object_params['radiusAccountingInterimInterval'] = self.new_object.get('radiusAccountingInterimInterval') or \
                self.new_object.get('radius_accounting_interim_interval')
        if self.new_object.get('radiusAttributeForGroupPolicies') is not None or self.new_object.get('radius_attribute_for_group_policies') is not None:
            new_object_params['radiusAttributeForGroupPolicies'] = self.new_object.get('radiusAttributeForGroupPolicies') or \
                self.new_object.get('radius_attribute_for_group_policies')
        if self.new_object.get('ipAssignmentMode') is not None or self.new_object.get('ip_assignment_mode') is not None:
            new_object_params['ipAssignmentMode'] = self.new_object.get('ipAssignmentMode') or \
                self.new_object.get('ip_assignment_mode')
        if self.new_object.get('useVlanTagging') is not None or self.new_object.get('use_vlan_tagging') is not None:
            new_object_params['useVlanTagging'] = self.new_object.get('useVlanTagging')
        if self.new_object.get('concentratorNetworkId') is not None or self.new_object.get('concentrator_network_id') is not None:
            new_object_params['concentratorNetworkId'] = self.new_object.get('concentratorNetworkId') or \
                self.new_object.get('concentrator_network_id')
        if self.new_object.get('secondaryConcentratorNetworkId') is not None or self.new_object.get('secondary_concentrator_network_id') is not None:
            new_object_params['secondaryConcentratorNetworkId'] = self.new_object.get('secondaryConcentratorNetworkId') or \
                self.new_object.get('secondary_concentrator_network_id')
        if self.new_object.get('disassociateClientsOnVpnFailover') is not None or self.new_object.get('disassociate_clients_on_vpn_failover') is not None:
            new_object_params['disassociateClientsOnVpnFailover'] = self.new_object.get('disassociateClientsOnVpnFailover')
        if self.new_object.get('vlanId') is not None or self.new_object.get('vlan_id') is not None:
            new_object_params['vlanId'] = self.new_object.get('vlanId') or \
                self.new_object.get('vlan_id')
        if self.new_object.get('defaultVlanId') is not None or self.new_object.get('default_vlan_id') is not None:
            new_object_params['defaultVlanId'] = self.new_object.get('defaultVlanId') or \
                self.new_object.get('default_vlan_id')
        if self.new_object.get('apTagsAndVlanIds') is not None or self.new_object.get('ap_tags_and_vlan_ids') is not None:
            new_object_params['apTagsAndVlanIds'] = self.new_object.get('apTagsAndVlanIds') or \
                self.new_object.get('ap_tags_and_vlan_ids')
        if self.new_object.get('walledGardenEnabled') is not None or self.new_object.get('walled_garden_enabled') is not None:
            new_object_params['walledGardenEnabled'] = self.new_object.get('walledGardenEnabled')
        if self.new_object.get('walledGardenRanges') is not None or self.new_object.get('walled_garden_ranges') is not None:
            new_object_params['walledGardenRanges'] = self.new_object.get('walledGardenRanges') or \
                self.new_object.get('walled_garden_ranges')
        if self.new_object.get('gre') is not None or self.new_object.get('gre') is not None:
            new_object_params['gre'] = self.new_object.get('gre') or \
                self.new_object.get('gre')
        if self.new_object.get('radiusOverride') is not None or self.new_object.get('radius_override') is not None:
            new_object_params['radiusOverride'] = self.new_object.get('radiusOverride')
        if self.new_object.get('radiusGuestVlanEnabled') is not None or self.new_object.get('radius_guest_vlan_enabled') is not None:
            new_object_params['radiusGuestVlanEnabled'] = self.new_object.get('radiusGuestVlanEnabled')
        if self.new_object.get('radiusGuestVlanId') is not None or self.new_object.get('radius_guest_vlan_id') is not None:
            new_object_params['radiusGuestVlanId'] = self.new_object.get('radiusGuestVlanId') or \
                self.new_object.get('radius_guest_vlan_id')
        if self.new_object.get('minBitrate') is not None or self.new_object.get('min_bitrate') is not None:
            new_object_params['minBitrate'] = self.new_object.get('minBitrate') or \
                self.new_object.get('min_bitrate')
        if self.new_object.get('bandSelection') is not None or self.new_object.get('band_selection') is not None:
            new_object_params['bandSelection'] = self.new_object.get('bandSelection') or \
                self.new_object.get('band_selection')
        if self.new_object.get('perClientBandwidthLimitUp') is not None or self.new_object.get('per_client_bandwidth_limit_up') is not None:
            new_object_params['perClientBandwidthLimitUp'] = self.new_object.get('perClientBandwidthLimitUp') or \
                self.new_object.get('per_client_bandwidth_limit_up')
        if self.new_object.get('perClientBandwidthLimitDown') is not None or self.new_object.get('per_client_bandwidth_limit_down') is not None:
            new_object_params['perClientBandwidthLimitDown'] = self.new_object.get('perClientBandwidthLimitDown') or \
                self.new_object.get('per_client_bandwidth_limit_down')
        if self.new_object.get('perSsidBandwidthLimitUp') is not None or self.new_object.get('per_ssid_bandwidth_limit_up') is not None:
            new_object_params['perSsidBandwidthLimitUp'] = self.new_object.get('perSsidBandwidthLimitUp') or \
                self.new_object.get('per_ssid_bandwidth_limit_up')
        if self.new_object.get('perSsidBandwidthLimitDown') is not None or self.new_object.get('per_ssid_bandwidth_limit_down') is not None:
            new_object_params['perSsidBandwidthLimitDown'] = self.new_object.get('perSsidBandwidthLimitDown') or \
                self.new_object.get('per_ssid_bandwidth_limit_down')
        if self.new_object.get('lanIsolationEnabled') is not None or self.new_object.get('lan_isolation_enabled') is not None:
            new_object_params['lanIsolationEnabled'] = self.new_object.get('lanIsolationEnabled')
        if self.new_object.get('visible') is not None or self.new_object.get('visible') is not None:
            new_object_params['visible'] = self.new_object.get('visible')
        if self.new_object.get('availableOnAllAps') is not None or self.new_object.get('available_on_all_aps') is not None:
            new_object_params['availableOnAllAps'] = self.new_object.get('availableOnAllAps')
        if self.new_object.get('availabilityTags') is not None or self.new_object.get('availability_tags') is not None:
            new_object_params['availabilityTags'] = self.new_object.get('availabilityTags') or \
                self.new_object.get('availability_tags')
        if self.new_object.get('mandatoryDhcpEnabled') is not None or self.new_object.get('mandatory_dhcp_enabled') is not None:
            new_object_params['mandatoryDhcpEnabled'] = self.new_object.get('mandatoryDhcpEnabled')
        if self.new_object.get('adultContentFilteringEnabled') is not None or self.new_object.get('adult_content_filtering_enabled') is not None:
            new_object_params['adultContentFilteringEnabled'] = self.new_object.get('adultContentFilteringEnabled')
        if self.new_object.get('dnsRewrite') is not None or self.new_object.get('dns_rewrite') is not None:
            new_object_params['dnsRewrite'] = self.new_object.get('dnsRewrite') or \
                self.new_object.get('dns_rewrite')
        if self.new_object.get('speedBurst') is not None or self.new_object.get('speed_burst') is not None:
            new_object_params['speedBurst'] = self.new_object.get('speedBurst') or \
                self.new_object.get('speed_burst')
        if self.new_object.get('networkId') is not None or self.new_object.get('network_id') is not None:
            new_object_params['networkId'] = self.new_object.get('networkId') or \
                self.new_object.get('network_id')
        if self.new_object.get('number') is not None or self.new_object.get('number') is not None:
            new_object_params['number'] = self.new_object.get('number') or \
                self.new_object.get('number')
        return new_object_params

    def get_object_by_name(self, name):
        result = None
        # NOTE: Does not have a get by name method, using get all
        try:
            items = self.meraki.exec_meraki(
                family="wireless",
                function="getNetworkWirelessSsids",
                params=self.get_all_params(name=name),
            )
            if isinstance(items, dict):
                if 'response' in items:
                    items = items.get('response')
            result = get_dict_result(items, 'name', name)
            if result is None:
                result = items
        except Exception as e:
            print("Error: ", e)
            result = None
        return result

    def get_object_by_id(self, id):
        result = None
        try:
            items = self.meraki.exec_meraki(
                family="wireless",
                function="getNetworkWirelessSsid",
                params=self.get_params_by_id()
            )
            if isinstance(items, dict):
                if 'response' in items:
                    items = items.get('response')
            result = items
        except Exception as e:
            print("Error: ", e)
            result = None
        return result

    def exists(self):
        prev_obj = None
        id_exists = False
        name_exists = False
        o_id = self.new_object.get("networkId") or self.new_object.get("network_id")
        o_id = o_id or self.new_object.get(
            "number") or self.new_object.get("number")
        name = o_id or self.new_object.get("name")
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            _id = _id or prev_obj.get("number")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters(
                    "The 'id' and 'name' params don't refer to the same object")
            if _id:
                self.new_object.update(dict(id=_id))
                self.new_object.update(dict(number=_id))
            if _id:
                prev_obj = self.get_object_by_id(_id)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("name", "name"),
            ("enabled", "enabled"),
            ("authMode", "authMode"),
            ("enterpriseAdminAccess", "enterpriseAdminAccess"),
            ("encryptionMode", "encryptionMode"),
            ("psk", "psk"),
            ("wpaEncryptionMode", "wpaEncryptionMode"),
            ("dot11w", "dot11w"),
            ("dot11r", "dot11r"),
            ("splashPage", "splashPage"),
            ("splashGuestSponsorDomains", "splashGuestSponsorDomains"),
            ("oauth", "oauth"),
            ("localRadius", "localRadius"),
            ("ldap", "ldap"),
            ("activeDirectory", "activeDirectory"),
            ("radiusServers", "radiusServers"),
            ("radiusProxyEnabled", "radiusProxyEnabled"),
            ("radiusTestingEnabled", "radiusTestingEnabled"),
            ("radiusCalledStationId", "radiusCalledStationId"),
            ("radiusAuthenticationNasId", "radiusAuthenticationNasId"),
            ("radiusServerTimeout", "radiusServerTimeout"),
            ("radiusServerAttemptsLimit", "radiusServerAttemptsLimit"),
            ("radiusFallbackEnabled", "radiusFallbackEnabled"),
            ("radiusCoaEnabled", "radiusCoaEnabled"),
            ("radiusFailoverPolicy", "radiusFailoverPolicy"),
            ("radiusLoadBalancingPolicy", "radiusLoadBalancingPolicy"),
            ("radiusAccountingEnabled", "radiusAccountingEnabled"),
            ("radiusAccountingServers", "radiusAccountingServers"),
            ("radiusAccountingInterimInterval", "radiusAccountingInterimInterval"),
            ("radiusAttributeForGroupPolicies", "radiusAttributeForGroupPolicies"),
            ("ipAssignmentMode", "ipAssignmentMode"),
            ("useVlanTagging", "useVlanTagging"),
            ("concentratorNetworkId", "concentratorNetworkId"),
            ("secondaryConcentratorNetworkId", "secondaryConcentratorNetworkId"),
            ("disassociateClientsOnVpnFailover", "disassociateClientsOnVpnFailover"),
            ("vlanId", "vlanId"),
            ("defaultVlanId", "defaultVlanId"),
            ("apTagsAndVlanIds", "apTagsAndVlanIds"),
            ("walledGardenEnabled", "walledGardenEnabled"),
            ("walledGardenRanges", "walledGardenRanges"),
            ("gre", "gre"),
            ("radiusOverride", "radiusOverride"),
            ("radiusGuestVlanEnabled", "radiusGuestVlanEnabled"),
            ("radiusGuestVlanId", "radiusGuestVlanId"),
            ("minBitrate", "minBitrate"),
            ("bandSelection", "bandSelection"),
            ("perClientBandwidthLimitUp", "perClientBandwidthLimitUp"),
            ("perClientBandwidthLimitDown", "perClientBandwidthLimitDown"),
            ("perSsidBandwidthLimitUp", "perSsidBandwidthLimitUp"),
            ("perSsidBandwidthLimitDown", "perSsidBandwidthLimitDown"),
            ("lanIsolationEnabled", "lanIsolationEnabled"),
            ("visible", "visible"),
            ("availableOnAllAps", "availableOnAllAps"),
            ("availabilityTags", "availabilityTags"),
            ("mandatoryDhcpEnabled", "mandatoryDhcpEnabled"),
            ("adultContentFilteringEnabled", "adultContentFilteringEnabled"),
            ("dnsRewrite", "dnsRewrite"),
            ("speedBurst", "speedBurst"),
            ("networkId", "networkId"),
            ("number", "number"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        current_obj["number"] = str(current_obj.get("number"))
        return any(not meraki_compare_equality(current_obj.get(meraki_param),
                                               requested_obj.get(ansible_param))
                   for (meraki_param, ansible_param) in obj_params)

    def update(self):
        id = self.new_object.get("id")
        id = id or self.new_object.get("number")
        name = self.new_object.get("name")
        result = None
        if not id:
            prev_obj_name = self.get_object_by_name(name)
            id_ = None
            if prev_obj_name:
                id_ = prev_obj_name.get("id")
                id_ = id_ or prev_obj_name.get("number")
            if id_:
                self.new_object.update(dict(number=id_))
        result = self.meraki.exec_meraki(
            family="wireless",
            function="updateNetworkWirelessSsid",
            params=self.update_by_id_params(),
            op_modifies=True,
        )
        return result


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail(
                "ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        meraki = MERAKI(self._task.args)
        obj = NetworksWirelessSsids(self._task.args, meraki)

        state = self._task.args.get("state")

        response = None
        if state == "present":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    response = obj.update()
                    meraki.object_updated()
                else:
                    response = prev_obj
                    meraki.object_already_present()
            else:
                meraki.fail_json(
                    "Object does not exists, plugin only has update")

        self._result.update(dict(meraki_response=response))
        self._result.update(meraki.exit_json())
        return self._result
