import requests

from project.extensions import db
from project.models import Event, Repository

from project.config import EVENT_TYPES, GITHUB_EVENTS_API_URL


def load_events():
    r = requests.get(GITHUB_EVENTS_API_URL)
    for event in r.json():
        if event.get('type') in EVENT_TYPES:
            event_exits = db.session.query(Event).filter(Event.id == event.get('id')).first()
            if not event_exits:
                db_event = Event(
                    id=event.get('id'),
                    type=event.get('type'),
                    created_at=event.get('created_at')
                )

                db_repo = db.session.query(Repository).filter(Repository.id == event.get('repo').get('id')).first()
                if db_repo:
                    db_repo.events.append(db_event)
                else:
                    db_repo = Repository(
                        id=event.get('repo').get('id'),
                        name=event.get('repo').get('name'),
                        url=event.get('repo').get('url')
                    )
                    db_repo.events.append(db_event)
                    db.session.add(db_repo)

                db.session.add(db_event)
                db.session.commit()
                db.session.close()
