from queue import Queue
import threading
from word_cloud_generator import cloudGenerate
from tweet_daily_list import tweetCall, maxIDsearch
from video_converter import videoConvert

# The queue handles the inputs to the module, sending in
# threads to be processed asynchronously and leaving the user open
# to attend to other tasks

userQueue = Queue(maxsize = 4)

def twitterQueueUp(userHandle,cycleCount):
  handleCycles = [userHandle, cycleCount]
  userQueue.put(handleCycles)
  queueMove()

def queueMove():
  if userQueue.empty() is True:
    print('No handles in queue: ending process.')
    pass

  # user contains both the user handle and the cycle count
  user = userQueue.get()

  print('Currently processing for ' + str(user[0]))
  maxID = maxIDsearch(user[0])

  # Messages notify the user of the module of remaining images
  # being processed, as well as when each handle's video is finished
  for i in range(user[1]):
    cycle = user[1] - i
    print(str(user[0]) + ' has ' + str(cycle) + ' cycle(s) remaining\n')
    tweets, dates, maxID = tweetCall(user[0], maxID)
    cloudGenerate(tweets,user[0],dates,i)
    if (i == user[1]):
      print(str(user[0]) + ' has generated all images')

  videoConvert(user[0])
  print(str(user[0]) + ' has a video ready to view')

def main(handles, cycles):
  handleList = handles
  cycleList = cycles
  threadList = []
  for i in range(len(handleList)):
    fiber = threading.Thread(target=twitterQueueUp, args=(handleList[i],cycleList[i],))
    threadList.append(fiber)
    fiber.start()

  for fiber in threadList:
    fiber.join()
  
if __name__ == "__main__":
  practiceHandles = ['MBTA','qikipedia','dog_rates','IvePetThatDog','GameGrumps','IBM']
  practiceCycles = [2,3,4,3,2,3]
  main(practiceHandles,practiceCycles)
