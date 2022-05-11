from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.combine import combine, FilterModule

NESTED_DATA_MODEL_X1 = {
    "vrfs": [
        {
            "name": "BLUE-C1",
            "rd": "1.0.1.1:101",
            "neighbors": [
                { "name": "10.255.1.1", "peer_group": "WELCOME_ROUTERS", "weight": 65535 },
                { "name": "101.0.3.1",  "peer_group": "SEDI" },
                { "name": "101.0.3.2",  "peer_group": "SEDI1", "shutdown": True },
                { "name": "101.0.3.3",  "peer_group": "SEDI-shut" },
            ],
            "aggregate_addresses": [
                { "prefix": "193.1.0.0/16", "as_set": True, "summary_only": True, "attribute_map": "RM-BGP-AGG-APPLY-SET", "advertise_only": False }
            ],
            "eos_cli": "comment\nComment created from eos_cli under router_bgp.vrfs.BLUE-C1\nEOF\n"
        }
    ]
}

NESTED_DATA_MODEL_Y1 = {
    "vrfs": [
        {
            "name": "BLUE-C1",
            "neighbors": [
                {"name": "10.1.1.0", "peer_group": "OBS_WAN"},
                {"name": "101.0.3.1", "weight": 100},
                {"name": "101.0.3.2", "peer_group": "SEDI2", "shutdown": False},
                {"name": "101.0.3.3"},
            ],
            "redistribute_routes": [
                {"source_protocol": "static"}
            ],
            "aggregate_addresses": [
                {"prefix": "0.0.0.0/0", "as_set": True, "summary_only": True, "attribute_map": "RM-BGP-AGG-APPLY-SET", "advertise_only": False}
            ],
            "eos_cli": "comment\nSpecial Comment created from eos_cli under router_bgp.vrfs.BLUE-C1\nEOF\n"
        }
    ]
}

EXPECTED_RESULT_1 = {
    'vrfs': [
        {
            'name': 'BLUE-C1',
            'rd': '1.0.1.1:101',
            'neighbors': [
                {'name': '10.255.1.1', 'peer_group': 'WELCOME_ROUTERS', 'weight': 65535},
                {'name': '101.0.3.1', 'peer_group': 'SEDI', 'weight': 100},
                {'name': '101.0.3.2', 'peer_group': 'SEDI2', 'shutdown': False},
                {'name': '101.0.3.3', 'peer_group': 'SEDI-shut'},
                {'name': '10.1.1.0', 'peer_group': 'OBS_WAN'}
            ],
            'redistribute_routes': [
                {'source_protocol': 'static'}
            ],
            'aggregate_addresses': [
                {'prefix': '193.1.0.0/16', 'as_set': True, 'summary_only': True, 'attribute_map': 'RM-BGP-AGG-APPLY-SET', 'advertise_only': False},
                {'prefix': '0.0.0.0/0', 'as_set': True, 'summary_only': True, 'attribute_map': 'RM-BGP-AGG-APPLY-SET', 'advertise_only': False}
            ],
            'eos_cli': 'comment\nSpecial Comment created from eos_cli under router_bgp.vrfs.BLUE-C1\nEOF\n'
        }
    ]
}


f = FilterModule()


class TestCombineFilter():
    def test_combine__filter_1(self):
        resp = combine(NESTED_DATA_MODEL_X1, NESTED_DATA_MODEL_Y1, recursive=True)
        assert resp == EXPECTED_RESULT_1
