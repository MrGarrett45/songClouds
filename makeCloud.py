from wordcloud import (WordCloud, get_single_color_func, ImageColorGenerator, STOPWORDS)
import matplotlib.pyplot as plt
import shelve
import numpy as np
from PIL import Image
import random
from palettable.colorbrewer.sequential import Reds_9

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Reds_9.colors[random.randint(2,8)])

shelveFile = shelve.open('lyricData')

text = shelveFile['lyrics']
text.replace("\\'", "")
text.replace("\\\\'", "")

stopwords = set(STOPWORDS)
stopwords.add("xa0")
stopwords.add("ctr")
stopwords.add("zl")
stopwords.add("don")
stopwords.add("llc")
stopwords.add("bmi")
stopwords.add("ain")
stopwords.add("nigga")

coloring = np.array(Image.open("MFDoomFace.jpg"))

# Since the text is small collocations are turned off and text is lower-cased
wc = WordCloud(stopwords = stopwords, collocations=False, background_color="white", max_words=2000,mask=coloring)
wc.generate(text.lower())

# will be colored with a grey single color function
default_color = 'grey'
image_colors = ImageColorGenerator(coloring)


wc.recolor(color_func=image_colors)
wc.recolor(color_func=color_func)
# Plot
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
