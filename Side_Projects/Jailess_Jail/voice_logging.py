import pyaudio
from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account
import time

class SpeechRecognizer:
    """Class for recording and transcribing speech."""

    def __init__(self):
        """Initialize SpeechRecognizer with keywords and credentials path."""
        self.keywords = [
            "weather", "sunny", "warm", "crashed", "sandy", "shores", "rain",
            "blurring", "world", "city", "canvas", "lights", "sweet", "mango", "sunshine"
        ]
        self.credentials_path = "/home/pi/Documents/speechtotext-421814-63b62d9c539a.json"

    def record_audio(self, duration_sec):
        """Record audio for a given duration.

        Args:
            duration_sec (int): Duration of audio recording in seconds.

        Returns:
            bytes: Recorded audio data.
        """
        try:
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=16000,  # Reduced sample rate
                            input=True,
                            frames_per_buffer=1024)  # Smaller buffer size

            print("Recording audio...")

            frames = []
            for _ in range(0, int(16000 / 1024 * duration_sec)):  # Adjusted for new sample rate and duration
                data = stream.read(1024)
                frames.append(data)

            print("Finished recording.")

            stream.stop_stream()
            stream.close()
            p.terminate()

            return b''.join(frames)
        except Exception as e:
            print(f"Error occurred during audio recording: {e}")
            return None

    def record_and_transcribe(self, duration_sec):
        """Record audio, transcribe it, and check for keywords.

        Args:
            duration_sec (int): Duration of audio recording in seconds.

        Returns:
            tuple: Tuple containing generated text and found keywords.
        """
        try:
            start_time = time.time()  # Start performance counter
            audio_data = self.record_audio(duration_sec)
            generated_text, found_keywords = self.transcribe_audio(audio_data)
            end_time = time.time()  # End performance counter
            print("Time taken:", end_time - start_time, "seconds")  # Print time taken
            return generated_text, found_keywords
        except Exception as e:
            print(f"Error occurred during recording and transcription: {e}")
            return None, None

    def transcribe_audio(self, audio_data):
        """Transcribe audio data into text.

        Args:
            audio_data (bytes): Recorded audio data.

        Returns:
            tuple: Tuple containing transcribed text and found keywords.
        """
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_path,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )

            client = speech.SpeechClient(credentials=credentials)

            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,  # Adjusted sample rate
                language_code="en-US",
            )

            audio = speech.RecognitionAudio(content=audio_data)

            response = client.recognize(config=config, audio=audio)

            transcript_words = []  # List to store individual words
            for result in response.results:
                transcript_words.extend(result.alternatives[0].transcript.split())  # Split by spaces and extend list

            keys_found = self.check_keywords(transcript_words)  # Pass list of words
            return transcript_words, keys_found
        except Exception as e:
            print(f"Error occurred during transcription: {e}")
            return None, None

    def check_keywords(self, words):
        """Check for keywords in a list of words.

        Args:
            words (list): List of words to check for keywords.

        Returns:
            list: List of found keywords.
        """
        keywords_found = []
        for word in words:
            if word.lower() in self.keywords:  # Convert word to lowercase for case-insensitive matching
                keywords_found.append(word)
        return keywords_found


if __name__ == "__main__":
    speech_recognizer = SpeechRecognizer()
    duration_sec = 7

    # Record and transcribe audio
    generated_text, found_keywords = speech_recognizer.record_and_transcribe(duration_sec)

    if generated_text is not None:
        print("Generated text:", generated_text)
        if found_keywords:
            print("Found keywords:", found_keywords)
        else:
            print("No keywords found.")
    else:
        print("Recording and transcription failed.")
