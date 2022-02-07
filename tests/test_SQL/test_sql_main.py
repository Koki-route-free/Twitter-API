import pytest
import sys
sys.path.append('../')
from tests.test_SQL.test_settings import session_engine
from conduct.SQL import model

session_local, engine = session_engine()
# テーブル作成
model.Base.metadata.create_all(bind=engine)

# 実際に値が代入できるのかのテストです
@pytest.fixture(scope="function")
def db():
    test_instance = model.TwitterInfo(
                    id=123456,
                    created_at=1010,
                    text="本文",
                    user_name="名前", 
                    user_screen_name="スクリーンネーム",
                    user_friends_count=10, 
                    user_followers_count=10, 
                    user_description="概要欄"
                  )
    return test_instance
  
def test_id(db):
  assert db.id == 123456
  assert db.created_at == 1010
  assert db.text == "本文" 
  assert db.user_name == "名前"
  assert db.user_screen_name == "スクリーンネーム"
  assert db.user_friends_count == 10
  assert db.user_followers_count == 10
  assert db.user_description == "概要欄"       
  
def test_roll_back(db): 
  try:
    session_local.add(instance=db)
    session_local.commit() 
  except:
    session_local.rollback()
  finally:
    session_local.close()