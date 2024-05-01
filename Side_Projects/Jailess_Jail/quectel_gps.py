import serial
import time

class GPSDataHandler:
    """Class for handling GPS data."""
    
    def __init__(self, port='/dev/ttyUSB0', baud=115200):
        """Initialize GPSDataHandler.

        Args:
            port (str, optional): The serial port for GPS communication. Defaults to '/dev/ttyUSB0'.
            baud (int, optional): The baud rate for GPS communication. Defaults to 115200.
        """
        self.port = port
        self.baud = baud
        self.ser = serial.Serial(self.port, self.baud, timeout=1)
        
    def setup_gps(self):
        """Setup GPS module."""
        # Send initial AT Commands for setup
        print(self._send_at_command('AT'))
        print(self._send_at_command('AT+QGPS=1'))
        print(self._send_at_command('AT+QGPSCFG="nmeasrc",1'))

    def get_gps_data(self):
        """Get GPS data."""
        response = self._send_at_command('AT+QGPSGNMEA="GGA"')
        received_data = str(response)

        if len(received_data) >= 91:
            GNGGA_buffer = received_data.split("$GNGGA,", 1)[1]  # store data coming after “$GPGGA,” string
            NMEA_buff = (GNGGA_buffer.split(','))
            nmea_latitude = NMEA_buff[1]  # extract latitude from GPGGA string
            nmea_longitude = NMEA_buff[3]  # extract longitude from GPGGA string

            lat = float(nmea_latitude)
            lat = self._convert_to_degrees(lat)
            longi = float(nmea_longitude)
            longi = self._convert_to_degrees(longi)
            print("NMEA Latitude:", lat, "NMEA Longitude:", longi)
            return lat, longi

        else:
            # Return None if GPS data is not available
            return None, None

    def _send_at_command(self, command):
        """Send an AT command to the GPS module.

        Args:
            command (str): AT command to send.

        Returns:
            str: Response from the GPS module.
        """
        self.ser.write((command + '\r').encode())  # Send the command with a newline
        time.sleep(1)  # Short delay to allow processing
        ATResponse = self.ser.read_all().decode()  # Read the response
        return ATResponse

    def _convert_to_degrees(self, raw_value):
        """Convert latitude and longitude values from GPS module to degrees format.

        Args:
            raw_value (float): Latitude or longitude value from GPS module.

        Returns:
            float: Latitude or longitude value in degrees format.
        """
        decimal_value = raw_value / 100.00
        degrees = int(decimal_value)
        mm_mmmm = (decimal_value - int(decimal_value)) / 0.6
        position = degrees + mm_mmmm
        position = "%.4f" % position
        return position

if __name__ == "__main__":
    # Test GPSDataHandler
    my_gps = GPSDataHandler()
    my_gps.setup_gps()
    while True:
        print(my_gps.get_gps_data())
