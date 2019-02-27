from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from .forms import login_manager

db = SQLAlchemy()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('main', 'cmdb'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app, db):
    # @app.teardown_request
    # def shutdown_session(exception=None):
    #     db.session.remove()

    migrate = Migrate(app, db)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app, resources={r'/asset/network': {'origins': '*'}})
    register_extensions(app)
    register_blueprints(app)
    configure_database(app, db)

    return app
