"""Module for application utilities"""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
migrate = Migrate(compare_type=True)


def create_app(config_name) -> Flask:
    """Function to create a Flask application"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from analytics import analytics
    app.register_blueprint(analytics)

    # pylint: disable=unused-import
    from analytics.models import Event

    return app
