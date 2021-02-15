from flask_restful import (
    Resource,
    marshal_with,
)
from app.api.model import Instrument
from flask import request
from app.api.schemas import (
    InstrumentOutSchema,
    resource_fields,
)
from app.core.alchemy import database


class InstrumentResource(Resource):
    def __init__(self):
        super().__init__()
        self.database = database

    @marshal_with(resource_fields)
    def get(self, figi: str):
        instrument = Instrument.get_instrument(figi=figi)
        response = InstrumentOutSchema()
        response.init(instrument)
        return response.encode()

    def post(self):
        data = request.get_json()
        new_instrument = Instrument.create_instrument(data)
        response = InstrumentOutSchema()
        response.init(data)
        return response.encode()
