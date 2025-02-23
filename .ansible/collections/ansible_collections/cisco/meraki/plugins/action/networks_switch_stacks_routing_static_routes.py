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
    get_dict_result,
)
from ansible_collections.cisco.meraki.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = meraki_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    advertiseViaOspfEnabled=dict(type="bool"),
    name=dict(type="str"),
    nextHopIp=dict(type="str"),
    preferOverOspfRoutesEnabled=dict(type="bool"),
    subnet=dict(type="str"),
    networkId=dict(type="str"),
    switchStackId=dict(type="str"),
    staticRouteId=dict(type="str"),
    managementNextHop=dict(type="str"),
))

required_if = [
    ("state", "present", ["name", "networkId", "staticRouteId", "switchStackId"], True),
    ("state", "absent", ["name", "networkId", "staticRouteId", "switchStackId"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NetworksSwitchStacksRoutingStaticRoutes(object):
    def __init__(self, params, meraki):
        self.meraki = meraki
        self.new_object = dict(
            advertiseViaOspfEnabled=params.get("advertiseViaOspfEnabled"),
            name=params.get("name"),
            nextHopIp=params.get("nextHopIp"),
            preferOverOspfRoutesEnabled=params.get("preferOverOspfRoutesEnabled"),
            subnet=params.get("subnet"),
            networkId=params.get("networkId"),
            switchStackId=params.get("switchStackId"),
            staticRouteId=params.get("staticRouteId"),
            managementNextHop=params.get("managementNextHop"),
        )

    def get_all_params(self, name=None, id=None):
        new_object_params = {}
        if self.new_object.get('networkId') is not None or self.new_object.get('network_id') is not None:
            new_object_params['networkId'] = self.new_object.get('networkId') or \
                self.new_object.get('network_id')
        if self.new_object.get('switchStackId') is not None or self.new_object.get('switch_stack_id') is not None:
            new_object_params['switchStackId'] = self.new_object.get('switchStackId') or \
                self.new_object.get('switch_stack_id')
        return new_object_params

    def get_params_by_id(self, name=None, id=None):
        new_object_params = {}
        if self.new_object.get('networkId') is not None or self.new_object.get('network_id') is not None:
            new_object_params['networkId'] = self.new_object.get('networkId') or \
                self.new_object.get('network_id')
        if self.new_object.get('switchStackId') is not None or self.new_object.get('switch_stack_id') is not None:
            new_object_params['switchStackId'] = self.new_object.get('switchStackId') or \
                self.new_object.get('switch_stack_id')
        if self.new_object.get('staticRouteId') is not None or self.new_object.get('static_route_id') is not None:
            new_object_params['staticRouteId'] = self.new_object.get('staticRouteId') or \
                self.new_object.get('static_route_id')
        return new_object_params

    def create_params(self):
        new_object_params = {}
        if self.new_object.get('advertiseViaOspfEnabled') is not None or self.new_object.get('advertise_via_ospf_enabled') is not None:
            new_object_params['advertiseViaOspfEnabled'] = self.new_object.get('advertiseViaOspfEnabled')
        if self.new_object.get('name') is not None or self.new_object.get('name') is not None:
            new_object_params['name'] = self.new_object.get('name') or \
                self.new_object.get('name')
        if self.new_object.get('nextHopIp') is not None or self.new_object.get('next_hop_ip') is not None:
            new_object_params['nextHopIp'] = self.new_object.get('nextHopIp') or \
                self.new_object.get('next_hop_ip')
        if self.new_object.get('preferOverOspfRoutesEnabled') is not None or self.new_object.get('prefer_over_ospf_routes_enabled') is not None:
            new_object_params['preferOverOspfRoutesEnabled'] = self.new_object.get('preferOverOspfRoutesEnabled')
        if self.new_object.get('subnet') is not None or self.new_object.get('subnet') is not None:
            new_object_params['subnet'] = self.new_object.get('subnet') or \
                self.new_object.get('subnet')
        if self.new_object.get('networkId') is not None or self.new_object.get('network_id') is not None:
            new_object_params['networkId'] = self.new_object.get('networkId') or \
                self.new_object.get('network_id')
        if self.new_object.get('switchStackId') is not None or self.new_object.get('switch_stack_id') is not None:
            new_object_params['switchStackId'] = self.new_object.get('switchStackId') or \
                self.new_object.get('switch_stack_id')
        return new_object_params

    def delete_by_id_params(self):
        new_object_params = {}
        if self.new_object.get('networkId') is not None or self.new_object.get('network_id') is not None:
            new_object_params['networkId'] = self.new_object.get('networkId') or \
                self.new_object.get('network_id')
        if self.new_object.get('switchStackId') is not None or self.new_object.get('switch_stack_id') is not None:
            new_object_params['switchStackId'] = self.new_object.get('switchStackId') or \
                self.new_object.get('switch_stack_id')
        if self.new_object.get('staticRouteId') is not None or self.new_object.get('static_route_id') is not None:
            new_object_params['staticRouteId'] = self.new_object.get('staticRouteId') or \
                self.new_object.get('static_route_id')
        return new_object_params

    def update_by_id_params(self):
        new_object_params = {}
        if self.new_object.get('advertiseViaOspfEnabled') is not None or self.new_object.get('advertise_via_ospf_enabled') is not None:
            new_object_params['advertiseViaOspfEnabled'] = self.new_object.get('advertiseViaOspfEnabled')
        if self.new_object.get('managementNextHop') is not None or self.new_object.get('management_next_hop') is not None:
            new_object_params['managementNextHop'] = self.new_object.get('managementNextHop') or \
                self.new_object.get('management_next_hop')
        if self.new_object.get('name') is not None or self.new_object.get('name') is not None:
            new_object_params['name'] = self.new_object.get('name') or \
                self.new_object.get('name')
        if self.new_object.get('nextHopIp') is not None or self.new_object.get('next_hop_ip') is not None:
            new_object_params['nextHopIp'] = self.new_object.get('nextHopIp') or \
                self.new_object.get('next_hop_ip')
        if self.new_object.get('preferOverOspfRoutesEnabled') is not None or self.new_object.get('prefer_over_ospf_routes_enabled') is not None:
            new_object_params['preferOverOspfRoutesEnabled'] = self.new_object.get('preferOverOspfRoutesEnabled')
        if self.new_object.get('subnet') is not None or self.new_object.get('subnet') is not None:
            new_object_params['subnet'] = self.new_object.get('subnet') or \
                self.new_object.get('subnet')
        if self.new_object.get('networkId') is not None or self.new_object.get('network_id') is not None:
            new_object_params['networkId'] = self.new_object.get('networkId') or \
                self.new_object.get('network_id')
        if self.new_object.get('switchStackId') is not None or self.new_object.get('switch_stack_id') is not None:
            new_object_params['switchStackId'] = self.new_object.get('switchStackId') or \
                self.new_object.get('switch_stack_id')
        if self.new_object.get('staticRouteId') is not None or self.new_object.get('static_route_id') is not None:
            new_object_params['staticRouteId'] = self.new_object.get('staticRouteId') or \
                self.new_object.get('static_route_id')
        return new_object_params

    def get_object_by_name(self, name):
        result = None
        # NOTE: Does not have a get by name method or it is in another action
        try:
            items = self.meraki.exec_meraki(
                family="switch",
                function="getNetworkSwitchStackRoutingStaticRoutes",
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
                family="switch",
                function="getNetworkSwitchStackRoutingStaticRoute",
                params=self.get_params_by_id()
            )
            if isinstance(items, dict):
                if 'response' in items:
                    items = items.get('response')
            result = get_dict_result(items, 'staticRouteId', id)
        except Exception as e:
            print("Error: ", e)
            result = None
        return result

    def exists(self):
        id_exists = False
        name_exists = False
        prev_obj = None
        o_id = self.new_object.get("id")
        o_id = o_id or self.new_object.get(
            "static_route_id") or self.new_object.get("staticRouteId")
        name = self.new_object.get("name")
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            _id = _id or prev_obj.get("staticRouteId")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters(
                    "The 'id' and 'name' params don't refer to the same object")
            if _id:
                self.new_object.update(dict(id=_id))
                self.new_object.update(dict(staticRouteId=_id))
            if _id:
                prev_obj = self.get_object_by_id(_id)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("advertiseViaOspfEnabled", "advertiseViaOspfEnabled"),
            ("name", "name"),
            ("nextHopIp", "nextHopIp"),
            ("preferOverOspfRoutesEnabled", "preferOverOspfRoutesEnabled"),
            ("subnet", "subnet"),
            ("networkId", "networkId"),
            ("switchStackId", "switchStackId"),
            ("staticRouteId", "staticRouteId"),
            ("managementNextHop", "managementNextHop"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (DNAC) params
        # If any does not have eq params, it requires update
        return any(not meraki_compare_equality2(current_obj.get(meraki_param),
                                                requested_obj.get(ansible_param))
                   for (meraki_param, ansible_param) in obj_params)

    def create(self):
        result = self.meraki.exec_meraki(
            family="switch",
            function="createNetworkSwitchStackRoutingStaticRoute",
            params=self.create_params(),
            op_modifies=True,
        )
        return result

    def update(self):
        id = self.new_object.get("id")
        id = id or self.new_object.get("staticRouteId")
        name = self.new_object.get("name")
        result = None
        if not id:
            prev_obj_name = self.get_object_by_name(name)
            id_ = None
            if prev_obj_name:
                id_ = prev_obj_name.get("id")
                id_ = id_ or prev_obj_name.get("staticRouteId")
            if id_:
                self.new_object.update(dict(staticRouteId=id_))
        result = self.meraki.exec_meraki(
            family="switch",
            function="updateNetworkSwitchStackRoutingStaticRoute",
            params=self.update_by_id_params(),
            op_modifies=True,
        )
        return result

    def delete(self):
        id = self.new_object.get("id")
        id = id or self.new_object.get("staticRouteId")
        name = self.new_object.get("name")
        result = None
        if not id:
            prev_obj_name = self.get_object_by_name(name)
            id_ = None
            if prev_obj_name:
                id_ = prev_obj_name.get("id")
                id_ = id_ or prev_obj_name.get("staticRouteId")
            if id_:
                self.new_object.update(dict(staticRouteId=id_))
        result = self.meraki.exec_meraki(
            family="switch",
            function="deleteNetworkSwitchStackRoutingStaticRoute",
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
        obj = NetworksSwitchStacksRoutingStaticRoutes(self._task.args, meraki)

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
