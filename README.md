# songClouds

Take artists song lyrics via web scraping and turn them into word clouds

This program uses the Genius API as well as traditional webscraping to collect all the lyrics by a particular artist available on Genius and turns them into a word cloud that shows their most frequently used words. 

Much of the work of this program is done via the open source wordcloud library available here: https://github.com/amueller/word_cloud

My program make_word_cloud is basically just taken from one of the examples on that github page and altered a bit.

The program is as simple as running getSongLyric.py, entering whatever artist you want, waiting for it to collect data, then running the makeCloud program. The only problem with this program is that webscraping is SLOW and it takes about 1 second per song to find and store each song, so collecting data for popular artists with 200+ songs gets annoying.

The odds this doesn't violate Genius's TOS are dicy at best.

Finally thanks to the "big-ish" data blog for their blog post on effeciently scraping the Genius API.

# Examples
Red Hot Chili Peppers:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/redHotChiliPeppers.png "Chili Peppers")

MF Doom:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/MFDoom.png "Doom")

Kenney Chesney:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/kenneyChesney.png "Kenney Chesney")

Danny Brown:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/dannyBrown.png "Danny Brown")

MGMT:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/MGMT.png "MGMT")

Tame Impala:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/examplePics/tameImpala.png "Tame Impala")
