import json
import os

import click
from flask.cli import with_appcontext

from pdv.models import Pdv


@click.command("load_fixtures")
@with_appcontext
def load_fixtures():
    fixtures_path = os.path.join(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "tests",
            "fixtures.json",
        )
    )

    with open(fixtures_path) as fp:
        pdv_fixtures = json.loads(fp.read())

    for pdv in pdv_fixtures["pdvs"]:
        Pdv(**pdv).save()
