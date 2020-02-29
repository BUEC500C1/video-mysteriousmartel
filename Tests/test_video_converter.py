from video_converter import videoConvert

def test_video_converter():
  try:
    videoConvert("potato")
    test = True

  except:
    test = False

  assert test, 'Unable to convert images to video. Check file type before trying again.'

if __name__ == '__main__':
  test_video_converter()