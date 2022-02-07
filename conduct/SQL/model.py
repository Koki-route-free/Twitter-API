from sqlalchemy import Column, Integer, String
import sys
sys.path.append('../')
from conduct.SQL.settings import Base


# twitter.pyで取得するidと照らし合わせてテーブルキーをつけまとめました
class TwitterInfo(Base):
  # データベースのテーブルネイムです
  __tablename__ = 'Twitter_Information'
  # データベースのテーブルキーとタイトルです
  id = Column('ツイートID',Integer, primary_key=True)
  created_at = Column('ツイート時間',Integer,server_default="NULL")
  text = Column('ツイート本文',String,server_default="NULL")
  user_name = Column('ユーザ名',String,server_default="NULL")
  user_screen_name = Column('スクリーンネーム',String,server_default="NULL")
  user_friends_count = Column('フォロー数',Integer,server_default="0")
  user_followers_count = Column('フォロワー数',Integer,server_default="0")
  user_description = Column('ユーザー概要',String,server_default="NULL") 