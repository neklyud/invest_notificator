from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate


class Database:
    def __init__(self):
        self.db = SQLAlchemy()
        self.migrate = Migrate()

    def init_db(self, app):
        if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            create_database(app.config['SQLALCHEMY_DATABASE_URI'])
        self.db.init_app(app)
        with app.app_context():
            self.db.create_all()
            self.db.session.commit()
        self.migrate.init_app(app, self.migrate)
        return self.db

    @property
    def get_database(self):
        return self.db


database = Database()
