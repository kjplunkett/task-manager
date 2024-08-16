import os

from flask import Flask, send_from_directory

from app.db import db
from app.routes.task import task_blueprint


def create_app():
    # Initialize the Flask app
    app = Flask(__name__, static_folder="../build")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the db
    db.init_app(app)

    # Register Task API routes
    app.register_blueprint(task_blueprint, url_prefix="/api/v1/")

    with app.app_context():
        # Import models within app context
        from app.db.models import Task  # noqa: F401

        # Create initial tables from models
        db.create_all()

    # Serve React App
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve(path):
        if path != "" and os.path.exists(app.static_folder + "/" + path):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, "index.html")

    return app
