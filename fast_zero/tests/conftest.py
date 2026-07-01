import pytest
from fast_zero.app import app, database
from fast_zero.models import table_registry
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def clear_database():
    database.clear()


@pytest.fixture(scope="module")
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
