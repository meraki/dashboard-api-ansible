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
    meraki_compare_equality2,
)
from ansible_collections.cisco.meraki.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = meraki_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    alertCondition=dict(type="dict"),
    description=dict(type="str"),
    networkTags=dict(type="list"),
    recipients=dict(type="dict"),
    type=dict(type="str"),
    organizationId=dict(type="str"),
    enabled=dict(type="bool"),
    alertConfigId=dict(type="str"),
))

required_if = [
    ("state", "present", ["alertConfigId", "organizationId"], True),
    ("state", "absent", ["alertConfigId", "organizationId"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class OrganizationsAlertsProfiles(object):
    def __init__(self, params, meraki):
        self.meraki = meraki
        self.new_object = dict(
            alertCondition=params.get("alertCondition"),
            description=params.get("description"),
            networkTags=params.get("networkTags"),
            recipients=params.get("recipients"),
            type=params.get("type"),
            organization_id=params.get("organizationId"),
            enabled=params.get("enabled"),
            alert_config_id=params.get("alertConfigId"),
        )

    def create_params(self):
        new_object_params = {}
        if self.new_object.get('alertCondition') is not None or self.new_object.get('alert_condition') is not None:
            new_object_params['alertCondition'] = self.new_object.get('alertCondition') or \
                self.new_object.get('alert_condition')
        if self.new_object.get('description') is not None or self.new_object.get('description') is not None:
            new_object_params['description'] = self.new_object.get('description') or \
                self.new_object.get('description')
        if self.new_object.get('networkTags') is not None or self.new_object.get('network_tags') is not None:
            new_object_params['networkTags'] = self.new_object.get('networkTags') or \
                self.new_object.get('network_tags')
        if self.new_object.get('recipients') is not None or self.new_object.get('recipients') is not None:
            new_object_params['recipients'] = self.new_object.get('recipients') or \
                self.new_object.get('recipients')
        if self.new_object.get('type') is not None or self.new_object.get('type') is not None:
            new_object_params['type'] = self.new_object.get('type') or \
                self.new_object.get('type')
        if self.new_object.get('organizationId') is not None or self.new_object.get('organization_id') is not None:
            new_object_params['organizationId'] = self.new_object.get('organizationId') or \
                self.new_object.get('organization_id')
        return new_object_params

    def delete_by_id_params(self):
        new_object_params = {}
        if self.new_object.get('organizationId') is not None or self.new_object.get('organization_id') is not None:
            new_object_params['organizationId'] = self.new_object.get('organizationId') or \
                self.new_object.get('organization_id')
        if self.new_object.get('alertConfigId') is not None or self.new_object.get('alert_config_id') is not None:
            new_object_params['alertConfigId'] = self.new_object.get('alertConfigId') or \
                self.new_object.get('alert_config_id')
        return new_object_params

    def update_by_id_params(self):
        new_object_params = {}
        if self.new_object.get('alertCondition') is not None or self.new_object.get('alert_condition') is not None:
            new_object_params['alertCondition'] = self.new_object.get('alertCondition') or \
                self.new_object.get('alert_condition')
        if self.new_object.get('description') is not None or self.new_object.get('description') is not None:
            new_object_params['description'] = self.new_object.get('description') or \
                self.new_object.get('description')
        if self.new_object.get('enabled') is not None or self.new_object.get('enabled') is not None:
            new_object_params['enabled'] = self.new_object.get('enabled')
        if self.new_object.get('networkTags') is not None or self.new_object.get('network_tags') is not None:
            new_object_params['networkTags'] = self.new_object.get('networkTags') or \
                self.new_object.get('network_tags')
        if self.new_object.get('recipients') is not None or self.new_object.get('recipients') is not None:
            new_object_params['recipients'] = self.new_object.get('recipients') or \
                self.new_object.get('recipients')
        if self.new_object.get('type') is not None or self.new_object.get('type') is not None:
            new_object_params['type'] = self.new_object.get('type') or \
                self.new_object.get('type')
        if self.new_object.get('organizationId') is not None or self.new_object.get('organization_id') is not None:
            new_object_params['organizationId'] = self.new_object.get('organizationId') or \
                self.new_object.get('organization_id')
        if self.new_object.get('alertConfigId') is not None or self.new_object.get('alert_config_id') is not None:
            new_object_params['alertConfigId'] = self.new_object.get('alertConfigId') or \
                self.new_object.get('alert_config_id')
        return new_object_params

    def get_object_by_name(self, name):
        result = None
        # NOTE: Does not have a get by name and get all
        return result

    def get_object_by_id(self, id):
        result = None
        # NOTE: Does not have a get by id method or it is in another action
        return result

    def exists(self):
        prev_obj = None
        id_exists = False
        name_exists = False
        o_id = self.new_object.get("id")
        o_id = o_id or self.new_object.get(
            "alert_config_id") or self.new_object.get("alertConfigId")
        name = self.new_object.get("name")
        if o_id:
            prev_obj = self.get_object_by_name(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            _id = _id or prev_obj.get("alertConfigId")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters(
                    "The 'id' and 'name' params don't refer to the same object")
            if _id:
                self.new_object.update(dict(id=_id))
                self.new_object.update(dict(alertConfigId=_id))
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("alertCondition", "alertCondition"),
            ("description", "description"),
            ("networkTags", "networkTags"),
            ("recipients", "recipients"),
            ("type", "type"),
            ("organizationId", "organizationId"),
            ("enabled", "enabled"),
            ("alertConfigId", "alertConfigId"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(not meraki_compare_equality2(current_obj.get(meraki_param),
                                                requested_obj.get(ansible_param))
                   for (meraki_param, ansible_param) in obj_params)

    def create(self):
        result = self.meraki.exec_meraki(
            family="organizations",
            function="createOrganizationAlertsProfile",
            params=self.create_params(),
            op_modifies=True,
        )
        return result

    def update(self):
        id = self.new_object.get("id")
        id = id or self.new_object.get("alertConfigId")
        name = self.new_object.get("name")
        result = None
        if not id:
            prev_obj_name = self.get_object_by_name(name)
            id_ = None
            if prev_obj_name:
                id_ = prev_obj_name.get("id")
                id_ = id_ or prev_obj_name.get("alertConfigId")
            if id_:
                self.new_object.update(dict(alertconfigid=id_))
        result = self.meraki.exec_meraki(
            family="organizations",
            function="updateOrganizationAlertsProfile",
            params=self.update_by_id_params(),
            op_modifies=True,
        )
        return result

    def delete(self):
        id = self.new_object.get("id")
        id = id or self.new_object.get("alertConfigId")
        name = self.new_object.get("name")
        result = None
        if not id:
            prev_obj_name = self.get_object_by_name(name)
            id_ = None
            if prev_obj_name:
                id_ = prev_obj_name.get("id")
                id_ = id_ or prev_obj_name.get("alertConfigId")
            if id_:
                self.new_object.update(dict(alertconfigid=id_))
        result = self.meraki.exec_meraki(
            family="organizations",
            function="deleteOrganizationAlertsProfile",
            params=self.delete_by_id_params(),
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
        obj = OrganizationsAlertsProfiles(self._task.args, meraki)

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
                response = obj.create()
                meraki.object_created()
        elif state == "absent":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                response = obj.delete()
                meraki.object_deleted()
            else:
                meraki.object_already_absent()

        self._result.update(dict(meraki_response=response))
        self._result.update(meraki.exit_json())
        return self._result
