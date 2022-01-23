from settings import session, TwitterInfo
import sys
import os
sys.path.append(os.path.abspath(".."))
from main import twitter 

# 取得するツイート数
tweet_count = 10

# twitter.pyのツイート取得を実行しています。詳しくはtwitter_api.ipynbをご覧ください
tweet_search = twitter.TweetSearch(tweet_count)
 
# 取得してきたツイートを分類しそれぞれのキーに代入し配列にしてまとめてコミットしています。      
def AddTwitterInfo(tweets):
  instance_tweet = []
  for tweet in tweets:
     a = TwitterInfo(
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

AddTwitterInfo(tweet_search)



      
      
 