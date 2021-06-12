"""Module for different configurations such as 'production', 'development'
or 'testing.'"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY', "hardtorememberstring")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        """Function for application initialization. It could be add
        some functionality in future"""


class DevelopmentConfig(Config):
    """Configurations for development"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
                              "sqlite:///" + os.path.join(basedir,
                                                          'data-dev.sqlite')


class TestingConfig(Config):
    """Configurations for testing"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'


class ProductionConfig(Config):
    """Configurations for production"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URL") or \
                              "postgresql://postgres:postgres@localhost:5432/postgres"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
