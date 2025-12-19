# Video Transcription Tool

A simple Python tool to transcribe video/audio files to text using OpenAI Whisper.

## Prerequisites

### macOS

```bash
brew install python ffmpeg
```

### Windows

1. Install Python from python.org (check "Add Python to PATH")
2. Install FFmpeg:
   ```powershell
   choco install ffmpeg
   ```

### Linux

```bash
sudo apt install python3 python3-pip ffmpeg
```

## Installation

```bash
pip install openai-whisper tqdm
```

Or:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python transcribe.py /path/to/video.mp4
```

### Model Options

Default is **medium** (recommended for accuracy).

| Model  | Size    | Speed   | Accuracy            |
|--------|---------|---------|---------------------|
| tiny   | 39 MB   | Fastest | Lower               |
| base   | 74 MB   | Fast    | Good                |
| small  | 244 MB  | Medium  | Better              |
| medium | 769 MB  | Slow    | High (default)      |
| large  | 1.5 GB  | Slowest | Highest             |

To use a different model:

```bash
python transcribe.py video.mp4 --model large
```

## Output

Transcript saves as `filename_transcript.txt` in the same folder.

## What to Do with the Transcript

Copy the transcript and paste into ChatGPT with this prompt:

```
Extract only technical interview questions from this script, summarize in simple sentences. List them in bullet points.
```

## Supported Formats

- Video: MP4, MKV, AVI, MOV, WebM
- Audio: MP3, WAV, M4A, FLAC, OGG

## Troubleshooting

- ffmpeg not found: Make sure FFmpeg is installed and restart terminal
- Slow: Use smaller model (--model tiny)
- Memory errors: Use smaller model, close other apps

## Final Note

After the first setup, the whole process takes only 2 minutes of attention - run the command, wait, paste into ChatGPT!

## License

MIT


