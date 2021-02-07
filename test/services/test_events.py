from fastapi.testclient import TestClient
from app.main import get_application
from sqlalchemy_utils import database_exists
from app.db import engine


def test_db_shutdown():
    # Start with no db
    assert not database_exists(engine.url)

    # Start app
    with TestClient(get_application()):

        # Ensure db exists
        assert database_exists(engine.url)

    # Ensure db clears itself after
    assert not database_exists(engine.url)
