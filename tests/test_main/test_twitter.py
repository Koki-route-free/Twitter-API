import sys
sys.path.append('../')
from conduct.main import twitter 
# 変数に値が代入できているかのかのテスト
def test_key():
  assert twitter.API_Key
  assert twitter.API_Sec
  assert twitter.Token
  assert twitter.Token_Sec
  assert twitter.Bearer_Token

# 代入されたトークンを使って変数を作成できているかのテスト
def test_variable():
  assert twitter.auth
  assert twitter.api
  assert twitter.tweets
  
# 全ての値が取得できているかのテスト  
def test_tweet():
  for tweet in twitter.tweets:
    assert tweet.id
    assert tweet.created_at
    assert tweet.text
    assert tweet.user.name
    assert tweet.user.screen_name 
#これらは空の値が返される可能性もあるのでテストから外します。
#user.friends_count（フォロー数）
#user.followers_count （フォロワー数）
#user.description（概要）
    
def test_authorization():    
    assert twitter.connect_to_twitter(twitter.Bearer_Token)  

def test_conduct():   
    assert twitter.make_request(twitter.headers)