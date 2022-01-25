import sys
sys.path.append('../')
# from conduct.main import config_main
from conduct.main.twitter import TweetSearch
from conduct.SQL.settings import TwitterInfo
from sql_main import AddTwitterInfo, tweet_search
from test_sql_main import session_local 

session = session_local()

# 取得するツイート数
tweet_count = 2

# twitter.pyのツイート取得を実行しています。詳しくはtwitter_api.ipynbをご覧ください
tweet_search = TweetSearch(tweet_count)

AddTwitterInfo(tweet_search, session)