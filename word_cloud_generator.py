import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

'''For the image generation, a word cloud is made for each
   tweet per day'''

def cloudGenerate(fileName):

  # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
  directory = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

  # Read the whole text
  text = open(path.join(directory, fileName)).read()

  # Generate a word cloud image
  wordcloud = WordCloud().generate(text)

  # Display the generated image:
  # the matplotlib way:
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.show()
  wordcloud.to_file('lines_read.png')

# if __name__ == "__main__":
#   cloudGenerate('constitution.txt')