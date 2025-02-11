# Use an official Python 3.12 runtime as a parent image
FROM python:3.12-slim
# FROM --platform=linux/arm64 python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Update package lists and install PortAudio
RUN apt update && apt install -y portaudio19-dev && apt install -y libgl1 && apt-get install -y ffmpeg

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
# conda install -c conda-forge libstdcxx-ng

# Expose Streamlit’s default port
EXPOSE 8501

# Define environment variable
# ENV NAME World

# Command to run the Streamlit app
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
