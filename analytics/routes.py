"""Module for API routes"""

from . import api
from .views import InfoApi

api.add_resource(InfoApi, '/info')
