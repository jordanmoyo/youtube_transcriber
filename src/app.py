import os 
import streamlit as st
from media.youtube_audio import YouTubeAudio
from transcription.transcriber import Transcriber
from dotenv import load_dotenv
import time
import itertools

load_dotenv()

default_video_url = os.getenv("YOUTUBE_VIDEO_URL",None)

# ✅ Force Streamlit to use full width and remove extra padding
st.set_page_config(layout="wide") 

st.title("🎥 YouTube Video Transcriber")
# Create two columns
left_col, right_col = st.columns([4, 6]) 

# Left Column: YouTube Input and Video Player
with left_col:
    st.subheader("📌 Enter YouTube URL")
    youtube_url = st.text_input("Paste YouTube video link here:",value=default_video_url)

    # Check if a URL is provided
    if youtube_url:
        try:
            # Display the video
            st.video(youtube_url)    
        except Exception as e:
            st.error(f"Error loading video: {e}")

# Right Column: Transcription Box

with right_col:
    st.subheader("📝 Transcription")

    if youtube_url:
        try:
            # Get audio from YouTube video
            youtube_audio = YouTubeAudio(url=youtube_url)
            path = youtube_audio.download_audio()
            print(f"Downloaded audio: {path}")
            print(f"Transcribing audio...")

            # Placeholder for real-time updates
            transcript_box = st.empty()
            full_transcription = ""

            # Transcribe in chunks
            transcriber = Transcriber()
            for chunk in transcriber.transcribe(path):
                full_transcription += chunk + "\n"
                transcript_box.text_area(
                    label="Transcription Output",
                    value=full_transcription,
                    height=400,
                    disabled=True
                )
                time.sleep(0.5)  # Simulating real-time effect

            is_transcribing = False

        except Exception as e:
            st.error(f"Error Transcribing video: {e}")
    else:
        st.text_area(label="Transcription Output", value="", height=320, disabled=True)

