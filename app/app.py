import os.path

from flask import Flask

from app.api.cars import cars
from app.api.home import home
from app.extensions import db, migrate


def create_app(app_name="CarChecker",) -> Flask:
    app = Flask(app_name, )
    app.config.from_object("app.config")

    app.template_folder = app.config.get("TEMPLATES_DIR")
    if app.config.get("SQLALCHEMY_DATABASE_URI") is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(cars)
    app.register_blueprint(home)
    if app.config["DEBUG"]:
        from app.api.testing import testing
        app.register_blueprint(testing)
    return app


app = create_app()
