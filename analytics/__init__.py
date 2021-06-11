"""Init module"""

from flask import Blueprint
from flask_restful import Api

analytics = Blueprint('analytics', __name__)
api = Api(analytics, prefix="/api")

# pylint: disable=wrong-import-position
from . import routes
