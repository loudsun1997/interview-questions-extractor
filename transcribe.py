import whisper
import argparse
import os
import sys
import threading
import time
from tqdm import tqdm

def transcribe_video(video_path, model_size="medium", output_format="txt"):
    """
    Transcribes a video file using OpenAI's Whisper model.
    """
    
    # 1. Check if file exists
    if not os.path.exists(video_path):
        print(f"Error: The file '{video_path}' was not found.")
        return

    print(f"Loading Whisper model ('{model_size}')...")
    
    # 2. Load the Whisper model
    try:
        model = whisper.load_model(model_size)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # 3. Transcribe with progress bar
    try:
        # Load audio to get duration for progress bar
        print("Loading audio...")
        audio = whisper.load_audio(video_path)
        audio_duration = len(audio) / whisper.audio.SAMPLE_RATE
        
        # Shared state for progress tracking
        transcription_done = threading.Event()
        result_holder = [None]
        error_holder = [None]
        
        def transcribe_thread():
            try:
                result_holder[0] = model.transcribe(
            video_path, 
                    fp16=False, 
                    language="en",
                    verbose=False
                )
            except Exception as e:
                error_holder[0] = e
            finally:
                transcription_done.set()
        
        # Start transcription in background thread
        thread = threading.Thread(target=transcribe_thread)
        thread.start()
        
        # Show progress bar while transcribing
        with tqdm(total=100, desc="Transcribing", unit="%",
                  bar_format="{l_bar}{bar}| {percentage:3.0f}% [{elapsed}<{remaining}]") as pbar:
            
            start_time = time.time()
            estimated_time = max(audio_duration / 10, 5)
            
            while not transcription_done.is_set():
                elapsed = time.time() - start_time
                progress = min(95, (elapsed / estimated_time) * 100)
                pbar.n = int(progress)
                pbar.refresh()
                time.sleep(0.1)
            
            pbar.n = 100
            pbar.refresh()
        
        thread.join()
        
        if error_holder[0]:
            raise error_holder[0]
        
        result = result_holder[0]
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
    parser = argparse.ArgumentParser(description="Transcribe video to English text using Whisper.")
    parser.add_argument("video_path", type=str, help="Path to the video file.")
    parser.add_argument("--model", type=str, default="medium", choices=["tiny", "base", "small", "medium", "large"], help="Model size (default: medium).")

    args = parser.parse_args()

    transcribe_video(args.video_path, model_size=args.model)
