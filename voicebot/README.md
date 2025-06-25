# Real-Time English Conversation Bot

This directory contains a sample Python script that demonstrates a very simple real-time conversation bot. It performs the following steps:

1. **Speech recognition** using your microphone.
2. **Text generation** by sending the recognized text to an API compatible with the Lambda included in this repository.
3. **Speech synthesis** of the generated reply using `pyttsx3`.

## Requirements

The script depends on a few Python packages. Install them via `pip`:

```bash
pip install -r requirements.txt
```

For Linux users, the `pyaudio` package may require additional system libraries such as `portaudio`.

## Usage

1. Start the script:

```bash
python voicebot.py
```

2. Speak into your microphone. The recognized text is sent to the API at `CHAT_API_ENDPOINT` (defaults to `http://localhost:8000/chat`). You can change this endpoint by setting the environment variable before running the script:

```bash
CHAT_API_ENDPOINT=https://example.com/chat python voicebot.py
```

3. The bot replies with synthesized speech. Press `Ctrl+C` to exit.

## Docker

A simple Dockerfile is provided. Build and run the container with:

```bash
docker build -t voicebot .
docker run --rm -e CHAT_API_ENDPOINT=https://example.com/chat --device /dev/snd voicebot
```

The container requires access to your audio devices; the exact `--device` options may vary by platform.

This is only a minimal prototype. You can swap the API endpoint with any text generation service and replace `pyttsx3` with a higher quality TTS library for more natural speech output.
