import subprocess
import time
from random import randint

class LoudSpeaker:
    """Class for controlling sound playback."""

    def __init__(self):
        """Initialize LoudSpeaker and play a beep sound."""
        self.play_beep()

    def play_log(self):
        """Play a random log sound."""
        rand_int = randint(1, 5)
        print(f"Playing sound: {rand_int}")
        subprocess.Popen(['aplay', f"/home/pi/Music/log{rand_int}.wav"])
        return rand_int

    def get_sleep_duration(self, log_number):
        """Get sleep duration based on log number.

        Args:
            log_number (int): The number of the log.

        Returns:
            int: The sleep duration in seconds.
        """
        # Define sleep durations based on log number
        sleep_duration_mapping = {
            1: 7,
            2: 9,
            3: 10,
            4: 9,
            5: 10
        }
        return sleep_duration_mapping.get(log_number, 7)  # Default to 7 seconds if log_number is not in mapping

    def play_camera(self, code):
        """Play a camera-related sound based on the code."""
        if code == 'MC101':
            subprocess.Popen(['aplay', "/home/pi/Music/camera_surr.wav"])
        elif code == 'MC202':
            subprocess.Popen(['aplay', "/home/pi/Music/camera_face.wav"])

    def play_alcohol(self):
        """Play an alcohol-related sound."""
        subprocess.Popen(['aplay', "/home/pi/Music/Alcohol .wav"])

    def play_beep(self):
        """Play a beep sound."""
        subprocess.Popen(['aplay', "/home/pi/Music/beep.wav"])

if __name__ == "__main__":
    speaker = LoudSpeaker()
    time.sleep(3)
    log = speaker.play_log()  # Example usage to play a log sound
    #speaker.play_alcohol()
