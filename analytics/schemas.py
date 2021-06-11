"""Module for deserialization and serialization analytics models"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Event


class EventSchema(SQLAlchemyAutoSchema):
    """Class for events model serialization/deserialization"""
    # pylint: disable=missing-class-docstring
    class Meta:
        model = Event
        exclude = ('id',)
        load_instance = True
