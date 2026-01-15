#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: devices_liveTools_cableTest_info
short_description: Information module for devices _livetools _cabletest
description:
  - Information module for Devices Livetools Cabletest Info.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - meraki >= 2.4.9
  - python >= 3.5
notes:
  - Paths used are
"""

EXAMPLES = r"""
"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample:
  - {}
"""
