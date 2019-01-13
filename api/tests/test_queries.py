from graphene.test import Client

from api.models import Pdv
from api.schema import schema


def test_create_pdv(db_con, snapshot):
    cli = Client(schema)
    resp = cli.execute(
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
                "document": "28563782/12345",
                "address": [-46.57421, -21.785741],
                "coverageArea": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
                ],
            }
        },
    )

    snapshot.assert_match(resp)


def test_all_pdvs(db_con, snapshot):
    Pdv(
        trading_name="Zé Delivery",
        owner_name="Zé",
        document="892046715/46728",
        address=[-46.57421, -21.785741],
        coverage_area=[
            [[[30, 20], [45, 40], [10, 40], [30, 20]]],
            [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
        ],
    ).save()
    Pdv(
        trading_name="Adega Osasco",
        owner_name="Ze da Ambev",
        document="04666182390",
        address=[-43.297337, -23.013538],
        coverage_area=[
            [
                [
                    [-43.36556, -22.99669],
                    [-43.36539, -23.01928],
                    [-43.26583, -23.01802],
                    [-43.25724, -23.00649],
                    [-43.23355, -23.00127],
                    [-43.2381, -22.99716],
                    [-43.23866, -22.99649],
                    [-43.24063, -22.99756],
                    [-43.24634, -22.99736],
                    [-43.24677, -22.99606],
                    [-43.24067, -22.99381],
                    [-43.24886, -22.99121],
                    [-43.25617, -22.99456],
                    [-43.25625, -22.99203],
                    [-43.25346, -22.99065],
                    [-43.29599, -22.98283],
                    [-43.3262, -22.96481],
                    [-43.33427, -22.96402],
                    [-43.33616, -22.96829],
                    [-43.342, -22.98157],
                    [-43.34817, -22.97967],
                    [-43.35142, -22.98062],
                    [-43.3573, -22.98084],
                    [-43.36522, -22.98032],
                    [-43.36696, -22.98422],
                    [-43.36717, -22.98855],
                    [-43.36636, -22.99351],
                    [-43.36556, -22.99669],
                ]
            ]
        ],
    ).save()
    Pdv(
        trading_name="Adega Sao Paulo",
        owner_name="Pedro Silva",
        document="02.453.716/000170",
        address=[-38.59826, -3.774186],
        coverage_area=[
            [
                [
                    [-38.6577, -3.7753],
                    [-38.63212, -3.81418],
                    [-38.61925, -3.82873],
                    [-38.59762, -3.84004],
                    [-38.58727, -3.84345],
                    [-38.58189, -3.8442],
                    [-38.57667, -3.84573],
                    [-38.56706, -3.85015],
                    [-38.56637, -3.84937],
                    [-38.56268, -3.84286],
                    [-38.56148, -3.83772],
                    [-38.55881, -3.82411],
                    [-38.55577, -3.81507],
                    [-38.55258, -3.80674],
                    [-38.54968, -3.80222],
                    [-38.53406, -3.79495],
                    [-38.52894, -3.77718],
                    [-38.52517, -3.76313],
                    [-38.53118, -3.76203],
                    [-38.53968, -3.76126],
                    [-38.54577, -3.76151],
                    [-38.55344, -3.76102],
                    [-38.56327, -3.76029],
                    [-38.58118, -3.75907],
                    [-38.60079, -3.75423],
                    [-38.60671, -3.74772],
                    [-38.61787, -3.7431],
                    [-38.62577, -3.7472],
                    [-38.63332, -3.7496],
                    [-38.65049, -3.76057],
                    [-38.6577, -3.7753],
                ]
            ]
        ],
    ).save()

    cli = Client(schema)

    resp = cli.execute(
        """ query { allPdvs { edges { node { tradingName ownerName document address coverageArea } } } } """
    )

    snapshot.assert_match(resp)


def test_find_pdv(db_con, snapshot):
    pdv = Pdv(
        trading_name="Zé Delivery",
        owner_name="Zé",
        document="89204671546728",
        address=[-46.57421, -21.785741],
        coverage_area=[
            [[[30, 20], [45, 40], [10, 40], [30, 20]]],
            [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
        ],
    ).save()

    cli = Client(schema)

    resp = cli.execute(
        """ query { allPdvs(document: "%s") { edges { node { tradingName ownerName document address coverageArea } } } }"""
        % pdv.document
    )

    snapshot.assert_match(resp)
