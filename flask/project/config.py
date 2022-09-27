import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

GITHUB_EVENTS_API_URL = 'https://api.github.com/events'

WATCH_EVENT_TYPE = 'WatchEvent'
PULL_REQUEST_EVENT_TYPE = 'PullRequestEvent'
ISSUE_EVENT_TYPE = 'IssuesEvent'
EVENT_TYPES = [WATCH_EVENT_TYPE, PULL_REQUEST_EVENT_TYPE, ISSUE_EVENT_TYPE]


class Config(object):
    # Flask
    FLASK_ENV = 'development'
    FLASK_DEBUG = 1
    JSONIFY_PRETTYPRINT_REGULAR = True

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
