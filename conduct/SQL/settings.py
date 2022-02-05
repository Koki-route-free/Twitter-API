# 必要ライブラリをインポートします
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


# これを使うことによってクラスでデータベースのベース（キーなど）を作成できるようになります
Base = declarative_base()            
  

# ここにpostgresqlの情報を入力してください
DATABASE = 'postgresql'
USER = 'i'
PASSWORD = 'i'
HOST = 'localhost'
PORT = '8000'
DB_NAME = 'conduct.db'

CONNECT_STR = '{}://{}:{}@{}:{}/database/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

# データベースのファイルがなければ作成しそのデータベースに格納します（echo=trueでクエリをコンソールに表示します）
engine = create_engine(CONNECT_STR, echo=True) 

# 次にデータベースの操作時の基本設定をします
# コミットは手動にし、オートフラッシュ（エンコードを正確に行う）をtrueにし書き込み先は先ほど指定したengineにします 
session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
    ))
