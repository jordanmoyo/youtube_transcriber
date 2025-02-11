# Abstract base class for media
from abc import ABC, abstractmethod

class MediaStream(ABC):
    @abstractmethod
    def start_stream(self):
        pass

    @abstractmethod
    def stop_stream(self):
        pass

    @abstractmethod
    def extract_audio(self):
        pass

   
    