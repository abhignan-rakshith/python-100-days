import requests
import random
import serial
import time
import os

class DataSender:
    """Class for sending data to ThingSpeak."""
    
    def __init__(self, use_wifi=True):
        """Initialize DataSender.

        Args:
            use_wifi (bool, optional): Whether to use WiFi for data transmission. Defaults to True.
        """
        self.use_wifi = use_wifi
        self.api_key = "LLTIMB9UJ8FI64X1"  # ThingSpeak API key
        self.modem_port = "/dev/ttyUSB0"  # this is based on your modem port
        self.baud_rate = 115200
        self.ser = serial.Serial(self.modem_port, self.baud_rate, timeout=1)

    def send_to_thingspeak_via_wifi(self, values):
        """Send data to ThingSpeak via WiFi.

        Args:
            values (list): List of data values to send.
        """
        print(values)
        url = f"https://api.thingspeak.com/update?api_key={self.api_key}&"
        url += "&".join([f"field{i+1}={value}" for i, value in enumerate(values)])
        response = requests.get(url)
        if response.status_code == 200:
            print("Data sent to ThingSpeak via WiFi successfully.")
        else:
            print(f"Failed to send data via WiFi: {response.status_code}")

    def send_to_thingspeak_via_modem(self, values):
        """Send data to ThingSpeak via modem.

        Args:
            values (list): List of data values to send.
        """
        print(values)
        def send_at_command(cmd, wait_for_response=True):
            self.ser.write((cmd + '\r\n').encode())
            time.sleep(0.6)  # Short delay for command processing
            if wait_for_response:
                response = self.ser.read_until(b'OK\r\n').decode().strip()  # Read until 'OK'
                print(response)
                return response

        if send_at_command("AT") != "OK":
            print("Modem not responding. Check connections.")
            return

        # Configure and activate GPRS connection
        # Add your configuration commands here

        # Establish connection to ThingSpeak
        send_at_command("AT+QIOPEN=1,0,\"TCP\",\"api.thingspeak.com\",80,0,1")
        send_at_command("AT+QISTATE=1,0")

        # Prepare HTTP request
        data = "{{\"api_key\":\"{}\"".format(self.api_key)
        for i, value in enumerate(values):
            data += f",\"field{i+1}\":{value}"
        data += "}"

        headers = [
            "POST /update.json HTTP/1.1",
            "Host: api.thingspeak.com",
            "Content-Type: application/json",
            f"Content-Length: {len(data)}\n",  # Enforce an empty line
        ]

        # Send HTTP request
        send_at_command("AT+QISEND=0")
        for header in headers:
            send_at_command(header)
        send_at_command(data)
        send_at_command(chr(26), wait_for_response=False)  # Send Ctrl+Z
        response = self.ser.read_until()  # Read any response immediately after Ctrl+Z
        print("Response from ThingSpeak:", response)

        # Close connection
        send_at_command("AT+QICLOSE=0")
        send_at_command("AT+QIDEACT=0")

        print("Data sent to ThingSpeak via modem successfully.")

    def send_random_data(self):
        """Send random data to ThingSpeak."""
        if self.use_wifi:
            values = [random.randint(1, 200) for _ in range(8)]
            self.send_to_thingspeak_via_wifi(values)
        else:
            values = [random.randint(0, 20) for _ in range(8)]
            self.send_to_thingspeak_via_modem(values)
    
    def send_real_data(self, list_values):
        """Send real data to ThingSpeak.

        Args:
            list_values (list): List of real data values to send.
        """
        if self.use_wifi:
            self.send_to_thingspeak_via_wifi(list_values)
        else:
            self.send_to_thingspeak_via_modem(list_values)

    def delete_channel_data(self):
        """Delete data from ThingSpeak channel."""
        ChannelID = 2510167  # Replace with your actual Channel ID
        UserAPIKey = 'DX3PMVGC8YIZSV5K'  # Replace with your ThingSpeak User API Key
        url = f'https://api.thingspeak.com/channels/{ChannelID}/feeds.json?api_key={UserAPIKey}'
        response = requests.delete(url)
        if response.status_code == 200:
            print("Data deleted successfully.")
        else:
            print(f"Deletion failed. Error code: {response.status_code}")

class ImageSender:
    """Class for sending images to ThingSpeak."""
    
    def __init__(self, filename="/home/pi/Pictures/thingspeak.jpg"):
        """Initialize ImageSender with filename.

        Args:
            filename (str, optional): Path to the image file. Defaults to "/home/pi/Pictures/thingspeak.jpg".
        """
        self.thingspeakImageChannelID = 'a5bb040578'
        self.thingSpeakImageChannelAPIKey = 'LCNF5KZNOJ935ETT'
        self.localFileName = filename
        self.thingSpeakURL = 'https://data.thingspeak.com/channels/' + self.thingspeakImageChannelID + '/images'
    
    def readImageBytes(self, local_file_path):
        """Read image bytes from a local file.

        Args:
            local_file_path (str): Path to the local image file.

        Returns:
            bytes: Image bytes.
        """
        with open(local_file_path, 'rb') as file:
            image_bytes = file.read()
        return image_bytes

    def send_image(self):
        """Send image to ThingSpeak."""
        # Read image bytes from local file
        imData = self.readImageBytes(self.localFileName)
        # POST image to ThingSpeak if there is a valid image
        if imData:
            x = requests.post(url=self.thingSpeakURL, data=imData,
                              headers={'Content-Type': 'image/jpeg',
                                       'thingspeak-image-channel-api-key': self.thingSpeakImageChannelAPIKey,
                                       'Content-Length': str(os.path.getsize(self.localFileName))})
            print(x)

if __name__ == "__main__":
    # Test DataSender
    sender = DataSender(use_wifi=False)
#     sender.delete_channel_data()
#     sender.send_random_data()
#     Uncomment the line below to test sending real data
    sender.send_real_data([10, 20, 30, 40, 50, 60, 70, 80])
    
    # Test ImageSender
#     image_sender = ImageSender()
#     image_sender.send_image()

