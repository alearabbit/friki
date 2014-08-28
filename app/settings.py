# -*- coding: utf-8 -*-


class Config(object):
    SECRET_KEY = "secret_keys"
    FACEBOOK_APP_ID ="1526648867568157"
    FACEBOOK_APP_SECRET = "69358ce6138c07c33f102af172a3835f"

    debug = False


class Production(Config):
    DEBUG = True
    CSRF_ENABLED = False
    ADMIN = "myfriki@gmail.com"
    SQLALCHEMY_DATABASE_URI = "mysql+gaerdbms:///flaskr?instance=myfriki:flaskr-instance"
    migration_directory = "migrations"