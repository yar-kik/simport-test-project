from analytics.models import Event
from wsgi import app
from utils import db
from csv import DictReader

events_list = []
filename = 'pydev_test_task_data.csv'
with open(filename, 'r') as csv_file:
    events = DictReader(csv_file)
    with app.app_context():
        for event in events:
            events_list.append(Event(event_id=event["id"],
                                     asin=event["asin"],
                                     brand=event["brand"],
                                     source=event["source"],
                                     stars=event["stars"],
                                     timestamp=event["timestamp"]))

with app.app_context():
    db.session.add_all(events_list)
    db.session.commit()
