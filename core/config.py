import os

SECRET_KEY = os.environ.get('SECRET_KEY')

DB_ENGINE = os.environ.get('DB_ENGINE')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_PORT = os.environ.get('DB_PORT')
DB_HOST = os.environ.get('DB_HOST')
