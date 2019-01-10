from graphene.test import Client
from api.schema import schema
from api.models import Pdv


def test_create_pdv(db_con, snapshot):
    cli = Client(schema)
    resp = cli.execute(
        """mutation createPdv($input: CreatePdvInput!) {
            createPdv(input: $input) {
                pdv {
                    tradingName
                    ownerName
                    document
                }
            }
        }""",
        variables={
            "input": {
                "tradingName": "Cabo Daciolo",
                "ownerName": "Gloriaaa",
                "document": "28563782/12345",
            }
        },
    )

    snapshot.assert_match(resp)


def test_all_pdvs(db_con, snapshot):
    Pdv(trading_name="Zé Delivery", owner_name="Zé", document="892046715/46728").save()
    Pdv(
        trading_name="Dudu Delivery", owner_name="Dudu", document="6288172645/9816"
    ).save()
    Pdv(
        trading_name="Deyverson Delivery",
        owner_name="Deyvinho",
        document="2366518955/8144",
    ).save()

    cli = Client(schema)

    resp = cli.execute(
        """ query { allPdvs { edges { node { id tradingName ownerName document } } } } """
    )

    snapshot.assert_match(resp)
