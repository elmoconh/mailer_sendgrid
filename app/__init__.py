import os 
from flask import Flask




def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SENDGRID_KEY = os.environ.get('SENDGRID_KEY'),
        SECRET_KEY = os.environ.get('SECRET_KEY'),
        DATABASE_HOST = os.environ.get('DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get('DATABASE_USER'),
        DATABASE_NAME = os.environ.get('DATABASE_NAME'),
    )
    from .  import db

    db.init_app(app)
    return app

