import sys
sys.path.append('../')
from conduct.main import twitter 
# 変数に値が代入できているかのかのテスト
def test_tweet_search():
  assert twitter.tweet_search()

  
# 全ての値が取得できているかのテスト  
def test_tweet():
  for tweet in twitter.tweet_search():
    assert tweet.id
    assert tweet.created_at
    assert tweet.text
    assert tweet.user.name
    assert tweet.user.screen_name 
#これらは空の値が返される可能性もあるのでテストから外します。
#user.friends_count（フォロー数）
#user.followers_count （フォロワー数）
#user.description（概要）
    
def test_bearer_token():
  assert twitter.bearer_token()
  
def test_conduct_tweet():
  assert twitter.conduct_tweet()  