import pytest
import sys
sys.path.append('../')
from tests.test_SQL.test_settings import session_engine
from conduct.SQL import model
from conduct.main.twitter import tweet_search


session_local, engine = session_engine()
# テーブル作成
model.Base.metadata.create_all(bind=engine)

# 取得してきたツイートを分類しそれぞれのキーに代入し配列にします
def add_twitter_information():
  # 取得するツイート数
  tweet_count = 1
  tweets = tweet_search(tweet_count)
  instance_tweet = []
  for tweet in tweets:
     a = model.TwitterInfo(
       id=tweet.id,
       created_at=tweet.created_at,
       text=tweet.text,
       user_name=tweet.user.name, 
       user_screen_name=tweet.user.screen_name,
       user_friends_count=tweet.user.friends_count, 
       user_followers_count=tweet.user.followers_count, 
       user_description=tweet.user.description
      )
     instance_tweet.append(a)
  return instance_tweet

# 配列に何かしらの要素が入っているかのテストです
def test_add_twiter_information():
  assert add_twitter_information()

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
    session_local.flush() 
    session_local.commit() 
  except:
    session_local.rollback()
  finally:
    session_local.close()