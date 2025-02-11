📂 whisper_streaming_project/
│── 📂 src/                      # Source code
│    │── 📂 media/               # Media handling (video & audio)
│    │    │── __init__.py        
│    │    │── media_stream.py    # Abstract base class for media
│    │    │── video_stream.py    # Handles video input
│    │    │── audio_stream.py    # Handles audio input
│    │
│    │── 📂 transcription/       # Whisper transcription logic
│    │    │── __init__.py
│    │    │── transcriber.py     # Whisper model wrapper
│    │
│    │── 📂 display/             # UI and display logic
│    │    │── __init__.py
│    │    │── display_manager.py # Handles displaying transcriptions
│    │
│    │── 📂 utils/               # Utility functions (optional)
│    │    │── __init__.py
│    │    │── audio_utils.py     # Audio preprocessing utils
│    │    │── video_utils.py     # Video-related utils
│    │
│    │── main.py                 # Main script to run the app
│
│── 📂 data/                      # Store sample audio/video files
│    │── sample_audio.wav
│    │── sample_video.mp4
│
│── 📂 models/                    # Store downloaded models
│
│── 📂 notebooks/                 # Jupyter notebooks for testing
│
│── 📂 tests/                     # Unit tests
│    │── test_transcriber.py
│    │── test_media_stream.py
│
│── .env                          # Environment variables (if needed)
│── requirements.txt               # Dependencies
│── Dockerfile                     # Containerization
│── docker-compose.yml             # Docker setup
│── README.md                      # Project documentation
