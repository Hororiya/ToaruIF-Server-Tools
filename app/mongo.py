from flask_pymongo import PyMongo
from flask import current_app

mongo = PyMongo()

def init_mongo(app):
    mongo.init_app(app)