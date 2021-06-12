"""Module for analytics controllers (views)"""
from flask import request
from flask_restful import Resource
from sqlalchemy.sql.functions import count, func

from analytics.models import Event
from analytics.services import AnalyticsServices, timestamp_to_date
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
        analytic_services = AnalyticsServices(
            db.session.query(func.min(Event.timestamp).label("date"),
                             count(Event.timestamp)
                             .label("count")), request.args)
        events = analytic_services.apply_grouping().db_query
        data = [{"date": timestamp_to_date(event.date),
                 "value": event.count} for event in events.all()]
        return {"timeline": data}
