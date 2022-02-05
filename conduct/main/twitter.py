#  まず初めにTwitterアカウントとTwitter developerアカウントの作成をしてください https://twitter.com/ja/using-twitter/create-twitter-account https://developer.twitter.com/en/portal どちらも終わりましたら、 developerアカウントでログインし、new projectを立ち上げてください すると自動的にAPI Key and Secret は自動的に生成され、その下にAuthentication Tokensが表示され最後にAccess Token and Secret が表示されます。またTwitter IDはhttps://tweeterid.com/ を利用するとすぐわかります。 これらをconfig.pyに記述してください。

# 最初にタイムラインの取得からおこないます
import tweepy
import requests
import json
import sys
sys.path.append('../')
from conduct.main import config

# config.pyから読み込み変数に代入しますさらにその変数を使ってAPIログインを行います
# 引数はツイートの引用数です  
def tweet_search(counts):    
    API_Key = config.API_KEY
    API_Sec = config.API_SECRET_KEY
    Token = config.ACCESS_TOKEN
    Token_Sec = config.ACCESS_TOKEN_SECRET
    auth = tweepy.OAuthHandler(API_Key, API_Sec)
    auth.set_access_token(Token, Token_Sec)
    api = tweepy.API(auth)

    tweets = api.home_timeline(count=counts)
    return tweets

# 取得してきたツイートはそれぞれidがふられているのでそれを使い表示させてみます。
def conduct_time_line(tweets):
    for tweet in tweets:
        print('='*20)
        print('ツイートID : '   , tweet.id)
        print('ツイート時間 : ' , tweet.created_at)
        print('ツイート本文 : ', tweet.text)
        print('ユーザ名 : ', tweet.user.name) 
        print('スクリーンネーム : ', tweet.user.screen_name) 
        print('フォロー数 : ', tweet.user.friends_count) 
        print('フォロワー数 : ', tweet.user.followers_count) 
        print('ユーザ概要 : ', tweet.user.description) 
        print('='*20)
  
#  実行コマンド
# 取得するツイート数
count = 5 
# tweet_search = tweet_search(count)
# conduct_time_line(tweet_search)
    



# 次に自分の投稿を取得します
# まずconfig.pyからインポートし変数に代入します
def bearer_token():
    Bearer_Token = config.BEARER_TOKEN
    return Bearer_Token


def connect_to_twitter(key):
    return {"Authorization": "Bearer {}".format(key)}

#検索実行

# 次にurlを取得するのですが今回は最後にresentを加えることで直近の投稿から取得されるようにします。 ここでオプションを色々付け加えられるのですが、今回は必要最低限のparamsの設定しか行っておりません。 また。jsonで見やすくします。
def make_request(headers):
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = "query=from:learningnao"
    return requests.request("GET", url, params=params, headers=headers).json()

# それぞれの関数をまとめて実行したものです
def conduct_tweet():
    Bearer_Token = bearer_token()
    headers = connect_to_twitter(Bearer_Token)
    response = make_request(headers)
    return response

# response = conduct_tweet()
# print(response)