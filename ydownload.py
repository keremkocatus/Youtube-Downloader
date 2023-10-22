from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp 
import re

#Functions that takes an url and downloads what user want 
def dowload_mp3_playlist(url):
  playlist = Playlist(url)
  playlist.video_urls
  for url in playlist:
      YouTube(url).streams.filter(only_audio=True).first().download("./downloads/")
  folder = "./downloads/"
  for file in os.listdir(folder):
    if re.search('mp4', file):
      print("Converting : " + file)
      mp4_path = os.path.join(folder,file)
      mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
      new_file = mp.AudioFileClip(mp4_path)
      new_file.write_audiofile(mp3_path)
      os.remove(mp4_path)
  return 1

def dowload_mp3(url):
  YouTube(url).streams.filter(only_audio=True).first().download("./downloads/") 
  folder = "./downloads/"
  for file in os.listdir(folder):
    if re.search('mp4', file):
      print("Converting : " + file)
      mp4_path = os.path.join(folder,file)
      mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
      new_file = mp.AudioFileClip(mp4_path)
      new_file.write_audiofile(mp3_path)
      os.remove(mp4_path)
  return 1

def dowload_mp4(url):
  YouTube(url).streams.get_highest_resolution().download("./downloads/")
  return 1

def dowload_mp4_playlist(url):
  playlist = Playlist(url)
  playlist.video_urls
  for url in playlist:
    YouTube(url).streams.get_highest_resolution().download("./downloads/")
  return 1

