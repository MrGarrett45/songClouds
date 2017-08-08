#! python3

import requests
from bs4 import BeautifulSoup
import re
import shelve
import sqlite3

conn = sqlite3.connect('artistDB.db')
table = conn.cursor()
table.execute('''CREATE TABLE IF NOT EXISTS artists (id integer primary key, name text, numSongs real, lyrics text) ''')
#conn.commit()
#conn.close()

base_url = "https://api.genius.com"
headers = {'Authorization': 'Bearer U6sHDfsAn3dAnrPFFwgxzB05A7-3kVK8pb2yNphCu37VVEeDXg1MIYlCTf0bRrfx'}

artist_name = input("Enter an artists name: ")

#removing brackets function by JF Sebastian stack overflow, needed to remove brackets such as [Verse 1 21 Savage]
def remove_text_inside_brackets(text, brackets="[]"):
    count = [0] * (len(brackets) // 2) # count open/close brackets
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b: # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close # `+1`: open, `-1`: close
                if count[kind] < 0: # unbalanced bracket
                    count[kind] = 0  # keep it
                else:  # found bracket to remove
                    break
        else: # character is not a [balanced] bracket
            if not any(count): # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars)

#function partly from "big-ish data blog", you give the method the API path to the song and it gives you lyrics
def lyrics_from_song_api_path(song_api_path):
  song_url = base_url + song_api_path
  response = requests.get(song_url, headers=headers)
  json = response.json()
  path = json["response"]["song"]["path"]
  page_url = "http://genius.com" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  [h.extract() for h in html('script')]
  lyrics = html.find("div", class_="lyrics").get_text()
  lyrics = repr(remove_text_inside_brackets(lyrics))
  lyrics = lyrics.replace('\\n', ' ')
  return lyrics

search_url = base_url + "/search"
data = {'q': artist_name}
response = requests.get(search_url, data=data, headers=headers)
json = response.json()
song_info = None
#print(json["response"]["hits"])
for hit in json["response"]["hits"]:
  if hit["result"]["primary_artist"]["name"] == artist_name:
    song_info = hit
    #print(song_info)
    break
if song_info:
  print("success")
  #print(artistId)
  #songLyrics = lyrics_from_song_api_path(song_api_path)
  #print(songLyrics)
  
  #From here trying to capture multiple songs 
  #lyricFile = open('lyrics.txt', 'a')
  shelveFile = shelve.open('lyricData')
  shelveFile['lyrcs'] = " "
  artistID = song_info["result"]["primary_artist"]["id"]
  print(artistID)
  looper = 1
  counter = 0
  fullLyrics = " "
  while True:
      artistUrl = base_url + "/artists/" + str(artistID) + "/songs?page="+str(looper)+"&per_page="+str(50)
      looper = looper + 1
      response = requests.get(artistUrl, headers=headers)
      json = response.json()
      print(len(json["response"]["songs"]))   #Fixing this stuff rn
      for song in json["response"]["songs"]:
          full_title = str(song["full_title"])
          if song["primary_artist"]["id"] == artistID and full_title.find("Ft.") == -1 and full_title.find("Remix") == -1:
              print(song["api_path"] +" "+ str(counter) + " "+song["title"])
              counter = counter + 1
              song_api_path = song["api_path"]
              #lyricFile.write(lyrics_from_song_api_path(song_api_path))
              fullLyrics += lyrics_from_song_api_path(song_api_path)

      print("next page " + str(json["response"]["next_page"]))
      if json["response"]["next_page"] == None:
          break

fullLyrics = fullLyrics.replace("  ", " ")
artistInfo = (artistID, artist_name, counter, fullLyrics)
table.execute('INSERT INTO artists VALUES (?,?,?,?)', artistInfo)
conn.commit()
conn.close()
shelveFile['lyrics'] = fullLyrics
#lyricFile.close()
shelveFile.close()
