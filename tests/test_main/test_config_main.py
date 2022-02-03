import sys
sys.path.append('../')
from conduct.main import config as CM    
# 値が代入されているかの確認です    
def test_config():
  assert CM.API_KEY
  assert CM.API_SECRET_KEY
  assert CM.ACCESS_TOKEN
  assert CM.ACCESS_TOKEN_SECRET
  assert CM.BEARER_TOKEN
  assert CM.TWITTER_ID