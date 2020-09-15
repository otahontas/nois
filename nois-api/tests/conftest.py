import pytest
from alembic.config import main
from starlette.config import environ
from starlette.testclient import TestClient

environ["TESTING"] = "TRUE"


@pytest.fixture
def client():
    from nois_api.app import db, get_app

    with TestClient(get_app()) as client:
        yield client
