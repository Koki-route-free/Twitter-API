import sys
sys.path.append('../')
from conduct.SQL import model
from conduct.SQL.settings import session, engine
from conduct.main.twitter import tweet_search

# テーブルの作成
model.Base.metadata.create_all(bind=engine)
        
# 取得してきたツイートを分類しそれぞれのキーに代入し配列にします
def add_twitter_information():
  # 取得するツイート数
  tweet_count = 1
  tweets = tweet_search(tweet_count)
  # からの配列を作成しfor文でその中に得た値を入れていきます
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

# 実行です
instance_tweet = add_twitter_information()
# 全ての値をテーブルに追加して行きます
session.add_all(instances=instance_tweet)
session.commit()



