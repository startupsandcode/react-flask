import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:PASSWORD@localhost:3306/tuts'
    SQLALCHEMY_TRACK_MODIFICATIONS = False