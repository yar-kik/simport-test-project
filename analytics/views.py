"""Module for analytics controllers (views)"""
from flask_restful import Resource

from analytics.services import AnalyticsServices
from utils import db


class InfoApi(Resource):
    """
    Class for info endpoint.
    """

    def get(self):
        """
        Information about possible filtering
        (list of attributes and list of values for each attribute)
        """
        analytic_services = AnalyticsServices(db.session.query)
        all_filters = analytic_services.possible_filtering
        return all_filters


class TimelineApi(Resource):
    """
    Class for timeline endpoint.
    """

    def get(self):
        """
        Number of events with applied type, grouping, filters,
        and date range.
        """
        return {"message": "Timeline"}
