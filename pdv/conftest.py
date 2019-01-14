import json
import os

import pytest
from flask import cli
from graphene.test import Client
from mongoengine import connect

from pdv.graphql import schema
from pdv.models import Pdv


@pytest.fixture()
def db_con():
    cli.load_dotenv()

    db_uri = os.environ["MONGODB_URI"]
    db_name = os.environ["MONGODB_URI"][::-1].split("/")[0][::-1]

    db_con = connect(host=db_uri)

    yield db_con

    db_con.drop_database(db_name)


@pytest.fixture()
def pdvs():
    fixtures_path = os.path.join(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "tests", "fixtures.json"
        )
    )

    with open(fixtures_path) as fp:
        pdv_fixtures = json.loads(fp.read())

    for pdv in pdv_fixtures["pdvs"]:
        Pdv(**pdv).save()

    return Pdv.objects.all()


@pytest.fixture()
def graph_cli():
    return Client(schema)
