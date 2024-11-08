# Get the tools we need
from transformers import pipeline
import librosa
import numpy as np
import warnings
warnings.filterwarnings('ignore')  # Hide warning messages

class AudioProcessor:
    """
    This class turns speech from audio files into text.
    """
    
    def __init__(self):
        """
        Start the program. Get ready to read audio files.
        """
        # Load the tool that turns speech into text
        self.speech_recognizer = pipeline(
            "automatic-speech-recognition",
            model="facebook/wav2vec2-base-960h"
        )
    
    def load_audio(self, file_path):
        """
        Open an audio file and get it ready.
        
        Input: 
            file_path = where your audio file is saved
            
        Output:
            audio data that the program can read
        """
        try:
            # Open the file and make it ready for the program
            audio_data, sample_rate = librosa.load(
                file_path, 
                sr=16000  # Make sure audio quality is good
            )
            return audio_data, sample_rate
        except Exception as e:
            print(f"Cannot open audio file: {str(e)}")
            return None, None
    
    def transcribe_audio(self, file_path):
        """
        Change the speech in your audio file to text.
        
        Input:
            file_path = where your audio file is saved
            
        Output:
            text from the audio file
        """
        # Step 1: Open the audio file
        audio_data, sample_rate = self.load_audio(file_path)
        
        if audio_data is None:
            return ""
            
        try:
            # Step 2: Turn speech into text
            result = self.speech_recognizer(
                {"raw": audio_data, "sampling_rate": sample_rate}
            )
            return result["text"]
        except Exception as e:
            print(f"Error making text: {str(e)}")
            return ""

def main():
    """
    Main program that shows how to use this tool.
    """
    # Start the program
    processor = AudioProcessor()
    
    try:
        # Ask user for their audio file
        audio_file = input("Type the location of your audio file (WAV or MP3): ")
        print("Reading your file...")
        
        # Get the text from the audio
        text_result = processor.transcribe_audio(audio_file)
        
        # Show what was found in the audio
        if text_result:
            print("\nHere is what the audio said:")
            print(text_result)
        else:
            print("\nNo words found in the audio.")
            
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
    except Exception as e:
        print(f"\nSomething went wrong: {str(e)}")

# Start the program if you run this file
if __name__ == "__main__":
    main()
