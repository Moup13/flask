import os

APP_NAME = "docker-flask"


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")
    DEBUG = True


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    STATIC_FOLDER = "/home/alex/projects/allprojects/all/pythonprojects/flask/docker-flask/services/web/project/static/"
    MEDIA_FOLDER = "/home/alex/projects/allprojects/all/pythonprojects/flask/docker-flask/services/web/project/media/"
    print("Static folder",STATIC_FOLDER)
    print("Media folder",MEDIA_FOLDER)
    DEBUG = False
