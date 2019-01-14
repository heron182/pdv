import os

import pytest
from mongoengine import connect
from pymongo import MongoClient

from pdv import create_app
from flask import cli


@pytest.fixture
def app():
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

    connection = MongoClient(db_uri)
    connection.drop_database(db_name)


@pytest.fixture()
def db_con():
    cli.load_dotenv()

    db_uri = os.environ["MONGODB_URI"]
    db_name = os.environ["MONGODB_URI"][::-1].split("/")[0][::-1]

    db_con = connect(host=db_uri)

    yield db_con

    db_con.drop_database(db_name)
