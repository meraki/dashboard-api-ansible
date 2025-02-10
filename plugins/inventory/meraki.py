# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
name: meraki
author:
  - Nilashish Chakrabirty (@NilashishC)
short_description: Ansible dynamic inventory plugin for Cisco Meraki devices.
requirements:
  - meraki
extends_documentation_fragment:
  - constructed
description:
  - Build inventories using the Cisco Meraki API.
  - Uses a YAML configuration file cisco_meraki.[yml|yaml].
options:
  meraki_api_key:
    description:
      - Specifies the Meraki API key,
      - See the Cisco Meraki documentaion to obtain the API key
        U(https://developer.cisco.com/meraki/api-v1/authorization/#obtaining-your-meraki-api-key).
    type: str
    required: true
  meraki_org_id:
    description:
      - The organization ID to fetch the networks and devices from.
    type: str
    required: true
"""

EXAMPLES = """
# cisco_meraki.yml
---
plugin: cisco.meraki.meraki
meraki_api_key: "<enter Meraki API key>"
meraki_org_id: "<enter Meraki Org ID>"
keyed_groups:
  # group devices based on network ID
  - prefix: meraki_network_id
    key: network_id
  # group devices based on device type
  - prefix: meraki_device_type
    key: device_type
  # group devices based on meraki device tag
  - prefix: meraki_tag
    key: tags
"""

from ansible.errors import AnsibleError
from ansible.module_utils.common.text.converters import to_native, to_text
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable
from ansible.module_utils.basic import missing_required_lib


try:
    import meraki

    HAS_MERAKI = True
except ImportError:
    HAS_MERAKI = False


class InventoryModule(BaseInventoryPlugin, Constructable):
    NAME = "cisco.meraki.meraki"

    def verify_file(self, path):
        """return true/false if this is possibly a valid file for this plugin to consume"""
        valid = False
        if super(InventoryModule, self).verify_file(path):
            # base class verifies that file exists and is readable by current user
            if path.endswith(("cisco_meraki.yaml", "cisco_meraki.yml")):
                valid = True
        return valid

    def _build_network_map(self, dashboard, org_id):
        """Build a dictionary mapping network ID to network names."""
        self._networks = {}
        networks = dashboard.organizations.getOrganizationNetworks(
            org_id, total_pages="all"
        )
        for network in networks:
            self._networks[network["id"]] = to_text(network.get("name", ""))

    def parse(self, inventory, loader, path, cache=True):
        """Talk to the Meraki API and build the inventory."""
        if not HAS_MERAKI:
            # fail if meraki python library is not installed
            raise AnsibleError(missing_required_lib("meraki"))

        # call base method to ensure properties are available for use with other helper methods
        super(InventoryModule, self).parse(inventory, loader, path, cache)
        self._read_config_data(path)

        meraki_api_key = self.get_option("meraki_api_key")
        meraki_org_id = self.get_option("meraki_org_id")

        strict = self.get_option("strict")
        keyed_groups = self.get_option("keyed_groups")

        if not meraki_api_key:
            raise AnsibleError("`meraki_api_key` option is not set or is empty.")
        if not meraki_org_id:
            raise AnsibleError("`meraki_org_id` option is not set or is empty.")

        dashboard = meraki.DashboardAPI(
            api_key=meraki_api_key.strip(),
            base_url="https://api.meraki.com/api/v1/",
            output_log=False,
            print_console=False,
        )
        try:
            devices = dashboard.organizations.getOrganizationDevices(
                meraki_org_id, total_pages="all"
            )
            if devices:
                self._build_network_map(dashboard, meraki_org_id)

                for device in devices:
                    hostname = device.get("name")
                    if not hostname:
                        self.display.warning(
                            f"No name set for device with MAC {device['mac']}"
                        )
                        hostname = device["mac"]
                    self.inventory.add_host(hostname, group="all")
                    self.inventory.set_variable(
                        hostname, "ansible_host", device.get("lanIp", "")
                    )
                    self.inventory.set_variable(
                        hostname, "device_type", device["model"]
                    )

                    if device.get("networkId"):
                        self.inventory.set_variable(
                            hostname, "network_id", device["networkId"]
                        )
                        self.inventory.set_variable(
                            hostname, "network",
                            self._networks[device["networkId"]]
                        )
                    else:
                        self.display.vvvv(
                            f"Device {hostname} is not associated with a network."
                        )

                    self.inventory.set_variable(
                        hostname, "serial_number", device["serial"]
                    )
                    self.inventory.set_variable(hostname, "mac", device["mac"])

                    # Add the host to the keyed groups
                    self._add_host_to_keyed_groups(
                        keys=keyed_groups,
                        variables=device,
                        host=hostname,
                        strict=strict,
                    )
        except Exception as e:
            raise AnsibleError(f"Failed to get devices from Meraki API: {to_native(e)}")
