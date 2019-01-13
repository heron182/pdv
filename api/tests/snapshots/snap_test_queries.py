# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_find_pdv 1'] = {
    'data': {
        'allPdvs': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 10,
                    'line': 1
                }
            ],
            'message': 'reading from stdin while output is captured',
            'path': [
                'allPdvs'
            ]
        }
    ]
}

snapshots['test_create_pdv 1'] = {
    'data': {
        'createPdv': {
            'pdv': {
                'address': '{"type": "Point", "coordinates": [-46.57421, -21.785741]}',
                'coverageArea': '{"type": "MultiPolygon", "coordinates": [[[[30.0, 20.0], [45.0, 40.0], [10.0, 40.0], [30.0, 20.0]]], [[[15.0, 5.0], [40.0, 10.0], [10.0, 20.0], [5.0, 10.0], [15.0, 5.0]]]]}',
                'document': '28563782/12345',
                'ownerName': 'Gloriaaa',
                'tradingName': 'Cabo Daciolo'
            }
        }
    }
}

snapshots['test_all_pdvs 1'] = {
    'data': {
        'allPdvs': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 10,
                    'line': 1
                }
            ],
            'message': 'reading from stdin while output is captured',
            'path': [
                'allPdvs'
            ]
        }
    ]
}
