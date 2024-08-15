from flask import Flask

from .db import db
from .routes.task import task_blueprint


def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Configure the db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the db
    db.init_app(app)

    # Register routes
    app.register_blueprint(task_blueprint)

    with app.app_context():
        # Create the db tables
        db.create_all()

    return app
