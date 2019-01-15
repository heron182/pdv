# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots["test_create_pdv_duplicate_document 1"] = {
    "data": {"createPdv": None},
    "errors": [
        {
            "locations": [{"column": 13, "line": 2}],
            "message": 'Tried to save duplicate unique keys (E11000 duplicate key error collection: pdv_test.pdv index: document_1 dup key: { : "02.453.716/000170" })',
            "path": ["createPdv"],
        }
    ],
}

snapshots["test_create_pdv 1"] = {
    "data": {
        "createPdv": {
            "pdv": {
                "address": '{"type": "Point", "coordinates": [-46.57421, -21.785741]}',
                "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[30.0, 20.0], [45.0, 40.0], [10.0, 40.0], [30.0, 20.0]]], [[[15.0, 5.0], [40.0, 10.0], [10.0, 20.0], [5.0, 10.0], [15.0, 5.0]]]]}',
                "document": "02.453.716/000170",
                "ownerName": "Gloriaaa",
                "tradingName": "Cabo Daciolo",
            }
        }
    }
}

snapshots["test_all_pdvs 1"] = {
    "data": {
        "allPdvs": {
            "edges": [
                {
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-43.297337, -23.013538]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-43.36556, -22.99669], [-43.36539, -23.01928], [-43.26583, -23.01802], [-43.25724, -23.00649], [-43.23355, -23.00127], [-43.2381, -22.99716], [-43.23866, -22.99649], [-43.24063, -22.99756], [-43.24634, -22.99736], [-43.24677, -22.99606], [-43.24067, -22.99381], [-43.24886, -22.99121], [-43.25617, -22.99456], [-43.25625, -22.99203], [-43.25346, -22.99065], [-43.29599, -22.98283], [-43.3262, -22.96481], [-43.33427, -22.96402], [-43.33616, -22.96829], [-43.342, -22.98157], [-43.34817, -22.97967], [-43.35142, -22.98062], [-43.3573, -22.98084], [-43.36522, -22.98032], [-43.36696, -22.98422], [-43.36717, -22.98855], [-43.36636, -22.99351], [-43.36556, -22.99669]]]]}',
                        "document": "02.453.716/000170",
                        "ownerName": "Ze da Ambev",
                        "tradingName": "Adega Osasco",
                    }
                },
                {
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-49.33425, -25.380995]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-49.36299, -25.4515], [-49.35334, -25.45065], [-49.33675, -25.4429], [-49.32291, -25.4398], [-49.3188, -25.44089], [-49.31064, -25.43903], [-49.29828, -25.43391], [-49.29751, -25.43377], [-49.29588, -25.43322], [-49.29215, -25.43189], [-49.28855, -25.43043], [-49.28662, -25.42958], [-49.28424, -25.42865], [-49.25803, -25.42853], [-49.25533, -25.42279], [-49.25585, -25.4169], [-49.25524, -25.40981], [-49.25761, -25.40403], [-49.25524, -25.39787], [-49.26005, -25.39178], [-49.26078, -25.3819], [-49.26267, -25.37348], [-49.25952, -25.37003], [-49.25971, -25.36597], [-49.26301, -25.35774], [-49.26468, -25.34742], [-49.30623, -25.35119], [-49.36262, -25.36639], [-49.37043, -25.3798], [-49.36743, -25.40593], [-49.36837, -25.42578], [-49.36299, -25.4515]]]]}',
                        "document": "04.433.714/0001-44",
                        "ownerName": "Ze da Silva",
                        "tradingName": "Adega Pinheiros",
                    }
                },
                {
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-38.59826, -3.774186]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-38.6577, -3.7753], [-38.63212, -3.81418], [-38.61925, -3.82873], [-38.59762, -3.84004], [-38.58727, -3.84345], [-38.58189, -3.8442], [-38.57667, -3.84573], [-38.56706, -3.85015], [-38.56637, -3.84937], [-38.56268, -3.84286], [-38.56148, -3.83772], [-38.55881, -3.82411], [-38.55577, -3.81507], [-38.55258, -3.80674], [-38.54968, -3.80222], [-38.53406, -3.79495], [-38.52894, -3.77718], [-38.52517, -3.76313], [-38.53118, -3.76203], [-38.53968, -3.76126], [-38.54577, -3.76151], [-38.55344, -3.76102], [-38.56327, -3.76029], [-38.58118, -3.75907], [-38.60079, -3.75423], [-38.60671, -3.74772], [-38.61787, -3.7431], [-38.62577, -3.7472], [-38.63332, -3.7496], [-38.65049, -3.76057], [-38.6577, -3.7753]]]]}',
                        "document": "04666182390",
                        "ownerName": "Pedro Silva",
                        "tradingName": "Adega Sao Paulo",
                    }
                },
                {
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-38.495586, -3.809936]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-38.56586, -3.85041], [-38.49599, -3.87361], [-38.45033, -3.90358], [-38.42304, -3.90273], [-38.37892, -3.88971], [-38.35566, -3.8844], [-38.39557, -3.82497], [-38.41531, -3.80133], [-38.42771, -3.76754], [-38.44251, -3.75054], [-38.45672, -3.75024], [-38.46562, -3.74746], [-38.46525, -3.74657], [-38.46616, -3.74458], [-38.46507, -3.74083], [-38.47256, -3.73743], [-38.47844, -3.72759], [-38.49002, -3.72476], [-38.49573, -3.72254], [-38.51226, -3.71384], [-38.51736, -3.74292], [-38.52517, -3.7681], [-38.53095, -3.78294], [-38.53415, -3.79124], [-38.5412, -3.79573], [-38.55148, -3.80326], [-38.55796, -3.82], [-38.5656, -3.84839], [-38.56586, -3.85041]]]]}',
                        "document": "04698149428",
                        "ownerName": "Joao Silva",
                        "tradingName": "Bar do Ze",
                    }
                },
                {
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-43.432034, -22.747707]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-43.50404, -22.768366], [-43.45254, -22.775646], [-43.429195, -22.804451], [-43.38422, -22.788942], [-43.390743, -22.764568], [-43.355724, -22.739239], [-43.403446, -22.705671], [-43.440525, -22.707571], [-43.4752, -22.698704], [-43.514683, -22.742722], [-43.50404, -22.768366]]]]}',
                        "document": "05202839000126",
                        "ownerName": "Fernando Silva",
                        "tradingName": "Bar Legal",
                    }
                },
            ]
        }
    }
}

snapshots["test_all_pdvs_paginated 1"] = {
    "data": {
        "allPdvs": {
            "edges": [
                {
                    "cursor": "YXJyYXljb25uZWN0aW9uOjA=",
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-43.297337, -23.013538]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-43.36556, -22.99669], [-43.36539, -23.01928], [-43.26583, -23.01802], [-43.25724, -23.00649], [-43.23355, -23.00127], [-43.2381, -22.99716], [-43.23866, -22.99649], [-43.24063, -22.99756], [-43.24634, -22.99736], [-43.24677, -22.99606], [-43.24067, -22.99381], [-43.24886, -22.99121], [-43.25617, -22.99456], [-43.25625, -22.99203], [-43.25346, -22.99065], [-43.29599, -22.98283], [-43.3262, -22.96481], [-43.33427, -22.96402], [-43.33616, -22.96829], [-43.342, -22.98157], [-43.34817, -22.97967], [-43.35142, -22.98062], [-43.3573, -22.98084], [-43.36522, -22.98032], [-43.36696, -22.98422], [-43.36717, -22.98855], [-43.36636, -22.99351], [-43.36556, -22.99669]]]]}',
                        "document": "02.453.716/000170",
                        "ownerName": "Ze da Ambev",
                        "tradingName": "Adega Osasco",
                    },
                },
                {
                    "cursor": "YXJyYXljb25uZWN0aW9uOjE=",
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-49.33425, -25.380995]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-49.36299, -25.4515], [-49.35334, -25.45065], [-49.33675, -25.4429], [-49.32291, -25.4398], [-49.3188, -25.44089], [-49.31064, -25.43903], [-49.29828, -25.43391], [-49.29751, -25.43377], [-49.29588, -25.43322], [-49.29215, -25.43189], [-49.28855, -25.43043], [-49.28662, -25.42958], [-49.28424, -25.42865], [-49.25803, -25.42853], [-49.25533, -25.42279], [-49.25585, -25.4169], [-49.25524, -25.40981], [-49.25761, -25.40403], [-49.25524, -25.39787], [-49.26005, -25.39178], [-49.26078, -25.3819], [-49.26267, -25.37348], [-49.25952, -25.37003], [-49.25971, -25.36597], [-49.26301, -25.35774], [-49.26468, -25.34742], [-49.30623, -25.35119], [-49.36262, -25.36639], [-49.37043, -25.3798], [-49.36743, -25.40593], [-49.36837, -25.42578], [-49.36299, -25.4515]]]]}',
                        "document": "04.433.714/0001-44",
                        "ownerName": "Ze da Silva",
                        "tradingName": "Adega Pinheiros",
                    },
                },
            ]
        }
    }
}

