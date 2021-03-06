from flask import Flask

from .apps.cores.libs import db, migrate, config
from .apps.samples.views import blueprint as sample_bp


def create_app():
    app = Flask(__name__)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(sample_bp, url_prefix='/api/samples')
