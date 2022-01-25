from fastapi import Depends, FastAPI, HTTPException
import sys
sys.path.append('../')
from conduct.SQL import model
from conduct.SQL.settings import Session_local, session, engine
from conduct.main.twitter import TweetSearch

# table作成
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = Session_local() # sessionを生成
        yield db
    finally:
        db.close()

# 取得するツイート数
tweet_count = 1

# twitter.pyのツイート取得を実行しています。詳しくはtwitter_api.ipynbをご覧ください
tweet_search = TweetSearch(tweet_count)
 
# 取得してきたツイートを分類しそれぞれのキーに代入し配列にしてまとめてコミットしています。  
def AddTwitterInfo(tweets, session):
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
  session.add_all(instances=instance_tweet)
  session.commit()

# 実行です
AddTwitterInfo(tweet_search, session)

