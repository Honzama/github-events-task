from flask.cli import FlaskGroup

from project import app
from project.extensions import db
from project import scripts

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    db.session.close()


@cli.command("load_events")
def load_events():
    scripts.load_events()


if __name__ == "__main__":
    cli()
