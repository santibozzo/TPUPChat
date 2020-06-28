import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
