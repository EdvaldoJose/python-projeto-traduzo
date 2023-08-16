import pytest

from src.app import app
from src.database.db import db


@pytest.fixture(autouse=True)
def app_test():
    return app.test_client()


@pytest.fixture(autouse=True)
def prepare_base(app_test):
    db.get_collection("history").drop()
    app_test.post(
        "/",
        data={
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )

    app_test.post(
        "/",
        data={
            "text-to-translate": "Do you love music?",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )
