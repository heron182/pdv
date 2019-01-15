def test_create_pdv(db_con, snapshot, graph_cli):
    resp = graph_cli.execute(
        """mutation createPdv($input: CreatePdvInput!) {
            createPdv(input: $input) {
                pdv {
                    tradingName
                    ownerName
                    document
                    address
                    coverageArea
                }
            }
        }""",
        variables={
            "input": {
                "tradingName": "Cabo Daciolo",
                "ownerName": "Gloriaaa",
                "document": "02.453.716/000170",
                "address": [-46.57421, -21.785741],
                "coverageArea": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
                ],
            }
        },
    )

    snapshot.assert_match(resp)


def test_create_pdv_invalid_document_number(db_con, snapshot, graph_cli):
    resp = graph_cli.execute(
        """mutation createPdv($input: CreatePdvInput!) {
            createPdv(input: $input) {
                pdv {
                    tradingName
                    ownerName
                    document
                    address
                    coverageArea
                }
            }
        }""",
        variables={
            "input": {
                "tradingName": "Cabo Daciolo",
                "ownerName": "Gloriaaa",
                "document": "18375667000170",
                "address": [-46.57421, -21.785741],
                "coverageArea": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
                ],
            }
        },
    )

    snapshot.assert_match(resp)


def test_create_pdv_duplicate_document(db_con, snapshot, graph_cli, pdvs):
    existing_pdv = pdvs.first()

    resp = graph_cli.execute(
        """mutation createPdv($input: CreatePdvInput!) {
            createPdv(input: $input) {
                pdv {
                    tradingName
                    ownerName
                    document
                    address
                    coverageArea
                }
            }
        }""",
        variables={
            "input": {
                "tradingName": "Lojinha Soprano",
                "ownerName": "Tony",
                "document": existing_pdv.document,
                "address": [70, 22],
                "coverageArea": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
                ],
            }
        },
    )

    snapshot.assert_match(resp)


def test_all_pdvs(db_con, snapshot, pdvs, graph_cli):
    resp = graph_cli.execute(
        """ query { allPdvs { edges { node { tradingName ownerName document address coverageArea } } } } """
    )

    snapshot.assert_match(resp)


def test_all_pdvs_paginated(db_con, snapshot, pdvs, graph_cli):
    resp = graph_cli.execute(
        """ query { allPdvs(first: 2) { edges { node { tradingName ownerName document address coverageArea } cursor } } } """
    )

    snapshot.assert_match(resp)
    assert len(resp["data"]["allPdvs"]["edges"]) == 2

    cursor = resp["data"]["allPdvs"]["edges"][1]["cursor"]

    resp = graph_cli.execute(
        """ query { allPdvs(first: 2, after: "%s") { edges { node { tradingName ownerName document address coverageArea } cursor } } } """
        % cursor
    )

    snapshot.assert_match(resp)
    assert len(resp["data"]["allPdvs"]["edges"]) == 2


def test_find_pdv(db_con, snapshot, pdvs, graph_cli):
    document = pdvs[0].document

    resp = graph_cli.execute(
        """ query { allPdvs(document: "%s") { edges { node { tradingName ownerName document address coverageArea } } } }"""
        % document
    )

    snapshot.assert_match(resp)


def test_nearest_pdv(db_con, snapshot, pdvs, graph_cli):
    user_coord = [-41.25625, -3.85015]

    resp = graph_cli.execute(
        """ query { nearestPdv(coord: %s) { edges { node { tradingName ownerName document address coverageArea } } } }"""
        % user_coord
    )

    snapshot.assert_match(resp)
