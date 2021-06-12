"""Module for analytics controllers (views)"""
from flask import request
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
        filters = analytic_services.possible_filters
        return filters


class TimelineApi(Resource):
    """
    Class for timeline endpoint.
    """

    def get(self):
        """
        Number of events with applied type, grouping, filters,
        and date range.
        """
        analytic_services = AnalyticsServices(db.session.query, request.args)
        data = analytic_services \
            .apply_date_interval() \
            .apply_filters() \
            .apply_grouping() \
            .apply_type_and_return_result()
        return {"timeline": data}
