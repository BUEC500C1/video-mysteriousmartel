from queue import Queue
import threading

# The queue handles the inputs to the module, sending in
# threads to be processed asynchronously and leaving the user open
# to attend to other tasks

userQueue = Queue(maxsize = 4)

def twitterQueueUp(userHandle,cycleCount):
  handleCycles = [userHandle, cycleCount]
  userQueue.put_nowait(handleCycles)
  queueMove()

def queueMove():
  if userQueue.empty() is True:
    print('No handles in queue: ending process.')
    pass

  user = userQueue.get()

  print('Currently processing for ' + str(user[0]))

def twitterThread(userHandle, cycleCount):
  pass
  
if __name__ == "__main__":
    twitterQueueUp('potato',3)
    handleList = ['MBTA','qikipedia','dog_rates','IvePetThatDog','GameGrumps']
    cycleList = [2,3,4,3,2]
    for i in range(len(handleList)):
      x = threading.Thread(target=twitterThread, args=(handleList[i],cycleList[i],))
      x.start()