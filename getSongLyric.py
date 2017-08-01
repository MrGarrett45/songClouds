#! python3

import requests
from bs4 import BeautifulSoup
import re

base_url = "https://api.genius.com"
headers = {'Authorization': 'Bearer U6sHDfsAn3dAnrPFFwgxzB05A7-3kVK8pb2yNphCu37VVEeDXg1MIYlCTf0bRrfx'}

song_title = "Bank Account"
artist_name = "21 Savage"

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

#function mostly from "big-ish data blog", you give the method the API path to the song and it gives you lyrics
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
data = {'q': song_title}
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
  artistID = song_info["result"]["primary_artist"]["id"]
  looper = 1
  while True:
      artistUrl = base_url + "/artists/" + str(artistID) + "/songs?page="+str(looper)+"&per_page="+str(50)
      looper = looper + 1
      response = requests.get(artistUrl, headers=headers)
      json = response.json()
      print(len(json["response"]["songs"]))   #Fixing this stuff rn
      counter = 0
      for song in json["response"]["songs"]:
          print(song["api_path"] +" "+ str(counter))
          counter = counter + 1
          song_api_path = song["api_path"]
          #print(lyrics_from_song_api_path(song_api_path))
          
      endLyrics = lyrics_from_song_api_path(song_api_path)
      print(endLyrics)
      if len(json["response"]["songs"]) < 50:
          break
