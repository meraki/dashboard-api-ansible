"""
Test for cisco.meraki.devices using fixture cisco.meraki.devices.json
Method: updateDevice
"""

import jq


def test_cisco_meraki_devices_updateDevice_taxonomy(query_data, load_fixture):
    """Test model-based taxonomy for updated Meraki devices."""
    module_fqcn = "cisco.meraki.devices"
    response = load_fixture(module_fqcn)
    assert response is not None, f"Fixture {module_fqcn}.json not found"

    results = jq.compile(query_data[module_fqcn]["query"]).input(response).all()
    expected_types = {
        "Switch": ("switch", "networking"),
        "Campus Switch": ("switch", "networking"),
        "AP": ("wireless_access_point", "networking"),
        "Catalyst AP": ("wireless_access_point", "networking"),
        "SD-WAN": ("sd_wan", "networking"),
        "Teleworker": ("sd_wan", "networking"),
        "Camera": ("ip_camera", "monitoring"),
        "Sensor": ("iot_sensor", "monitoring"),
        "Gateway": ("gateway", "networking"),
        "Other": ("network_device", "networking"),
    }
    expected = [[{
        "name": name,
        "canonical_facts": {
            "ansible_product_serial": f"Q2XX-{index:04d}",
            "hostname": f"10.0.0.{index}",
        },
        "facts": {
            "device_type": device_type,
            "infra_type": "private_cloud",
            "infra_bucket": infra_bucket,
            "meraki_network_id": "N_1",
            "ansible_hostname": f"10.0.0.{index}",
            "ansible_product_name": model,
            "ansible_bios_version": "1",
            "macaddress": f"00:00:00:00:00:{index:02d}",
        },
    } for index, (name, model, (device_type, infra_bucket)) in enumerate(
        [("Switch", "MS120", expected_types["Switch"]), ("Campus Switch", "C9300", expected_types["Campus Switch"]), ("AP", "MR36", expected_types["AP"]), ("Catalyst AP", "CW9166", expected_types["Catalyst AP"]), ("SD-WAN", "MX68", expected_types["SD-WAN"]), ("Teleworker", "Z3", expected_types["Teleworker"]), ("Camera", "MV12", expected_types["Camera"]), ("Sensor", "MT10", expected_types["Sensor"]), ("Gateway", "MG21", expected_types["Gateway"]), ("Other", "XX1", expected_types["Other"])],
        start=1,
    )]]
    assert results == expected
