import pytest
from app import create_app, db


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            # Create the db tables
            db.create_all()

            # Provide the client to each test
            yield client

            # Tear down the db after each test
            db.drop_all()
