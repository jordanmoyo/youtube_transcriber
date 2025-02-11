# # Whisper transcription logic and model wrapper
import os
import torch
import torchaudio
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
from dotenv import load_dotenv

load_dotenv()
whisper_model=os.getenv("MODEL_NAME", "openai/whisper-base")
class Transcriber:
    def __init__(self, model_name=whisper_model):
        model_cache_dir = os.getenv("MODEL_PATH", "../models")
        self.processor = AutoProcessor.from_pretrained(model_name, cache_dir=model_cache_dir)
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(model_name, cache_dir=model_cache_dir)

    def transcribe(self, audio_path, chunk_length_sec=30):
        """Yields transcription chunks with timestamps dynamically."""
        waveform, sample_rate = torchaudio.load(audio_path)

        # Convert stereo to mono
        if waveform.shape[0] > 1:
            waveform = torch.mean(waveform, dim=0, keepdim=True)

        # Resample if necessary
        target_sample_rate = int(os.getenv("TARGET_SAMPLE_RATE", 16000))
        if sample_rate != target_sample_rate:
            resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=target_sample_rate)
            waveform = resampler(waveform)

        # Chunk processing
        chunk_length_samples = chunk_length_sec * target_sample_rate
        num_samples = waveform.shape[1]

        for start in range(0, num_samples, chunk_length_samples):
            end = min(start + chunk_length_samples, num_samples)
            audio_chunk = waveform[:, start:end]

            inputs = self.processor(audio_chunk.squeeze(0), sampling_rate=target_sample_rate, return_tensors="pt")

            # Generate transcription
            with torch.no_grad():
                predicted_ids = self.model.generate(**inputs)

            transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

            # Convert start time to MM:SS format
            timestamp = f"[{start // target_sample_rate // 60:02}:{(start // target_sample_rate) % 60:02}]"

            # Yield transcript chunk with timestamp
            yield f"{timestamp} {transcription}"


# import os
# import torch
# import torchaudio
# from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
# from dotenv import load_dotenv

# load_dotenv()
# # torchaudio.set_audio_backend("ffmpeg")  

# class Transcriber:
#     def __init__(self, model_name=os.getenv("MODEL_NAME")):
#         model_cache_dir = os.getenv("MODEL_PATH")
#         self.processor = AutoProcessor.from_pretrained(model_name, cache_dir=model_cache_dir)
#         self.model = AutoModelForSpeechSeq2Seq.from_pretrained(model_name, cache_dir=model_cache_dir)

#     def transcribe(self, audio_path, chunk_length_sec=int(os.getenv("CHUNK_LENTTH_SECONDS", 10))):
#         # Load audio file
#         waveform, sample_rate = torchaudio.load(audio_path,)

#         # Convert stereo to mono
#         if waveform.shape[0] > 1:
#             waveform = torch.mean(waveform, dim=0, keepdim=True)

#         # Resample to 16kHz if necessary
#         target_sample_rate = int(os.getenv("TARGET_SAMPLE_RATE", 16000))
#         if sample_rate != target_sample_rate:
#             resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=target_sample_rate)
#             waveform = resampler(waveform)

#         # Convert seconds to samples
#         chunk_length_samples = chunk_length_sec * target_sample_rate
#         num_samples = waveform.shape[1]

#         transcription_output = []

#         # Process audio in chunks
#         for start in range(0, num_samples, chunk_length_samples):
#             end = min(start + chunk_length_samples, num_samples)
#             audio_chunk = waveform[:, start:end]
            
#             # Convert sample index to timestamp
#             start_time_sec = start / target_sample_rate  # Convert sample index to seconds
#             timestamp = f"{int(start_time_sec // 60):02}:{int(start_time_sec % 60):02}"  # Format as MM:SS


#             inputs = self.processor(audio_chunk.squeeze(0), sampling_rate=target_sample_rate, return_tensors="pt")

#             # Generate transcription
#             with torch.no_grad():
#                 predicted_ids = self.model.generate(**inputs)

#             # Decode output
#             transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
            
#             # Append timestamped transcription
#             transcription_output.append({"time": timestamp, "text": transcription})
#             # full_transcription.append(transcription)

#             # Print each portion immediately
#             print(f"[{timestamp}] : {transcription}")

#         # Return the full transcription as a single string
#         return transcription_output #" ".join(full_transcription)


