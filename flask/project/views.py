import plotly
import plotly.graph_objs as go

import pandas as pd
import json

from datetime import time, timedelta, datetime

from flask import jsonify, render_template, request

from project.extensions import db
from project.models import Event, Repository

from project.config import PULL_REQUEST_EVENT_TYPE, WATCH_EVENT_TYPE, ISSUE_EVENT_TYPE, EVENT_TYPES


def get_repositories():
    repos = []

    for repo in db.session.query(Repository).all():
        event_creations = []
        query = db.session.query(Event).filter(Event.type == PULL_REQUEST_EVENT_TYPE).filter(Event.repository_id == repo.id)
        for event in query.all():
            event_creations.append(event.created_at)

        if event_creations:
            sum_deltas = timedelta(seconds=0)
            i = 1
            while i < len(event_creations):
                sum_deltas += event_creations[i - 1] - event_creations[i]
                i = i + 1

            pull_request_avg_time = (sum_deltas / (len(event_creations) - 1)) if len(event_creations) > 1 else sum_deltas
        else:
            pull_request_avg_time = None

        repo_json = repo.serialize
        repo_json['pull_request_avg_time'] = str(pull_request_avg_time)
        repos.append(repo_json)

    return jsonify(repos)


def get_events_by_type():
    offset = int(request.args.get('offset', 60*24*365*100))
    offset_date = datetime.now() - timedelta(minutes=offset)
    print(offset_date)

    query = db.session.query(Event).filter(Event.created_at >= offset_date)

    events_json = {}
    for event_type in EVENT_TYPES:
        events_json[event_type] = query.filter(Event.type == event_type).count()
    return jsonify(events_json)


def get_events_type_plot():
    x = EVENT_TYPES
    y = []

    query = db.session.query(Event)
    for event_type in EVENT_TYPES:
        y.append(query.filter(Event.type == event_type).count())

    df = pd.DataFrame({'x': x, 'y': y})
    data = [
        go.Bar(
            x=df['x'],
            y=df['y']
        )
    ]

    graph = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', plot=graph)
