import os
from dotenv import load_dotenv

load_dotenv()
DB_SERVER = os.getenv('DB_SERVER')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_DATABASE')

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'pg://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_SERVER + '/' + DB_NAME