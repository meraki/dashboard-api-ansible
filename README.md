# Ansible Modules for Meraki

The Meraki-Ansible project provides an Ansible collection for managing and automating your Cisco Meraki environment. It consists of a set of modules and roles for performing tasks related to Meraki.

## Requirements

- Ansible >= 2.14
- [Python Meraki SDK](https://github.com/meraki/dashboard-api-python) v1.33.0 or newer
- Python >= 3.6, as the Meraki SDK doesn't support Python version 2.x

## Installation

1. Install the collection from Ansible Automation Hub or Galaxy:

```
ansible-galaxy collection install cisco.meraki -f
```

2. Install the Python Meraki SDK:

```
pip install meraki
```

3. Make your Meraki API key available to the playbook. You can use an environment variable:

```
export MERAKI_DASHBOARD_API_KEY=<your_api_key>
```

> **Note:** Storing your API key in an unencrypted text file is not recommended for security reasons. Consider using Ansible Vault or AAP credentials.

4. Create a `hosts` ([example](https://github.com/meraki/dashboard-api-ansible/blob/main/playbooks/hosts)) file:

```
[meraki_servers]
meraki_server
```

## Use Cases

### 1. Retrieve administrator identity

Verify which Meraki admin account is being used by the API key:

```yaml
---
- name: Get administered identities
  hosts: meraki_servers
  gather_facts: false
  tasks:
    - name: Get my administered identities
      cisco.meraki.administered_identities_me_info:
        meraki_api_key: "{{ meraki_api_key }}"
      register: result

    - name: Show result
      ansible.builtin.debug:
        msg: "{{ result }}"
```

### 2. Manage network webhooks

Create an HTTP server webhook for a Meraki network to receive alert notifications:

```yaml
---
- name: Configure network webhook
  hosts: meraki_servers
  gather_facts: false
  tasks:
    - name: Create webhook
      cisco.meraki.networks_webhooks_http_servers:
        meraki_api_key: "{{ meraki_api_key }}"
        state: present
        name: MyWebhook
        networkId: "{{ network_id }}"
        payloadTemplate:
          name: Slack (included)
          payloadTemplateId: wpt_00001
        sharedSecret: "{{ webhook_secret }}"
        url: https://webhook.example.com/
```

### 3. Configure wireless settings

Enable or disable multicast-to-unicast conversion for a network's wireless settings:

```yaml
---
- name: Update wireless settings
  hosts: meraki_servers
  gather_facts: false
  tasks:
    - name: Enable multicast-to-unicast conversion
      cisco.meraki.networks_wireless_settings:
        meraki_api_key: "{{ meraki_api_key }}"
        state: present
        networkId: "{{ network_id }}"
        ipv6BridgeEnabled: false
        locationAnalyticsEnabled: false
        meshingEnabled: true
        upgradeStrategy: minimizeUpgradeTime
```

### 4. Query organization inventory

Retrieve device inventory for an organization, including End-of-Life status information:

```yaml
---
- name: Get organization inventory
  hosts: meraki_servers
  gather_facts: false
  tasks:
    - name: Retrieve inventory devices
      cisco.meraki.organizations_inventory_devices_info:
        meraki_api_key: "{{ meraki_api_key }}"
        organizationId: "{{ org_id }}"
      register: inventory

    - name: Show inventory
      ansible.builtin.debug:
        msg: "{{ inventory }}"
```

### 5. Manage organization appliance VPN peers

Configure third-party VPN peers for an organization's appliances:

```yaml
---
- name: Configure third-party VPN peers
  hosts: meraki_servers
  gather_facts: false
  tasks:
    - name: Update VPN peers
      cisco.meraki.organizations_appliance_vpn_third_party_vpn_peers:
        meraki_api_key: "{{ meraki_api_key }}"
        state: present
        organizationId: "{{ org_id }}"
        peers:
          - name: RemoteSite
            publicIp: 198.51.100.1
            privateSubnets:
              - 192.168.100.0/24
            secret: "{{ vpn_secret }}"
            ikeVersion: "2"
```

## Testing

This collection has been tested against the following environments:

| Cisco Meraki Dashboard API | Ansible "cisco.meraki" | Python "meraki" SDK |
|----------------------------|------------------------|---------------------|
| 1.33.0                     | 2.17.0                 | 1.33.0              |
| 1.44.1                     | 2.18.3                 | 1.44.1              |
| 1.53.0                     | 2.20.8                 | 1.53.0              |
| 1.57.0                     | 2.21.2                 | 1.57.0              |
| 1.68.0                     | 2.23.0                 | 2.2.0               |

*Notes*:

1. The "Python `meraki` SDK version" column shows the minimum recommended version used during testing. Later versions of the SDK may also be used.
2. The "Cisco Meraki Dashboard API" column corresponds to the `meraki_version` value you should use with this collection.
3. This collection is not compatible with versions of Ansible before v2.14.

### Known issues

**macOS users** may encounter the following error when running playbooks:

```
objc[34120]: +[__NSCFConstantString initialize] may have been in progress in
another thread when fork() was called. We cannot safely call it or ignore it
in the fork() child process. Crashing instead.
ERROR! A worker was found in a dead state
```

Set the following environment variable to resolve this:

```
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```

## Support

As Red Hat Ansible Certified Content, this collection is entitled to support through the Ansible Automation Platform (AAP) using the **Create issue** button on the top right corner. If a support case cannot be opened with Red Hat and the collection has been obtained either from Galaxy or GitHub, there may be community help available on the [Ansible Forum](https://forum.ansible.com/).

## Release Notes and Roadmap

See the full [Changelog](https://github.com/meraki/dashboard-api-ansible/blob/main/CHANGELOG.rst) for release history.

This collection follows [Semantic Versioning](https://semver.org/). More details on versioning can be found [in the Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#collection-versions).

New minor and major releases as well as deprecations will follow new releases and deprecations of the Cisco Meraki product, its REST API and the corresponding Python SDK, which this project relies on.

## Related Information

- [Meraki Ansible Collection Documentation](https://docs.ansible.com/ansible/latest/collections/cisco/meraki/index.html)
- [Meraki Dashboard API Documentation](https://meraki.io/api)
- [DevNet Learning Lab](https://developer.cisco.com/learning/labs/meraki-dashboard-ansible/introduction/)
- [DevNet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/a9487767-deef-4855-b3e3-880e7f39eadc?diagramType=Topology)
- [Ansible Galaxy: cisco.meraki](https://galaxy.ansible.com/cisco/meraki)

## Contributing to this collection

Ongoing development efforts and contributions to this collection are tracked as issues in this repository.

We welcome community contributions to this collection. If you find problems, need an enhancement, or need a new module, please open an issue or create a PR against the [Cisco Meraki Ansible collection repository](https://github.com/meraki/dashboard-api-ansible/issues).

This collection follows the Ansible project's [Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html). Please read and familiarize yourself with this document.

## Module migration

The modules that were there before, usually with a `meraki` prefix, are maintained until version 2.x.x, with the same structure used in previous versions. The old modules will disappear in the next major release and only the new modules will remain. Each old module has its deprecation marking indicating which is the new equivalent.

### Example

Old module:

```yaml
- name: Create webhook
  cisco.meraki.meraki_webhook:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    name: Test_Hookx
    url: https://webhook.url/
    shared_secret: shhhdonttellanyone
    payload_template_name: 'Slack (included)'
  delegate_to: localhost
```

New module:

```yaml
- name: Create webhook
  cisco.meraki.networks_webhooks_http_servers:
    meraki_api_key: "{{ meraki_api_key }}"
    state: present
    name: Test_Hook
    networkId: "{{ network_id }}"
    payloadTemplate:
      name: Slack (included)
      payloadTemplateId: wpt_00001
    sharedSecret: shhhdonttellanyone
    url: https://webhook.url/
```

## License

This project is licensed under the [GNU General Public License](https://github.com/meraki/dashboard-api-ansible/blob/main/LICENSE).
