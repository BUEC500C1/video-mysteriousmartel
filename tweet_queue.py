from queue import Queue
import threading

# The queue handles the inputs to the module, sending in
# threads to be processed asynchronously and leaving the user open
# to attend to other tasks

userQueue = Queue(maxsize = 10)

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

def twitterThread(userHandle):
  pass
  
if __name__ == "__main__":
    twitterQueueUp('potato',3)
    # x = threading.Thread(target=twitterThread, args=("potato",))
    # x.start()