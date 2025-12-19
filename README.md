# Video Transcription Tool

A simple Python tool to transcribe video/audio files to text using OpenAI's Whisper model.

## Prerequisites

### macOS (using Homebrew)

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and FFmpeg (required for audio processing)
brew install python ffmpeg
```

### Windows

1. **Install Python**
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, check ✅ "Add Python to PATH"

2. **Install FFmpeg**
   - Using Chocolatey (recommended):
     ```powershell
     choco install ffmpeg
     ```
   - Or using winget:
     ```powershell
     winget install ffmpeg
     ```
   - Or manually: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip ffmpeg
```

---

## Installation

1. **Clone or download this repository**

2. **Install Python dependencies**

```bash
pip install openai-whisper
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

---

## Usage

### Basic usage

```bash
python transcribe.py /path/to/your/video.mp4
```

### Choose a model size

```bash
python transcribe.py /path/to/your/video.mp4 --model base
```

| Model  | Size   | Speed    | Accuracy |
|--------|--------|----------|----------|
| tiny   | ~39 MB | Fastest  | Lower    |
| base   | ~74 MB | Fast     | Good     |
| small  | ~244 MB| Medium   | Better   |
| medium | ~769 MB| Slow     | High     |
| large  | ~1.5 GB| Slowest  | Highest  |

### Examples

```bash
# Transcribe with default base model
python transcribe.py interview.mp4

# Transcribe with higher accuracy (slower)
python transcribe.py interview.mp4 --model medium

# Transcribe an audio file
python transcribe.py podcast.mp3 --model small
```

---

## Output

The transcript is saved as `{filename}_transcript.txt` in the same directory as your input file.

```
Loading Whisper model ('base')...
Transcribing 'interview.mp4'...
100%|████████████████████████████████| 309239/309239 [08:07<00:00, 634.52frames/s]

--- Transcription Complete ---
Saved to: interview_transcript.txt

Preview:
Hello and welcome to today's interview...
```

---

## What to Do with the Transcript

Once you have the transcript, copy the text and paste it into **ChatGPT** with this prompt:

> Extract only technical interview questions from this script, summarize in simple sentences. List them in bullet points.

This will give you a clean, organized list of the key questions from your interview.

---

## Supported Formats

- **Video**: MP4, MKV, AVI, MOV, WebM
- **Audio**: MP3, WAV, M4A, FLAC, OGG

---

## Troubleshooting

### "ffmpeg not found"
Make sure FFmpeg is installed and in your system PATH. Restart your terminal after installation.

### Slow transcription
- Use a smaller model (`--model tiny` or `--model base`)
- If you have an NVIDIA GPU, install PyTorch with CUDA support for faster processing

### Memory errors
- Use a smaller model
- Close other applications to free up RAM

---

## Final Note

After running it for the first time, the whole process will only take **2 minutes of attention** — just run the command, wait for it to finish, and paste into ChatGPT!

---

## License

MIT

