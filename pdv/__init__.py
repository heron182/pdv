from logging.config import dictConfig

from flask import Flask, cli
from flask_graphql import GraphQLView
from flask_mongoengine import MongoEngine

from pdv.commands import load_fixtures

from .graphql import schema


def create_app():
    cli.load_dotenv()

    from .settings import BaseSettings, LOGGING

    dictConfig(LOGGING)

    app = Flask(__name__)
    app.config.from_object(BaseSettings)
    app.url_map.strict_slashes = False
    configure_commands(app)
    configure_extensions(app)
    configure_rules(app)

    return app


def configure_commands(app):
    app.cli.add_command(load_fixtures)


def configure_extensions(app):
    db = MongoEngine()
    db.init_app(app)


def configure_rules(app):
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )
