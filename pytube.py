import streamlit as st
from pytube import YouTube


url = st.text_input("Enter the YouTube video URL:")


try:
   video = YouTube(url)
   stream = video.streams.filter(only_audio=True).first()
   stream.download(filename=f"{video.title}.mp3")
   st.write("The video is downloaded in MP3")
except KeyError:
   st.write("Unable to fetch video information. Please check the video URL or your network connection.")