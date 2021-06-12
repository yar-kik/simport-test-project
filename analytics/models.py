"""Module for library database models"""
from datetime import datetime
from utils import db


class Event(db.Model):
    """Class for events entity in database"""
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(14), unique=True)
    asin = db.Column(db.String(10))
    brand = db.Column(db.String(100))
    source = db.Column(db.String(100))
    stars = db.Column(db.SmallInteger)
    timestamp = db.Column(db.Integer)

    def __str__(self):
        date = datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d')
        return f"Event <{self.brand}> ({date})"

    def save(self):
        """Save entity to database"""
        db.session.add(self)
        db.session.commit()
