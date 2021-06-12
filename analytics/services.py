"""Module for analytics database services"""
from datetime import datetime
from typing import Dict

from sqlalchemy import and_
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
    Convert timestamp to human-readable format.
    """
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')


def date_to_timestamp(date: str) -> int:
    """
    Convert date to timestamp in seconds.
    """
    return int(datetime.strptime(date, '%Y-%m-%d').timestamp())


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

    def apply_date_interval(self):
        """
        Apply start and end date.
        """
        start_date = self.search_query.get("startDate")
        end_date = self.search_query.get("endDate")
        if start_date and end_date:
            self.db_query = self.db_query.filter(
                and_(date_to_timestamp(start_date) <= Event.timestamp,
                     date_to_timestamp(end_date) >= Event.timestamp))
        return self

    def apply_filters(self):
        """
        Apply type (cumulative or usual).
        """
        for event_filter in self.search_query:
            if event_filter in FILTERS:
                self.db_query = self.db_query.filter(
                    FILTERS[event_filter].in_(
                        self.search_query.getlist(event_filter)))
        return self

    def apply_type(self):
        """
        Apply type (cumulative or usual) and return result.
        """
        data = []
        value = 0
        event_type = self.search_query.get("Type")
        # TODO: make more readable
        for event in self.db_query.all():
            if event_type == "cumulative":
                value += event.count
                data.append({"date": timestamp_to_date(event.date),
                             "value": value})
            else:
                data.append({"date": timestamp_to_date(event.date),
                             "value": event.count})
        return data

    def apply_grouping(self):
        """
        Apply grouping type (weekly, bi-weekly or monthly) by query parameters.
        """
        event_grouping = self.search_query.get("Grouping")
        if event_grouping in GROUPING:
            self.db_query = self.db_query. \
                group_by(Event.timestamp / GROUPING[event_grouping])
        return self
