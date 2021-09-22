import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()


def create_app(config_name=None):
    from .main.views import main as main_blueprint

    app = Flask(__name__)
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:plomza-rds-password@plomza-rds.cgpzlgzs9ybi.eu-central-1.rds.amazonaws.com:5432/postgres'

    app.register_blueprint(main_blueprint)

    while True:
        try:
            db.init_app(app)
        except OperationalError:
            db.create_all()
            continue
        break

    return app
