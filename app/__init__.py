from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name=None):
    from .main.views import main as main_blueprint

    app = Flask(__name__)
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:plomza-rds-password@plomza-rds-postgre.cgpzlgzs9ybi.eu-central-1.rds.amazonaws.com:5432/postgres'

    app.register_blueprint(main_blueprint)

    db.init_app(app)

    return app
