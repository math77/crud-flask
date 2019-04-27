import os
from dotenv import load_dotenv
from db import DatabaseSettings


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = 'Qwe_$#@!asd'
    SQLALCHEMY_DATABASE_URI = DatabaseSettings.get_db()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
