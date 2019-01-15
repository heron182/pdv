def test_create_pdv(app, snapshot, graph_cli):
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


def test_create_pdv_required_parameters(app, snapshot, graph_cli):
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
                "tradingName": None,
                "ownerName": None,
                "document": None,
                "address": None,
                "coverageArea": None,
            }
        },
    )

    snapshot.assert_match(resp)


def test_create_pdv_invalid_document_number(app, snapshot, graph_cli):
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
                "document": "02.453.716/",
                "address": [-46.57421, -21.785741],
                "coverageArea": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
                ],
            }
        },
    )

    snapshot.assert_match(resp)


def test_create_pdv_invalid_address(app, snapshot, graph_cli):
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
                "address": [-46.57421, -21.785741, -21.785741],
                "coverageArea": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
                ],
            }
        },
    )

    snapshot.assert_match(resp)

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
                "address": [-46.57421],
                "coverageArea": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
                ],
            }
        },
    )

    snapshot.assert_match(resp)


def test_create_pdv_invalid_coverage_area(app, snapshot, graph_cli):
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
                "address": [-46.57421, -21.785741, -21.785741],
                "coverageArea": [
                    [[[30, 20], [45, 40], [10, 40]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
                ],
            }
        },
    )

    snapshot.assert_match(resp)

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
                "address": [-46.57421],
                "coverageArea": [
                    [[[30, 20, 50], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20, 80], [5, 10], [15, 5]]],
                ],
            }
        },
    )

    snapshot.assert_match(resp)


def test_create_pdv_duplicate_document(app, snapshot, graph_cli, pdvs):
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


def test_all_pdvs(app, snapshot, pdvs, graph_cli):
    resp = graph_cli.execute(
        """ query { allPdvs { edges { node { tradingName ownerName document address coverageArea } } } } """
    )

    snapshot.assert_match(resp)


def test_all_pdvs_paginated(app, snapshot, pdvs, graph_cli):
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


def test_find_pdv_by_id(app, snapshot, pdvs, graph_cli):
    pdv = pdvs.first()

    resp = graph_cli.execute(
        """ query { allPdvs(id: "%s") { edges { node { tradingName ownerName document address coverageArea } } } }"""
        % pdv.id
    )

    snapshot.assert_match(resp)


def test_nearest_pdv(app, snapshot, pdvs, graph_cli):
    user_coord = [-41.25625, -3.85015]

    resp = graph_cli.execute(
        """ query { nearestPdv(coord: %s) { edges { node { tradingName ownerName document address coverageArea } } } }"""
        % user_coord
    )

    snapshot.assert_match(resp)


def test_nearest_pdv_invalid_coord(app, snapshot, pdvs, graph_cli):
    user_coord = [-41.25625]

    resp = graph_cli.execute(
        """ query { nearestPdv(coord: %s) { edges { node { tradingName ownerName document address coverageArea } } } }"""
        % user_coord
    )

    snapshot.assert_match(resp)

    user_coord = None

    resp = graph_cli.execute(
        """ query { nearestPdv(coord: %s) { edges { node { tradingName ownerName document address coverageArea } } } }"""
        % user_coord
    )

    snapshot.assert_match(resp)
