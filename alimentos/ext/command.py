import click

from alimentos.ext.database import db
from alimentos.models import AlimentosModel

def create_db():
    db.create_all()

def drop_db():
    db.drop_all()

def init_app(app):
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))

    @app.cli.command()