#! python3

from wordcloud import (WordCloud, get_single_color_func, ImageColorGenerator, STOPWORDS)
import matplotlib.pyplot as plt
import random, sqlite3, os
import numpy as np
from PIL import Image

from palettable.wesanderson import *
from palettable.colorbrewer.diverging import *
from palettable.colorbrewer.sequential import *
from palettable.colorbrewer.qualitative import *
from palettable.matplotlib import *
from palettable.mycarta import *
from palettable.tableau import *

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colorPalette = Moonrise2_4
    return tuple(colorPalette.colors[random.randint(0,len(colorPalette.colors)-1)])

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

def run(artist_name):
    conn = sqlite3.connect('artistDB.db')
    table = conn.cursor()
    table.execute("SELECT lyrics FROM artists WHERE name=?", (artist_name,))
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
    #stopwords.add("nigga")
    
    imagePath = input("Enter your the name of your image file: ")
    coloring = np.array(Image.open(imagePath))
    
    print("Your font options are listed below: ")
    for filenames in os.walk('C:\\Users\\gmclaughlin\\Fonts'):
        for filename in filenames:
            if filename != '':
                print(filename)

    font = input("Enter the name of your font, or default for DroidSanaMono: ")
    #font_path = "/home/gmclaughlin/Python/Fonts/%s" % font   #linux
    font_path = "C:\\Users\\gmclaughlin\\Fonts\\%s" % font    #windows

    # Since the text is small collocations are turned off and text is lower-cased
    background_color = input("Enter a background color: ")
    print("Generating cloud now...")
    if font == 'default':
        wc = WordCloud(stopwords = stopwords, collocations=False, background_color=background_color, max_words=2000,mask=coloring)
    else:
        wc = WordCloud(font_path=font_path,stopwords = stopwords, collocations=False, background_color=background_color, max_words=3000,mask=coloring)

    wc.generate(text.lower())

    color_to_words = {
        # words below will be colored with a red single color function
        'red': ['test'],
    }
    # will be colored with a grey single color function
    default_color = 'red'

    #Multiple options for coloring here. Think its best to use a palette coloring system unless you want to only do one color in which case use SimpleGrouped
    chooseColoring = input("Enter what kind of image coloring you want. Select from image_colors, grouped_color_func, simple_color_func, or palette: ")
    if chooseColoring == 'image_colors':
        image_colors = ImageColorGenerator(coloring)
        wc.recolor(color_func=image_colors)

    if chooseColoring == 'grouped_color_func':
        default_color = input("Enter a color: ")
        grouped_color_func = GroupedColorFunc(color_to_words,default_color)
        wc.recolor(color_func=grouped_color_func)

    if chooseColoring == 'simple_color_func':
        default_color = input("Enter a color: ")
        simple_color_func = SimpleGroupedColorFunc(color_to_words, default_color)
        wc.recolor(color_func=simple_color_func)

    if chooseColoring == 'palette':
        wc.recolor(color_func=color_func)

    # Plot
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
