# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_pdv 1'] = {
    'data': {
        'createPdv': {
            'pdv': {
                'document': '28563782/12345',
                'ownerName': 'Gloriaaa',
                'tradingName': 'Cabo Daciolo'
            }
        }
    }
}

snapshots['test_all_pdvs 1'] = {
    'data': {
        'allPdvs': {
            'edges': [
                {
                    'node': {
                        'document': '892046715/46728',
                        'id': 'UGR2OjVjMzdkNzFhMjhhNWUxMDM3MDE4MjkzMw==',
                        'ownerName': 'Zé',
                        'tradingName': 'Zé Delivery'
                    }
                },
                {
                    'node': {
                        'document': '6288172645/9816',
                        'id': 'UGR2OjVjMzdkNzFhMjhhNWUxMDM3MDE4MjkzNA==',
                        'ownerName': 'Dudu',
                        'tradingName': 'Dudu Delivery'
                    }
                },
                {
                    'node': {
                        'document': '2366518955/8144',
                        'id': 'UGR2OjVjMzdkNzFhMjhhNWUxMDM3MDE4MjkzNQ==',
                        'ownerName': 'Deyvinho',
                        'tradingName': 'Deyverson Delivery'
                    }
                }
            ]
        }
    }
}
