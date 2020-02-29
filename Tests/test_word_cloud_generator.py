from word_cloud_generator import cloudGenerate

def test_word_cloud_generator():
  try:
    potato = ['How many potatoes in a fish with tomato paste?', 'How many potatoes in a fish with tomato paste?',\
     'How many potatoes in a fish with tomato paste?', 'Alright it’s official, after 9months @trihex has officially \
      shipped me his 3DS + capture card, the MM3D playthrough is finally going to happen. Thanks for sending it out \
      brother lmao ily', 'The drop you have been waiting for. Shoutout to @Newegg for making it happen. #CLG10 \
      #IntelNUC #winwithNUC']
    cloudGenerate(potato,'potato','12/12/20-12/17/20',0)
    test = True

  except:
    test = False

  assert test, 'Unable to generate an image with test tweets, or due to missing information'

if __name__ == '__main__':
  test_word_cloud_generator()