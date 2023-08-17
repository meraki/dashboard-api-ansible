# Ansible Collection - cisco.meraki

## Ansible Modules for Meraki

The meraki-ansible project provides an Ansible collection for managing and automating your Cisco Meraki environment. It consists of a set of modules and roles for performing tasks related to Meraki.

This collection has been tested and supports Cisco Meraki v1.33.0

*Note: This collection is not compatible with versions of Ansible before v2.8.*

Other versions of this collection have support for previous Cisco Meraki versions. The recommended versions are listed below on the [Compatibility matrix](https://github.com/cisco-en-programmability/meraki-ansible#compatibility-matrix).

## Compatibility matrix

| Cisco Meraki version | Ansible "cisco.meraki" version | Python "DashboardAPI" version |
|--------------------------|------------------------------|-------------------------------|
| 1.33.0                    | 1.0.0                       |1.33.0                         |

*Notes*:


1. The "Python 'merakisdk' version" column has the minimum recommended version used when testing the Ansible collection. This means you could use later versions of the Python "merakisdk" than those listed.
2. The "Cisco Meraki version" column has the value of the `meraki_version` you should use for the Ansible collection.

## Installing according to Compatibility Matrix

For example, for Cisco Meraki 1.33.0, it is recommended to use Ansible "cisco.meraki" v1.0.0 and Python "meraki DashboardAPI" v1.33.0.

To get the Python Meraki SDK v1.33.0 in a fresh development environment:
```
sudo pip install meraki==1.33.0
```

To get the Ansible collection v1.0.0 in a fresh development environment:
```
ansible-galaxy collection install cisco.meraki:1.0.0
```

## Requirements
- Ansible >= 2.9
- [Python Meraki SDK](https://github.com/meraki/dashboard-api-python) v1.33.0 or newer
- Python >= 3.6, as the Meraki SDK doesn't support Python version 2.x

## Install
Ansible must be installed ([Install guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html))
```
sudo pip install ansible
```

Python Meraki SDK must be installed
```
sudo pip install meraki
```

Install the collection ([Galaxy link](https://galaxy.ansible.com/cisco/meraki))
```
ansible-galaxy collection install cisco.meraki
```
## Use
First, your Meraki API key needs to be available for the playbook to use. You can leverage environment variables `export MERAKI_DASHBOARD_API_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73`, or create a `credentials.yml` ([example](https://github.com/cisco-en-programmability/meraki-ansible/blob/main/playbooks/credentials.template)) file.
**Note:** storing your API key in an unencrypted text file is not recommended for security reasons.
```
---
meraki_api_key: "ABC"
meraki_base_url: "https://api.meraki.com/api/v1"
meraki_single_request_timeout: ""
meraki_certificate_path: ""
meraki_requests_proxy: True
meraki_wait_on_rate_limit: 60
meraki_nginx_429_retry_wait_time: 60
meraki_action_batch_retry_wait_time: 60
meraki_retry_4xx_error: False
meraki_retry_4xx_error_wait_time: 60
meraki_maximum_retries: 2
meraki_output_log: True
meraki_log_file_prefix: "meraki_api_"
meraki_log_path: ""
meraki_print_console: True
meraki_suppress_logging: False
meraki_simulate: False
meraki_be_geo_id: ""
meraki_caller: ""
meraki_use_iterator_for_get_pages: False
meraki_inherit_logging_config: False
```

Create a `hosts` ([example](https://github.com/cisco-en-programmability/meraki-ansible/blob/main/playbooks/hosts)) file that uses `[meraki_servers]` with your Cisco Meraki Settings:
```
[meraki_servers]
meraki_server
```

Then, create a playbook `myplaybook.yml` ([example](https://github.com/cisco-en-programmability/meraki-ansible/blob/main/playbooks/tag.yml)) referencing the variables in your credentials.yml file and specifying the full namespace path to the module, plugin and/or role:
```
---
- hosts: meraki_servers
  gather_facts: false
  tasks:
    - name: Get all administered _identities _me
      cisco.meraki.administered_identities_me_info:
        meraki_suppress_logging: true
      register: result

```

Execute the playbook:
```
ansible-playbook -i hosts myplaybook.yml
```
In the `playbooks` [directory](https://github.com/cisco-en-programmability/meraki-ansible/blob/main/playbooks) you can find more examples and use cases.


## Update
Getting the latest/nightly collection build

Clone the meraki-ansible repository.
```
git clone https://github.com/cisco-en-programmability/meraki-ansible.git
```

Go to the meraki-ansible directory
```
cd meraki-ansible
```

Pull the latest master from the repo
```
git pull origin master
```

Build and install a collection from source
```
ansible-galaxy collection build --force
ansible-galaxy collection install cisco-meraki-* --force
```

### See Also:

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Attention macOS users

If you're using macOS you may receive this error when running your playbook:

```
objc[34120]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called.
objc[34120]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
ERROR! A worker was found in a dead state
```

If that's the case try setting this environment variable:
```
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```

## Contributing to this collection

Ongoing development efforts and contributions to this collection are tracked as issues in this repository.

We welcome community contributions to this collection. If you find problems, need an enhancement or need a new module, please open an issue or create a PR against the [Cisco Meraki Ansible collection repository](https://github.com/cisco-en-programmability/meraki-ansible/issues).

## Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Releasing, Versioning and Deprecation

This collection follows [Semantic Versioning](https://semver.org/). More details on versioning can be found [in the Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#collection-versions).

New minor and major releases as well as deprecations will follow new releases and deprecations of the Cisco Meraki product, its REST API and the corresponding Python SDK, which this project relies on. 
