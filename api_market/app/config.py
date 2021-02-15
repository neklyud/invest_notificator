from betterconf import Config, field
from betterconf.caster import to_bool


class LocalConfig(Config):
    db_uri = field('SQLALCHEMY_DATABASE_URI', default='postgresql://postgres:postgres@localhost:5432/instruments')
    track_modification = field('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, caster=to_bool)
    prefix = field('API_PREFIX', default='/api')


cfg = LocalConfig()
