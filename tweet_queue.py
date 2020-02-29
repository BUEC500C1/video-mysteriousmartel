from queue import Queue
import threading
import time

userQueue = Queue(maxsize = 4)

def twitterQueueUp(userHandle):
  queueMove()

  if not userQueue.full():
    userQueue.put_nowait(userHandle)
    print(userQueue)

def queueMove():
  return 'hi'

if __name__ == '__main__':
  twitterQueueUp('potato')