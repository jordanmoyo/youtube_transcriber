import os
import sys
# Get the absolute path to the "src" folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from transcription.transcriber import Transcriber
from IPython.display import Audio
from IPython.display import display

from IPython.display import Audio

class NotebookDisplay:
    def __init__(self, transcriber: Transcriber, audio_path:str):
        self.audio_path = audio_path
        self.transcriber = transcriber
        
    def display_in_notebook(self):
        transcribed_text = self.transcriber.transcribe(self.audio_path)
        display(Audio(self.audio_path))
        print(transcribed_text)