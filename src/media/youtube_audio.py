import yt_dlp
from pydub import AudioSegment
import os
from dotenv import load_dotenv

load_dotenv()

class YouTubeAudio:
    def __init__(self, url):
        self.url = url
        self.audio_path_mp3 = "./media_cache/downloaded_audio"  # Temp MP3 file
        # self.audio_path_wav = "./media_cache/downloaded_audio.wav"  # Final WAV file

    def download_audio(self):
        """Download audio from a YouTube video in the best available format."""
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': self.audio_path_mp3,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Download as MP3 first
                'preferredquality': '192'
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
        
        print(f"Audio downloaded as MP3: {self.audio_path_mp3}")
        return f'{self.audio_path_mp3}.mp3' #self.convert_to_wav()

    def convert_to_wav(self): # This method is not used in the final code
        """Convert MP3 to WAV format."""
        audio = AudioSegment.from_mp3(self.audio_path_mp3)
        audio.export(self.audio_path_wav,  format="wav")
        print(f"Converted to WAV: {self.audio_path_wav}")
        return self.audio_path_wav  # Return the final WAV file

