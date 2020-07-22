import os

db_host = os.environ.get('DB_HOST', default='localhost')
db_host = os.environ.get('DB_NAME', default='notes')
db_host = os.environ.get('DB_USERNAME', default='notes')
db_host = os.environ.get('DB_PASSWORD', default='')
db_host = os.environ.get('DB_PORT', default='5432')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

