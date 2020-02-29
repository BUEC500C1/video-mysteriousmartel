from tweet_daily_list import tweetCall, maxIDsearch
import pathlib

def test_tweet_daily_list():
  try:
    keyFile = pathlib.Path("keys")
    if keyFile.exists():
      handle = 'qikipedia'
      initID = maxIDsearch(handle)
      tweetCall(handle,initID)
      test = True
    else:
      print('Keys are not available. Please use the JSON test file for remaining tests')
      test = True

  except:
    test = False

  assert test, 'Unable to collect tweets for test handle'

if __name__ == '__main__':
  test_tweet_daily_list()