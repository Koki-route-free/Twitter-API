from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine('sqlite:///:memory', echo=True)

Base = declarative_base()

from model import TwitterInfo

Base.metadata.create_all(bind=engine)              
      
session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
    ))

# 予めテーブル定義の継承元クラスにqueryプロパティを仕込んでおく

Base.query = session.query_property()