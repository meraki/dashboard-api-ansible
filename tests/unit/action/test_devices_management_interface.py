"""
Unit tests for plugins/action/devices_management_interface.py.

Regression coverage for a bug where state=present could reboot a device
instead of configuring its management interface:

- create() used to call rebootDevice. A device's management interface
  always pre-exists, so there is no legitimate "create" outcome for this
  resource; the reboot mapping and create() have been removed entirely.
- get_object_by_name() used to swallow every exception (including the
  AnsibleActionFail raised by exec_meraki() on a real API failure) and
  report the object as missing, which sent execution down the removed
  create()/reboot path. It must now let a failed read propagate.
"""

import importlib.util
from pathlib import Path

import pytest
from ansible.errors import AnsibleActionFail

# Loaded by file path so these tests exercise the module in this checkout,
# even if a different build of the collection is also installed elsewhere.
_MODULE_PATH = Path(__file__).resolve().parents[3] / "plugins" / "action" / "devices_management_interface.py"
_spec = importlib.util.spec_from_file_location("devices_management_interface_under_test", _MODULE_PATH)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

DevicesManagementInterface = _module.DevicesManagementInterface


class FakeMeraki:
    """Stand-in for plugin_utils.meraki.MERAKI, recording calls."""

    def __init__(self, responses=None, raises=None):
        self.calls = []
        self._responses = responses or {}
        self._raises = raises

    def exec_meraki(self, family, function, params=None, op_modifies=False, **kwargs):
        self.calls.append({"family": family, "function": function, "params": params})
        if self._raises is not None:
            raise self._raises
        return self._responses.get(function)


def make_obj(meraki, serial="Q2XX-0000-0001", wan1=None, wan2=None):
    params = {"serial": serial, "wan1": wan1, "wan2": wan2}
    return DevicesManagementInterface(params, meraki)


def test_create_operation_no_longer_exists():
    # The management interface always pre-exists on a real device; there is
    # no create operation for it. Asserting create()/create_params() are
    # gone guards against the reboot mapping being reintroduced.
    assert not hasattr(DevicesManagementInterface, "create")
    assert not hasattr(DevicesManagementInterface, "create_params")


def test_get_object_by_name_returns_current_object_on_success():
    current = {"wan1": {"usingStaticIp": False}, "wan2": {"usingStaticIp": False}}
    meraki = FakeMeraki(responses={"getDeviceManagementInterface": current})
    obj = make_obj(meraki)

    result = obj.get_object_by_name(obj.new_object.get("serial"))

    assert result == current
    assert meraki.calls[0]["function"] == "getDeviceManagementInterface"


def test_get_object_by_name_propagates_read_failure():
    # This is the core regression: a failed read must fail the task, not be
    # silently reinterpreted as "the object does not exist".
    meraki = FakeMeraki(raises=AnsibleActionFail("devices, getDeviceManagementInterface - 404 Not Found"))
    obj = make_obj(meraki)

    with pytest.raises(AnsibleActionFail):
        obj.get_object_by_name(obj.new_object.get("serial"))


def test_exists_propagates_read_failure_instead_of_reporting_absent():
    meraki = FakeMeraki(raises=AnsibleActionFail("devices, getDeviceManagementInterface - 429 Too Many Requests"))
    obj = make_obj(meraki)

    with pytest.raises(AnsibleActionFail):
        obj.exists()


def test_exists_true_when_read_succeeds():
    current = {"wan1": {"usingStaticIp": False}}
    meraki = FakeMeraki(responses={"getDeviceManagementInterface": current})
    obj = make_obj(meraki)

    (obj_exists, prev_obj) = obj.exists()

    assert obj_exists is True
    assert prev_obj == current


def test_update_calls_update_device_management_interface_not_reboot():
    meraki = FakeMeraki(responses={"updateDeviceManagementInterface": {"success": True}})
    obj = make_obj(meraki, wan1={"usingStaticIp": True})

    obj.update()

    functions_called = [c["function"] for c in meraki.calls]
    assert functions_called == ["updateDeviceManagementInterface"]
    assert "rebootDevice" not in functions_called


def test_requires_update_true_when_wan_settings_differ():
    current = {"wan1": {"usingStaticIp": False}, "wan2": {"usingStaticIp": False}}
    meraki = FakeMeraki()
    obj = make_obj(meraki, wan1={"usingStaticIp": True})

    assert obj.requires_update(current) is True


def test_requires_update_false_when_nothing_requested():
    current = {"wan1": {"usingStaticIp": False}, "wan2": {"usingStaticIp": False}}
    meraki = FakeMeraki()
    obj = make_obj(meraki)

    assert obj.requires_update(current) is False
