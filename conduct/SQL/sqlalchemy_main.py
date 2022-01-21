import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine('sqlite:///:memory', echo=True)

Base = declarative_base()


class TwitterInfo(Base):
  __tablename__ = 'Twitter Information'
  
  # ツイートID
  id = Column(Integer, primary_key=True)
  # ツイート時間
  created_at = Column(Integer,server_default="NULL")
  # ツイート本文
  text = Column(String,server_default="NULL")
  # ユーザ名
  user_name = Column(String,server_default="NULL")
  # スクリーンネーム
  user_screen_name = Column(String,server_default="NULL")
  # フォロー数
  user_friends_count = Column(Integer,server_default="0")
  # フォロワー数 
  user_followers_count = Column(Integer,server_default="0")
  # ユーザ概要
  user_description = Column(String,server_default="NULL")
  

Base.metadata.create_all(bind=engine)    

session = sessionmaker(bind=engine)()




      
      
 