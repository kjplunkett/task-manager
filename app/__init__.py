from flask import Flask

from app.db import db
from app.routes.task import task_blueprint


def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///:memory:'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the db
    db.init_app(app)

    # Register routes
    app.register_blueprint(task_blueprint)

    with app.app_context():
        # Import models within app context
        from app.db.models import Task

        # Create initial tables from models
        db.create_all()

    return app
