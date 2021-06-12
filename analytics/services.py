"""Module for analytics database services"""
from typing import Dict

from sqlalchemy.orm import Query
from werkzeug.datastructures import ImmutableMultiDict

from analytics.models import Event

TYPE = ("cumulative", "usual")
GROUPING = {
    "weekly": "",
    "biWeekly": "",
    "monthly": ""
}
FILTERS = {
    "brand": Event.brand,
    "stars": Event.stars,
    "asin": Event.asin
}


class AnalyticsServices:
    """
    Class to work with database.
    """

    def __init__(self, db_query: Query,
                 search_query: ImmutableMultiDict = None):
        self.db_query = db_query
        self.search_query = search_query

    @property
    def possible_filtering(self) -> Dict[str, list]:
        """
        Return list of values for each attribute.
        """
        filters = {}
        for attribute, field in FILTERS.items():
            values = [getattr(event, attribute) for event in
                      self.db_query(field).distinct().order_by(field).all()]
            filters[attribute] = values
        return filters
