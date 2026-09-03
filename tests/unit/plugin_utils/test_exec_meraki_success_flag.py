"""
Unit tests for MERAKI.exec_meraki()'s handling of {"success": false} responses
(plugins/plugin_utils/meraki.py).

Several write operations across the collection (reboot, cycle ports, blink
LEDs, unenroll, batch updates, ...) return HTTP 2xx with a body of the form
{"success": false} when the requested action is rejected, instead of raising
an APIError. Before this fix, exec_meraki() returned that body as-is, so the
calling action plugin reported changed=True/failed=False even though nothing
happened. Only write calls (op_modifies=True) whose response is a dict with
an *explicit* `success: False` must now fail; anything else (reads, or a
write response with no "success" key at all, like most update* operations
that return the updated object) must be unaffected.
"""

import importlib.util
from pathlib import Path

import pytest
from ansible.errors import AnsibleActionFail

_MODULE_PATH = Path(__file__).resolve().parents[3] / "plugins" / "plugin_utils" / "meraki.py"
_spec = importlib.util.spec_from_file_location("meraki_plugin_utils_under_test", _MODULE_PATH)
_meraki_pu = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_meraki_pu)

MERAKI = _meraki_pu.MERAKI


class _Family:
    """Stand-in for a meraki.DashboardAPI family object (e.g. api.devices)."""

    def __init__(self, **functions):
        for name, fn in functions.items():
            setattr(self, name, fn)


def make_meraki(**families):
    # Bypass MERAKI.__init__ (it builds a real meraki.DashboardAPI, which
    # requires the meraki SDK and API credentials) and wire up a fake .api.
    obj = MERAKI.__new__(MERAKI)
    obj.result = dict(changed=False, result="")
    obj._params = {}
    obj.api = type("FakeAPI", (), {})()
    for family_name, family in families.items():
        setattr(obj.api, family_name, family)
    return obj


def test_explicit_success_false_on_a_write_call_fails():
    meraki = make_meraki(devices=_Family(rebootDevice=lambda **kw: {"success": False}))

    with pytest.raises(AnsibleActionFail):
        meraki.exec_meraki(family="devices", function="rebootDevice", params={"serial": "Q2XX"}, op_modifies=True)


def test_explicit_success_true_on_a_write_call_passes_through():
    meraki = make_meraki(devices=_Family(rebootDevice=lambda **kw: {"success": True}))

    response = meraki.exec_meraki(
        family="devices", function="rebootDevice", params={"serial": "Q2XX"}, op_modifies=True
    )

    assert response == {"success": True}


def test_write_response_without_success_key_remains_valid():
    # Most update* operations return the updated object itself, with no
    # "success" key at all. That must still be treated as a normal result.
    updated = {"wan1": {"usingStaticIp": True}}
    meraki = make_meraki(devices=_Family(updateDeviceManagementInterface=lambda **kw: updated))

    response = meraki.exec_meraki(
        family="devices", function="updateDeviceManagementInterface", params={"serial": "Q2XX"}, op_modifies=True
    )

    assert response == updated


def test_read_call_with_success_as_business_data_is_unaffected():
    # Some _info responses use "success" as an actual data field (e.g.
    # wireless connection stats: counts of successful/failed connections),
    # not an operation-result flag. Read calls never set op_modifies, so
    # they must never be evaluated against this check.
    stats = {"success": 0, "assoc": 4, "auth": 4}
    meraki = make_meraki(wireless=_Family(getDeviceWirelessConnectionStats=lambda **kw: stats))

    response = meraki.exec_meraki(
        family="wireless", function="getDeviceWirelessConnectionStats", params={"serial": "Q2XX"}
    )

    assert response == stats


def test_non_dict_response_on_a_write_call_is_unaffected():
    meraki = make_meraki(devices=_Family(rebootDevice=lambda **kw: None))

    response = meraki.exec_meraki(
        family="devices", function="rebootDevice", params={"serial": "Q2XX"}, op_modifies=True
    )

    assert response is None
