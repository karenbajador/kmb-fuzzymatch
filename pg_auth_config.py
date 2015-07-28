class Config(object):
    PG_HOST = "HOST_IP_ADDRESS"
    PG_PORT = 'PORT'
    PG_USERNAME = 'USERNAME'
    PG_PASSWORD = 'PASSWORD'
    PG_DB = 'DATABASE_NAME'
    PG_THREADS = 8


class DubaiDevConfig(Config):
    PG_HOST = "localhost"
    PG_PORT = '9999'
    PG_USERNAME = 'karen_user'
    PG_PASSWORD = 'secret'
    PG_DB = 'karen_db'


import os

conf = {
    'DubaiDevConfig': DubaiDevConfig,
    'ProductionConfig': Config
}
#pg_conf = conf.get(os.getenv('PG_ENV'), Config)
pg_conf = DubaiDevConfig

POSTGRESS_HOST = pg_conf.PG_HOST
POSTGRESS_PORT = pg_conf.PG_PORT
POSTGRESS_USERNAME = pg_conf.PG_USERNAME
POSTGRESS_PASSWORD = pg_conf.PG_PASSWORD
POSTGRESS_DB = pg_conf.PG_DB
POSTGRESS_THREADS = pg_conf.PG_THREADS

_all_ = [POSTGRESS_HOST,
         POSTGRESS_PORT,
         POSTGRESS_USERNAME,
         POSTGRESS_PASSWORD,
         POSTGRESS_DB,
         POSTGRESS_THREADS]