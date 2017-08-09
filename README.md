# songClouds

Take artists song lyrics via web scraping and turn them into word clouds

This program uses the Genius API as well as traditional webscraping to collect all the lyrics by a particular artist available on Genius and turns them into a word cloud that shows their most frequently used words. 

Much of the work of this program is done via the open source wordcloud library available here: https://github.com/amueller/word_cloud

My program makeCloud.py is basically just taken from one of the examples on that github page and repurposed. 

The program is as simple as running getSongLyric.py, entering whatever artist you want, waiting for it to collect data, then using a vast array of customization tools to decide how your final word cloud will look. The only problem with this program is that webscraping is SLOW and it takes about 1 second per song to find and store each song, so collecting data for popular artists with 200+ songs gets annoying.

This program allows you to customize everything from images, fonts, colors, etc easily from a command line interface. Also provides an easy framework for adding new fonts (assuming they are .ttf files).

The odds this doesn't violate Genius's TOS are dicy at best.

SHOTOUTS:
Thanks to the "big-ish" data blog for their blog post on effeciently scraping the Genius API.

Thanks to the guy who wrote this http://minimaxir.com/2016/05/wordclouds/ which got me started with really customizing the clouds.

And finally thanks again to the awesome wordcloud library.

# Program work flow
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/songCloudWF.png "WF")

# Database as of 8/9/2017
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/DBscreenshot.png "DB")

# Examples
Red Hot Chili Peppers:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/redHotChiliPeppers.png "Chili Peppers")

Linkin Park:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/linkinPark.png "Linkin Park")

MF Doom:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/MFDoom.png "Doom")

Kenney Chesney:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/kenneyChesney.png "Kenney Chesney")

Danny Brown:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/dannyBrown.png "Danny Brown")

Cage The Elephant:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/CageTheElephantNew.png "CtE")

MGMT:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/MGMT.png "MGMT")
