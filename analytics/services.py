"""Module for analytics database services"""
from datetime import datetime
from typing import Dict

from sqlalchemy.orm import Query
from werkzeug.datastructures import MultiDict

from analytics.models import Event

TYPES = ("cumulative", "usual")
GROUPING = {
    "weekly": 60 * 60 * 24 * 7,
    "biWeekly": 60 * 60 * 24 * 14,
    "monthly": 60 * 60 * 24 * 30
}
FILTERS = {
    "brand": Event.brand,
    "stars": Event.stars,
    "asin": Event.asin
}


def timestamp_to_date(timestamp: int) -> str:
    """
    Convert timestamp to human-readable format
    """
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')


class AnalyticsServices:
    """
    Class to work with database.
    """

    def __init__(self, db_query: Query,
                 search_query: MultiDict = None):
        self.db_query = db_query
        self.search_query = search_query

    @property
    def possible_filters(self) -> Dict[str, list]:
        """
        Return list of values for each attribute.
        """
        filters = {}
        for attribute, field in FILTERS.items():
            values = [getattr(event, attribute) for event in
                      self.db_query(field).distinct().order_by(field).all()]
            filters[attribute] = values
        return filters

    def apply_type(self):
        """
        Apply type (cumulative or usual) by query parameters.
        """
        event_type = self.search_query.get("Type")
        if event_type == "cumulative":
            self.db_query = self.db_query
        if event_type == "usual":
            self.db_query = self.db_query
        return self

    def apply_grouping(self):
        """
        Apply grouping type (weekly, bi-weekly or monthly) by query parameters.
        """
        event_grouping = self.search_query.get("Grouping")
        if event_grouping in GROUPING:
            self.db_query = self.db_query. \
                group_by(Event.timestamp / GROUPING[event_grouping])
        return self
