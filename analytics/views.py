"""Module for analytics controllers (views)"""
from flask_restful import Resource


class InfoApi(Resource):
    """Class for info"""

    def get(self):
        """Information about possible filtering
        (list of attributes and list of values for each attribute)"""
        return {"message": "Success"}, 201
