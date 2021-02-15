from app.core.alchemy import database

db = database.get_database


class Instrument(db.Model):
    figi = db.Column(db.String, primary_key=True)
    ticker = db.Column(db.String)
    isin = db.Column(db.String)
    currency = db.Column(db.String)
    type = db.Column(db.String)
    minPriceIncrement = db.Column(db.Integer)
    lot = db.Column(db.Integer)
    minQuantity = db.Column(db.Integer)

    def __repr__(self):
        return '<Instrument %r>' % self.figi

    @classmethod
    def get_instrument(cls, figi):
        return Instrument.query.filter_by(figi).first()

    @classmethod
    def create_instrument(cls, data_for_creation: dict):
        new_instrument = Instrument(**data_for_creation)
        db.session.add(new_instrument)
        db.session.commit()
        return new_instrument
