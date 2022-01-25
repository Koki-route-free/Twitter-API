import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, drop_database
import sys
sys.path.append('../')
from conduct.SQL.settings import Base

@pytest.fixture(scope="function")
def SessionLocal():
    TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///test_database/test_temp.db"
    engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

    assert not database_exists(TEST_SQLALCHEMY_DATABASE_URL), "既に存在しています"

    Base.metadata.create_all(engine)
    SessionLocal = scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=True,
            bind=engine
            ))

    yield SessionLocal

    drop_database(TEST_SQLALCHEMY_DATABASE_URL)