from project.extensions import db


class Repository(db.Model):
    __tablename__ = "repository"

    id = db.Column('id', db.BigInteger, primary_key=True)
    name = db.Column('name', db.String(255), unique=False, nullable=False)
    url = db.Column('url', db.String(255), unique=False, nullable=False)
    events = db.relationship('Event', backref='repository')

    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url
        }


class Event(db.Model):
    __tablename__ = "event"

    id = db.Column('id', db.BigInteger, primary_key=True)
    type = db.Column('type', db.String(255), unique=False, nullable=False)
    created_at = db.Column('created_at', db.DateTime, unique=False, nullable=False)
    repository_id = db.Column('repository_id', db.BigInteger, db.ForeignKey('repository.id'))

    def __init__(self, id, type, created_at):
        self.id = id
        self.type = type
        self.created_at = created_at

    @property
    def serialize(self):
        return {
            'id': self.id,
            'type': self.type,
            'created_at': str(self.created_at)
        }
