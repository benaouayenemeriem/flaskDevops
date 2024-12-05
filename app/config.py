import os

class Config:
    # SQLAlchemy Database URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:example@mysql:3306/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
