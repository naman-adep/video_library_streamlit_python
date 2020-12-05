

#Import package
import streamlit as st

#Title
st.title("Video Library")

#Videos
video_file = open("video1.mp4","rb").read()
st.video(video_file)

video_file = open("video2.mp4","rb").read()
st.video(video_file)

video_file = open("video3.mp4","rb").read()
st.video(video_file)


