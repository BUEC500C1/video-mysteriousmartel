import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

'''For the image generation, a word cloud is made for each
   tweet per day'''

def cloudGenerate(statusList,userHandle,dateRange,indexCount):

  if not os.path.isdir(userHandle + '_DailyTweets'):
    os.mkdir(userHandle + '_DailyTweets')

  tweetPath = os.getcwd() + '/' + userHandle + '_DailyTweets/'

  text = ' '.join([str(tweet) for tweet in statusList])

  # Generate a word cloud image
  wordcloud = WordCloud().generate(text)

  imageName = tweetPath + "tweet" + str(indexCount) + ".png"

  wordcloud.to_file(imageName)

  # Write dates of the tweet cloud in top corner of image

  # NOTE: you will need the arial.ttf font in the directory
  # where you are running this file (available in repo)

  image = Image.open(imageName)
  write = ImageDraw.Draw(image)

  font = ImageFont.truetype('arial.ttf', size=15)
  (x,y) = (10,10)
  date = dateRange
  fontcolor = 'rgb(255,255,255)'
  write.text((x,y),date,fill=fontcolor,font=font)

  image.save(imageName)

  