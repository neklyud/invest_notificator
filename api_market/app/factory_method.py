from flask import Flask
from app.config import cfg
from app.core.alchemy import database
from app.api.resource import InstrumentResource
from flask_restful import Api


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = cfg.db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = cfg.track_modification
    database.init_db(app)
    api = Api(app)
    api.prefix = cfg.prefix
    api.add_resource(InstrumentResource, '/instrument/<string:figi>', '/instrument')
    return app
