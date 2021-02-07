from fastapi.testclient import TestClient
from app.main import get_application
from sqlalchemy_utils import database_exists, drop_database
from app.db import engine


def test_db_shutdown():

    # Clear any existing db
    if database_exists(engine.url):
        drop_database(engine.url)
    assert not database_exists(engine.url)

    # Start app
    with TestClient(get_application()):

        # Ensure db exists
        assert database_exists(engine.url)

    # Ensure db clears itself after
    assert not database_exists(engine.url)
