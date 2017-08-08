#! python3

from wordcloud import (WordCloud, get_single_color_func, ImageColorGenerator, STOPWORDS)
import matplotlib.pyplot as plt
import random, sqlite3
import numpy as np
from PIL import Image
import palettable.colorbrewer.sequential

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(RdPu_9.colors[random.randint(2,8)])

class SimpleGroupedColorFunc(object):
    """Create a color function object which assigns EXACT colors
       to certain words based on the color to words mapping
       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.
       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)


class GroupedColorFunc(object):
    """Create a color function object which assigns DIFFERENT SHADES of
       specified colors to certain words based on the color to words mapping.
       Uses wordcloud.get_single_color_func
       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.
       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        """Returns a single_color_func associated with the word"""
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

conn = sqlite3.connect('artistDB.db')
table = conn.cursor()
table.execute("SELECT lyrics FROM artists WHERE name=?", ("Lil Pump",))
lyrics = table.fetchone()
conn.commit()
conn.close()

text = lyrics[0]
#text = shelveFile['lyrics']
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
stopwords.add("ll")
stopwords.add("nigga")

coloring = np.array(Image.open("manyColors.jpg"))

# Since the text is small collocations are turned off and text is lower-cased
wc = WordCloud(stopwords = stopwords, collocations=False, background_color="white", max_words=2000,mask=coloring)
wc.generate(text.lower())



color_to_words = {
    # words below will be colored with a green single color function
    'red': ['beautiful', 'explicit', 'simple', 'sparse',
                'readability', 'rules', 'practicality',
                'explicitly', 'one', 'now', 'easy', 'obvious', 'better'],
    # will be colored with a red single color function
    #'red': ['ugly', 'implicit', 'complex', 'complicated', 'nested',
    #        'dense', 'special', 'errors', 'silently', 'ambiguity',
    #        'guess', 'hard']
}
# will be colored with a grey single color function
default_color = 'red'
image_colors = ImageColorGenerator(coloring)
grouped_color_func = GroupedColorFunc(color_to_words,default_color)

#Multiple options for coloring here. Think its best to use a palette coloring system unless you want to only do one color in which case use SimpleGrouped
wc.recolor(color_func=image_colors)
#wc.recolor(color_func=grouped_color_func)
#wc.recolor(color_func=color_func)  #for palette colors
# Plot
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
