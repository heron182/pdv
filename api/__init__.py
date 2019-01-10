from logging.config import dictConfig

from flask import Flask, cli


def create_app():
    cli.load_dotenv()

    from .settings import BaseSettings, LOGGING

    dictConfig(LOGGING)

    app = Flask(__name__)
    app.config.from_object(BaseSettings)
    app.url_map.strict_slashes = False

    return app
