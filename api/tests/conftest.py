import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel
from ..app.core.database import engine
from ..app.main import app


@pytest.fixture(scope='session', autouse=True)
def setup_database():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)

@pytest.fixture()
def client():
    return TestClient(app)