"""Module for testing event database model"""
import unittest
from analytics.models import Event


class TestBookModel(unittest.TestCase):
    """
    Class for testing book model
    """

    def setUp(self) -> None:
        """
        Setting up test database and configs
        """
        self.event = Event(brand="Downy", timestamp=1543269600)

    def test_model_str(self) -> None:
        """
        Test book model representation
        """
        self.assertEqual(str(self.event), 'Event <Downy> (2018-11-26)')
