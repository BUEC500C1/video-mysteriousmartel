from tweet_queue import main
from word_cloud_generator import cloudGenerate
from video_converter import videoConvert
import pathlib
import json

def test_tweet_queue():
  try:
    keyFile = pathlib.Path("keys.key")
    if keyFile.exists():
      Handles = ['MBTA','qikipedia','dog_rates','IvePetThatDog','GameGrumps','IBM']
      Cycles = [2,3,4,3,2,3]
      main(Handles,Cycles)
      test = True
    else:
      with open('twitterVideoConverterTest.json', 'r') as read_file:
        twitterData = json.load(read_file)

      tweetList = [sub['text'] for sub in twitterData]
      cloudGenerate(tweetList,'tester','date to date',1)
      videoConvert('tester')
      test = True

  except:
    test = False

  assert test, 'Module test failed. Check individual tests for issues.'

if __name__ == '__main__':
  test_tweet_queue()