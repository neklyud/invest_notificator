from flask import jsonify
from flask_restful import fields

resource_fields = {
    'figi': fields.String,
    'ticker': fields.String,
    'isin': fields.String,
    'currency': fields.String,
    'type': fields.String,
    'minPriceIncrement': fields.Integer,
    'lot': fields.Integer,
    'minQuantity': fields.Integer,
}


class BaseInstrument(object):
    def __init__(self):
        self.figi = None
        self.ticker = None
        self.isin = None
        self.currency = None
        self.type = None
        self.minPriceIncrement = None
        self.lot = None
        self.minQuantity = None

    def init(self, parameters: dict) -> None:
        for i_key, i_val in parameters.items():
            if i_key in resource_fields.keys():
                setattr(self, i_key, i_val)


class InstrumentOutSchema(BaseInstrument):
    def __init__(self):
        super().__init__()

    def encode(self):
        return jsonify(self.__dict__)
