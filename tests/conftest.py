import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from db import Base


@pytest.fixture
def connection():
    engine = create_engine('sqlite://')
    return engine.connect()


@pytest.fixture()
def create_db(connection):
    Base.metadata.bind = connection
    Base.metadata.create_all()

    yield

    Base.metadata.drop_all()


@pytest.fixture()
def db_session(connection, create_db):
    transaction = connection.begin()

    session = sessionmaker(bind=connection, autoflush=False, autocommit=False)
    session = scoped_session(session)
    Base.query = session.query_property()

    yield session

    transaction.rollback()
    