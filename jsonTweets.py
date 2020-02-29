import tweepy
import json
import configparser

config = configparser.ConfigParser()
config.read('keys')
auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),
  config.get('auth', 'consumer_secret').strip())
auth.set_access_token(config.get('auth', 'access_token').strip(),
  config.get('auth', 'access_secret').strip())
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

tweets1 = api.user_timeline(screen_name = 'IBM', count = 30, include_rts = False)

jsonSetup = json.dumps(tweets1, indent = 4)

with open("twitterVideoConverterTest.json","w") as outfile:
  outfile.write(jsonSetup)