import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, drop_database
import sys
sys.path.append('../')
from conduct.SQL.settings import Base

@pytest.fixture(scope="function")
def session_local():
    local_engine = "sqlite:///test_database/:test.db"
    
    engine = create_engine(local_engine, echo=True)

    assert not database_exists(local_engine), "既に存在しています"

    SessionLocal = scoped_session(
      sessionmaker(
        autocommit=False,
        autoflush=True,
        bind=engine
      ))
    Base.query = SessionLocal.query_property()
    Base.metadata.create_all(bind=engine)
    
    yield SessionLocal

    drop_database(local_engine)