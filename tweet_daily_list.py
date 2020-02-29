import tweepy
import configparser
from datetime import datetime, date

''' This part of the module creates text lists of
    each cycle's tweets to be sent for image processing '''

def tweetCall(userHandle):
  config = configparser.ConfigParser()
  config.read('keys')
  auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),
    config.get('auth', 'consumer_secret').strip())
  auth.set_access_token(config.get('auth', 'access_token').strip(),
    config.get('auth', 'access_secret').strip())
  api = tweepy.API(auth)

  tweets = api.user_timeline(screen_name = userHandle, count = 30, include_rts = False)
  tweetList = []

  startTime = tweets[0].created_at.strftime("%m%d%Y")
  startDate = datetime.strptime(startTime, "%m%d%Y").date()
  startDateStr = str(startDate)

  endTime = tweets[-1].created_at.strftime("%m%d%Y")
  endDate = datetime.strptime(endTime, "%m%d%Y").date()
  endDateStr = str(endDate)

  dates = startDateStr + " to " + endDateStr

  for status in tweets:
    tweetList.append(status.text)
  return tweetList, dates
