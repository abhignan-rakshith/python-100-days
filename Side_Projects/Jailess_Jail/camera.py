import subprocess


def capture_image(filename="/home/pi/Pictures/thingspeak.jpg"):
    """Capture an image using libcamera-still.

    Args:
        filename (str, optional): The file path to save the captured image. Defaults to "/home/pi/Pictures/thingspeak.jpg".
    """
    try:
        # Run libcamera-still command to capture an image
        result = subprocess.run(["libcamera-still", "-o", filename], check=True)
    except subprocess.CalledProcessError as e:
        # Handle error if image capture fails
        print(f"Image capture failed: {e}")
        exit(1)  # Exit with an error code


if __name__ == "__main__":
    # Test capture_image function
    capture_image()
