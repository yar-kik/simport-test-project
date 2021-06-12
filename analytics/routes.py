"""Module for API routes"""

from . import api
from .views import InfoApi, TimelineApi

api.add_resource(InfoApi, '/info')
api.add_resource(TimelineApi, '/timeline')