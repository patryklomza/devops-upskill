from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name=None):
    from .main.views import main as main_blueprint

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    app.register_blueprint(main_blueprint)

    db.init_app(app)

    return app
