from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import drop_database

# テスト用のエンジンを作成します。ここではsqliteを使用しています。
def session_engine():
  local_engine = "sqlite:///test_database/:testdata"

  # データベースのファイルがなければ作成しそのデータベースに格納します（echo=trueでクエリをコンソールに表示します）
  engine = create_engine(local_engine, echo=True)
  # 次にデータベースの操作時の基本設定をします
  # コミットは手動にし、オートフラッシュ（エンコードを正確に行う）をtrueにし書き込み先は先ほど指定したengineにします 
  session_local = scoped_session(
    sessionmaker(
      autocommit=False,
      autoflush=True,
      bind=engine
      ))
  
  return session_local, engine

  # yield Session_local
  # yield engine
  # drop_database(local_engine)