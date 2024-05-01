import serial
import time

msg_codes = {
    "MC101": "Point camera to surrounding",
    "MC202": "Point camera to face",
    "MC303": "Get GPS and Geofence data",
    "MC404": "Get all sensor data",
}

class SMSHandler:
    """Class for handling SMS communication."""

    def __init__(self, port='/dev/ttyUSB0', baud=115200):
        """Initialize SMSHandler.

        Args:
            port (str, optional): The serial port for SMS communication. Defaults to '/dev/ttyUSB0'.
            baud (int, optional): The baud rate for SMS communication. Defaults to 115200.
        """
        self.port = port
        self.baud = baud
        self.ser = serial.Serial(self.port, self.baud, timeout=1)
        self.send_sms(message="Starting SMS service...")

    def _send_at_command(self, command):
        """Send an AT command to the GSM module.

        Args:
            command (str): AT command to send.

        Returns:
            str: Response from the GSM module.
        """
        self.ser.write((command + '\r').encode())  # Send the command with a newline
        time.sleep(1)  # Short delay to allow processing
        response = self.ser.read(self.ser.in_waiting).decode()  # Read the response
        return response

    def read_latest_sms(self):
        """Read the latest SMS.

        Returns:
            tuple: A tuple containing the SMS message and its code.
        """
        # Set SMS format to text mode (AT+CMGF=1)
        print(self._send_at_command("AT+CMGF=1"))

        # Read the SMS @ index 0 using AT+CMGR=0 to get the latest SMS
        message_code = self._send_at_command("AT+CMGR=0")

        if "+CMGR:" in message_code:
            # Split the response into lines to extract SMS content
            response_lines = message_code.splitlines()
            sms_code = response_lines[2].upper()

            if sms_code in msg_codes:
                return msg_codes[sms_code], sms_code
            else:
                return "Invalid SMS Code", sms_code

        return None

    def send_sms(self, message, recipient="9008032021"):
        """Send an SMS.

        Args:
            message (str): The message to send.
            recipient (str, optional): The phone number of the recipient. Defaults to "9008032021".
        """
        # Set SMS format to text mode
        response = self._send_at_command('AT+CMGF=1')

        # Set character set to GSM
        response = self._send_at_command('AT+CSCS="GSM"')

        # Send SMS to the recipient number
        response = self._send_at_command(f'AT+CMGS="{recipient}"')
        self.ser.write(str.encode(message))

        # Send Ctrl+Z to indicate end of message
        self.ser.write(chr(26).encode('utf-8'))
        print(response)

    def delete_all_sms(self):
        """Delete all SMS messages."""
        return self._send_at_command("AT+CMGD=1,4")  # Delete all SMS

# Example usage
if __name__ == "__main__":
    sms_handler = SMSHandler()
#     sms_handler.send_sms(message="Finalizing the project soon")  # To send a message
    # Read and process the latest SMS
    sms_data = sms_handler.read_latest_sms()
    if sms_data:
        message, content = sms_data
        print("Received SMS:", message, "-", content)
        if message == "Invalid SMS Code":
            print("Invalid SMS Code Received:", content)
    else:
        print("Buffer Empty...")
    sms_handler.delete_all_sms()
