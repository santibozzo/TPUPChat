import os

"""Base configuration for all profiles"""
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretKey'

"""Configuration for development profile"""
class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

"""Configuration for testing profile"""
class TestingConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

"""Configuration for production profile"""
class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
