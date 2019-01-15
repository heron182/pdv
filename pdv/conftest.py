import json
import os

import pytest
from flask import cli
from graphene.test import Client
from mongoengine import connect

from pdv import create_app
from pdv.graphql import schema
from pdv.models import Pdv


@pytest.fixture()
def app():
    cli.load_dotenv()

    os.environ["MONGODB_URI"] = "%s_test" % os.environ["MONGODB_URI"]

    app = create_app()
    app.config["TESTING"] = True

    app_context = app.test_request_context()
    app_context.push()

    yield app

    teardown_database(app)


@pytest.fixture
def client(app):
    client = app.test_client()

    yield client


def teardown_database(app):
    db_uri = app.config["MONGODB_SETTINGS"]["host"]
    db_name = app.config["MONGODB_SETTINGS"]["host"][::-1].split("/")[0][::-1]

    connection = connect(db_uri)
    connection.drop_database(db_name)


@pytest.fixture()
def pdvs():
    fixtures_path = os.path.join(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "tests", "fixtures.json"
        )
    )

    with open(fixtures_path) as fp:
        pdv_fixtures = json.loads(fp.read())

    for pdv in pdv_fixtures["pdvs"][:5]:
        Pdv(**pdv).save()

    return Pdv.objects.all()


@pytest.fixture()
def graph_cli():
    return Client(schema)
