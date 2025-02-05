from __future__ import (absolute_import, division, print_function)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

__metaclass__ = type

DOCUMENTATION = '''
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
'''

EXAMPLES = '''
# cisco_meraki.yml
---
plugin: cisco.meraki.meraki
meraki_api_key: "a80f0b3fd8d5fc214faf67c8398b04a23574b48d"
meraki_org_id: "828099381482762270"
keyed_groups:
  # group devices based on network ID
  - prefix: meraki_network_id
    key: meraki_network_id
  # group devices based on device type
  - prefix: meraki_device_type
    key: meraki_device_type
  # group devices based on meraki device tag
  - prefix: meraki_tag
    key: tags
'''

from ansible.errors import AnsibleError
from ansible.module_utils.common.text.converters import to_native
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable
from ansible.module_utils.basic import missing_required_lib


try:
    import meraki
    HAS_MERAKI = True
except ImportError:
    HAS_MERAKI = False


class InventoryModule(BaseInventoryPlugin, Constructable):
    NAME = 'cisco.meraki.meraki'

    def verify_file(self, path):
        """return true/false if this is possibly a valid file for this plugin to consume"""
        valid = False
        if super(InventoryModule, self).verify_file(path):
            # base class verifies that file exists and is readable by current user
            if path.endswith(("cisco_meraki.yaml", "cisco_meraki.yml")):
                valid = True
        return valid

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

        strict = self.get_option('strict')
        keyed_groups = self.get_option('keyed_groups')

        if not meraki_api_key:
            raise AnsibleError("`meraki_api_key` option is not set or is empty.")
        if not meraki_org_id:
            raise AnsibleError("`meraki_org_id` option is not set or is empty.")

        dashboard = meraki.DashboardAPI(
            api_key=meraki_api_key.strip(),
            base_url='https://api.meraki.com/api/v1/',
            output_log=False,
            print_console=False
        )
        try:
            devices = dashboard.organizations.getOrganizationDevices(meraki_org_id, total_pages='all')
            for device in devices:
                hostname = device.get('name')
                if not hostname:
                    self.display.warning(f"No name set for device with MAC {device['mac']}")
                    hostname = device['mac']
                self.inventory.add_host(hostname, group="all")
                self.inventory.set_variable(hostname, 'ansible_host', device.get('lanIp', ""))
                self.inventory.set_variable(hostname, 'meraki_device_type', device['model'])
                self.inventory.set_variable(hostname, 'meraki_network_id', device['networkId'])
                self.inventory.set_variable(hostname, 'mac', device['mac'])

                # Add the host to the keyed groups
                self._add_host_to_keyed_groups(
                    keys=keyed_groups,
                    variables=device,
                    host=hostname,
                    strict=strict
                )
        except Exception as e:
            raise AnsibleError(f"Failed to get devices from Meraki API: {to_native(e)}")
