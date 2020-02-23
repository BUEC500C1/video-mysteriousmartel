import tweepy
from datetime import datetime, date

''' This part of the module creates text lists of
    each day's tweets and files them in separate
    text documents '''

def tweetCall(userHandle):
  consumer_key = '***'
  consumer_secret = '***'
  access_token = '***'
  access_token_secret = '***'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
  auth.set_access_token(access_token, access_token_secret)   
  api = tweepy.API(auth)

  tweets = api.user_timeline(screen_name = userHandle, count = 20, include_rts = False)
  tweetList = []

  currentDay = date.today()

  for status in tweets:
    dateString = status.created_at.strftime("%m%d%Y")
    dateVal = datetime.strptime(dateString, "%m%d%Y").date()
    if dateVal == currentDay:
      tweetList.append(status.text)
    print(dateVal)

  print(currentDay)

  return tweetList

# if __name__ == '__main__':
  # print(tweetCall('username'))
