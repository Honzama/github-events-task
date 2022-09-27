from flask import Flask

from .extensions import db
from .views import get_repositories, get_events_by_type, get_events_type_plot


def register_extensions(app):
    db.init_app(app)


def add_views(app):
    app.add_url_rule('/repositories', view_func=get_repositories)
    app.add_url_rule('/events/type', view_func=get_events_by_type)
    app.add_url_rule('/events/plot', view_func=get_events_type_plot)


def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.Config")

    register_extensions(app)
    add_views(app)

    return app


app = create_app()
