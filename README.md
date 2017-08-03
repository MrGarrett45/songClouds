# songClouds

Take artists song lyrics via web scraping and turn them into song clouds

This program uses the Genius API as well as traditional webscraping to collect all the lyrics by a particular artist available on Genius and turns them into a word cloud that shows their most frequently used words. 

Much of the work of this program is done via the open source wordcloud library available here: https://github.com/amueller/word_cloud

My program make_word_cloud is basically just taken from one of the examples on that github page and altered a bit.

The program is as simple as running getSongLyric.py, entering whatever artist you want, waiting for it to collect data, then running the make word cloud program. The only problem with this program is that webscraping is SLOW and it takes about 1 second per song to find and store each song, so collecting data for popular artists with 200+ songs gets annoying.

The odds this doesn't violate Genius's TOS are dicy at best.

Finally thanks to the "big-ish" data blog for their blog post on effeciently scraping the Genius API.

# Examples
Red Hot Chili Peppers:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/redHotChiliPeppers.png "Chili Peppers")

Kendrick Lamar:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/kendrickLamar.png "Kendrick Lamar")

Kenney Chesney:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/kenneyChesney.png "Kenney Chesney")

Chance The Rapper:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/chanceTheRapper.png "Chance The Rapper")

MGMT:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/MGMT.png "MGMT")

Wiz Khalifa:
![alt text](https://github.com/MrGarrett45/songClouds/blob/master/wizKhalifa.png "Wiz Khalifa")
