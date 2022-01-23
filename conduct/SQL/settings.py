# 必要ライブラリをインポートします
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String

# データベースのファイルがなければ作成しそのデータベースに格納します（echo=trueでクエリをコンソールに表示します）
engine = create_engine('sqlite:///:memory', echo=True)

# これを使うことによってクラスでデータベースのベース（キーなど）を作成できるようになります
Base = declarative_base()            

# 次にデータベースの操作時の基本設定をします
# コミットは手動にし、オートフラッシュ（エンコードを正確に行う）をtrueにし書き込み先は先ほど指定したengineにします      
session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
    ))

# 予めテーブル定義の継承元クラスにqueryプロパティを仕込んでおきます
Base.query = session.query_property()

# twitter.pyで取得するidと照らし合わせてテーブルキーをつけまとめました
class TwitterInfo(Base):
  # データベースのテーブルネイムです
  __tablename__ = 'Twitter_Information'
  
  id = Column('ツイートID',Integer, primary_key=True)
  created_at = Column('ツイート時間',Integer,server_default="NULL")
  text = Column('ツイート本文',String,server_default="NULL")
  user_name = Column('ユーザ名',String,server_default="NULL")
  user_screen_name = Column('スクリーンネーム',String,server_default="NULL")
  user_friends_count = Column('フォロー数',Integer,server_default="0")
  user_followers_count = Column('フォロワー数 ',Integer,server_default="0")
  user_description = Column('ユーザー概要',String,server_default="NULL") 
  
# クラスを実行し、テーブルを作成します
Base.metadata.create_all(bind=engine)  