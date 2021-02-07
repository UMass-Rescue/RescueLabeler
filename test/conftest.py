import pytest
from sqlalchemy_utils import database_exists, drop_database
from app.db import engine


@pytest.fixture(scope="session", autouse=True)
def before_after_all(request):
    clear_db()
    yield
    clear_db()


def clear_db():
    if database_exists(engine.url):
        drop_database(engine.url)
