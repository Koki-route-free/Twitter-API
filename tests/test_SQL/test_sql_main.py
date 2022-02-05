import pytest
import sys
sys.path.append('../')
from tests.test_SQL.test_settings import session_engine
sys.path.append('../')
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
# 実行です
instance_tweet = add_twitter_information()
session_local.add_all(instances=instance_tweet)
session_local.commit()
