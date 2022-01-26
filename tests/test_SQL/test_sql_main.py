import sys
sys.path.append('../')
from tests.test_SQL.conftest import pytest_session_engine
sys.path.append('../')
from conduct.SQL import model
from conduct.main.twitter import TweetSearch


Session_local, engine = pytest_session_engine()
# table作成
model.Base.metadata.create_all(bind=engine)

# 取得してきたツイートを分類しそれぞれのキーに代入し配列にしてまとめてコミットしています。  
def AddTwitterInfo():
  # 取得するツイート数
  tweet_count = 1
  # twitter.pyのツイート取得を実行しています。詳しくはtwitter_api.ipynbをご覧ください
  tweets = TweetSearch(tweet_count)
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

session = Session_local()

# 実行です
instance_tweet = AddTwitterInfo()

session.add_all(instances=instance_tweet)
session.commit()
