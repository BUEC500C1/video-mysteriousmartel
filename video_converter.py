import os
import ffmpeg
import glob

''' Converts all collected tweet images to video '''

def videoConvert(userHandle):
  if not os.path.isdir(userHandle + '_Video'):
    os.mkdir(userHandle + '_Video')

  videoPath = userHandle + '_Video/'
  imagePath = os.getcwd() + '/' + userHandle + '_DailyTweets/'
  inputImage = imagePath + '*.png'
  tweetVid = videoPath + userHandle + '_tweetVid.mp4'
  out, err = (ffmpeg
    .input(inputImage, pattern_type='glob',framerate=0.2)
    .filter('fps', fps=1)
    .output(tweetVid).run()
    )
  return out
