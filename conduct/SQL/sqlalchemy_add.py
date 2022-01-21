from sqlalchemy_main import *
import sys
import os
sys.path.append(os.path.abspath(".."))
import main.config_main as config_main
from main.twitter import TweetSearch

# 取得するツイート数
tweet_count = 3

tweet_search = TweetSearch(tweet_count)

twitter_info = TwitterInfo()

def AddTwitterInfo(tweets):
    for tweet in tweets:
      twitter_info.id = tweet.id
      twitter_info.created_at = tweet.created_at
      twitter_info.text = tweet.text
      twitter_info.user_name = tweet.user.name 
      twitter_info.user_screen_name = tweet.user.screen_name
      twitter_info.user_friends_count = tweet.user.friends_count 
      twitter_info.user_followers_count = tweet.user.followers_count 
      twitter_info.user_description = tweet.user.description

AddTwitterInfo(tweet_search)


# 実行
session.add(instance=twitter_info)
session.commit()