snapshots["test_all_pdvs_paginated 2"] = {
    "data": {
        "allPdvs": {
            "edges": [
                {
                    "cursor": "YXJyYXljb25uZWN0aW9uOjI=",
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-38.59826, -3.774186]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-38.6577, -3.7753], [-38.63212, -3.81418], [-38.61925, -3.82873], [-38.59762, -3.84004], [-38.58727, -3.84345], [-38.58189, -3.8442], [-38.57667, -3.84573], [-38.56706, -3.85015], [-38.56637, -3.84937], [-38.56268, -3.84286], [-38.56148, -3.83772], [-38.55881, -3.82411], [-38.55577, -3.81507], [-38.55258, -3.80674], [-38.54968, -3.80222], [-38.53406, -3.79495], [-38.52894, -3.77718], [-38.52517, -3.76313], [-38.53118, -3.76203], [-38.53968, -3.76126], [-38.54577, -3.76151], [-38.55344, -3.76102], [-38.56327, -3.76029], [-38.58118, -3.75907], [-38.60079, -3.75423], [-38.60671, -3.74772], [-38.61787, -3.7431], [-38.62577, -3.7472], [-38.63332, -3.7496], [-38.65049, -3.76057], [-38.6577, -3.7753]]]]}',
                        "document": "04666182390",
                        "ownerName": "Pedro Silva",
                        "tradingName": "Adega Sao Paulo",
                    },
                },
                {
                    "cursor": "YXJyYXljb25uZWN0aW9uOjM=",
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-38.495586, -3.809936]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-38.56586, -3.85041], [-38.49599, -3.87361], [-38.45033, -3.90358], [-38.42304, -3.90273], [-38.37892, -3.88971], [-38.35566, -3.8844], [-38.39557, -3.82497], [-38.41531, -3.80133], [-38.42771, -3.76754], [-38.44251, -3.75054], [-38.45672, -3.75024], [-38.46562, -3.74746], [-38.46525, -3.74657], [-38.46616, -3.74458], [-38.46507, -3.74083], [-38.47256, -3.73743], [-38.47844, -3.72759], [-38.49002, -3.72476], [-38.49573, -3.72254], [-38.51226, -3.71384], [-38.51736, -3.74292], [-38.52517, -3.7681], [-38.53095, -3.78294], [-38.53415, -3.79124], [-38.5412, -3.79573], [-38.55148, -3.80326], [-38.55796, -3.82], [-38.5656, -3.84839], [-38.56586, -3.85041]]]]}',
                        "document": "04698149428",
                        "ownerName": "Joao Silva",
                        "tradingName": "Bar do Ze",
                    },
                },
            ]
        }
    }
}

snapshots["test_find_pdv 1"] = {
    "data": {
        "allPdvs": {
            "edges": [
                {
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-43.297337, -23.013538]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-43.36556, -22.99669], [-43.36539, -23.01928], [-43.26583, -23.01802], [-43.25724, -23.00649], [-43.23355, -23.00127], [-43.2381, -22.99716], [-43.23866, -22.99649], [-43.24063, -22.99756], [-43.24634, -22.99736], [-43.24677, -22.99606], [-43.24067, -22.99381], [-43.24886, -22.99121], [-43.25617, -22.99456], [-43.25625, -22.99203], [-43.25346, -22.99065], [-43.29599, -22.98283], [-43.3262, -22.96481], [-43.33427, -22.96402], [-43.33616, -22.96829], [-43.342, -22.98157], [-43.34817, -22.97967], [-43.35142, -22.98062], [-43.3573, -22.98084], [-43.36522, -22.98032], [-43.36696, -22.98422], [-43.36717, -22.98855], [-43.36636, -22.99351], [-43.36556, -22.99669]]]]}',
                        "document": "02.453.716/000170",
                        "ownerName": "Ze da Ambev",
                        "tradingName": "Adega Osasco",
                    }
                }
            ]
        }
    }
}

snapshots["test_nearest_pdv 1"] = {
    "data": {
        "nearestPdv": {
            "edges": [
                {
                    "node": {
                        "address": '{"type": "Point", "coordinates": [-38.59826, -3.774186]}',
                        "coverageArea": '{"type": "MultiPolygon", "coordinates": [[[[-38.6577, -3.7753], [-38.63212, -3.81418], [-38.61925, -3.82873], [-38.59762, -3.84004], [-38.58727, -3.84345], [-38.58189, -3.8442], [-38.57667, -3.84573], [-38.56706, -3.85015], [-38.56637, -3.84937], [-38.56268, -3.84286], [-38.56148, -3.83772], [-38.55881, -3.82411], [-38.55577, -3.81507], [-38.55258, -3.80674], [-38.54968, -3.80222], [-38.53406, -3.79495], [-38.52894, -3.77718], [-38.52517, -3.76313], [-38.53118, -3.76203], [-38.53968, -3.76126], [-38.54577, -3.76151], [-38.55344, -3.76102], [-38.56327, -3.76029], [-38.58118, -3.75907], [-38.60079, -3.75423], [-38.60671, -3.74772], [-38.61787, -3.7431], [-38.62577, -3.7472], [-38.63332, -3.7496], [-38.65049, -3.76057], [-38.6577, -3.7753]]]]}',
                        "document": "04666182390",
                        "ownerName": "Pedro Silva",
                        "tradingName": "Adega Sao Paulo",
                    }
                }
            ]
        }
    }
}

snapshots["test_create_pdv_invalid_document_number 1"] = {
    "errors": [{"message": "Invalid document number"}]
}
