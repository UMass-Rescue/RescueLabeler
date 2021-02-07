import app.models as models
from app.db import DBContextManager
from fastapi.testclient import TestClient
from app.main import get_application


def test_db_insert():
    with TestClient(get_application()):
        with DBContextManager() as db:
            simple_user = models.LabelUser(
                username="Me",
                full_name="Me Person",
                email="me@person.com",
                password="badpassword",
            )
            db.add(simple_user)
            db.commit()

        with DBContextManager() as db:
            results = db.query(models.LabelUser).all()
            assert len(results) == 1
            print(results[0])
