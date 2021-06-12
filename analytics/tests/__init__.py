"""Init module for testing"""
import unittest

from analytics.models import Event
from utils import create_app, db


def create_event():
    """Create new event in test db"""
    event = Event(event_id="R11QPQWAH45REP",
                  asin="B0014D3N0Q",
                  brand="Downy",
                  source="amazon",
                  stars=5,
                  timestamp=1548799200)
    db.session.add(event)
    db.session.commit()


class BaseCase(unittest.TestCase):
    """Base test configurations"""

    def setUp(self) -> None:
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app.app_context().push()
        db.create_all()
        create_event()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
