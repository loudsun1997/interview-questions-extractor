import whisper
import argparse
import os
import warnings

# Filter out FP16 warnings but keep tqdm progress bar
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

def transcribe_video(video_path, model_size="base", output_format="txt"):
    """
    Transcribes a video file using OpenAI's Whisper model.
    """
    
    # 1. Check if file exists
    if not os.path.exists(video_path):
        print(f"Error: The file '{video_path}' was not found.")
        return

    print(f"Loading Whisper model ('{model_size}')...")
    
    # 2. Load the Whisper model
    # Available models: tiny, base, small, medium, large
    try:
        model = whisper.load_model(model_size)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    print(f"Transcribing '{video_path}'...")

    # 3. Transcribe
    # task="transcribe" will transcribe the audio in its original language.
    # task="translate" will transcribe AND translate non-English audio into English.
    
    try:
        # verbose=True shows Whisper's built-in progress bar (tqdm)
        result = model.transcribe(video_path, fp16=False, language="en", verbose=True)
        text = result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return

    # 4. Save to file
    base_name = os.path.splitext(video_path)[0]
    output_filename = f"{base_name}_transcript.{output_format}"

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(text.strip())

    print(f"\n--- Transcription Complete ---")
    print(f"Saved to: {output_filename}")
    
    # Optional: Print preview
    print("\nPreview:")
    print(text[:200] + "..." if len(text) > 200 else text)

if __name__ == "__main__":
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Transcribe video to English text using Whisper.")
    parser.add_argument("video_path", type=str, help="Path to the video file.")
    parser.add_argument("--model", type=str, default="base", choices=["tiny", "base", "small", "medium", "large"], help="Model size (default: base).")

    args = parser.parse_args()

    transcribe_video(args.video_path, model_size=args.model)
