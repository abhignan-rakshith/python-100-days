import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_mlx90614


class ADS1115Sensor:
    """Class for interfacing with ADS1115 ADC for analog sensors."""

    def __init__(self):
        """Initialize ADS1115Sensor."""
        # Initialize I2C bus
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Initialize ADS1115 ADC
        self.ads = ADS.ADS1115(self.i2c)

        # Initialize analog input for channel 1 (Pulse sensor)
        self.pulse_sensor = AnalogIn(self.ads, ADS.P0)

        # Initialize analog input for channel 2 (Alcohol sensor)
        self.alcohol_sensor = AnalogIn(self.ads, ADS.P1)

    def read_average_value(self, channel, num_readings=5):
        """Read average ADC value from the specified channel.

        Args:
            channel: Analog input channel object.
            num_readings (int): Number of readings to average.

        Returns:
            float: Average ADC value.
        """
        sum_values = 0
        for _ in range(num_readings):
            sum_values += channel.value
            time.sleep(0.05)  # Delay between readings to stabilize the sensor
        average_value = sum_values / num_readings
        return average_value

    def read_alcohol_concentration(self):
        """Read alcohol concentration from the alcohol sensor.

        Returns:
            float: Alcohol concentration.
        """
        average_value = self.read_average_value(self.alcohol_sensor)
        #print(average_value)
        return average_value

    def check_pulse(self):
        """Check if pulse is detected using the pulse sensor.

        Returns:
            bool: True if pulse is detected, False otherwise.
        """
        average_value = self.read_average_value(self.pulse_sensor)
        pulse_threshold = 21000  # Adjust threshold as needed
        pulse_detected = average_value > pulse_threshold
        return pulse_detected


class MLX90614:
    """Class for interfacing with MLX90614 temperature sensor."""

    def __init__(self, num_readings=5):
        """Initialize MLX90614 sensor.

        Args:
            num_readings (int): Number of readings to average.
        """
        # Initialize I2C communication
        self.i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        # Initialize the sensor
        self.mlx = adafruit_mlx90614.MLX90614(self.i2c)
        # Number of readings to average
        self.num_readings = num_readings

    def get_ambient_temperature(self):
        """Get the ambient temperature.

        Returns:
            float: Ambient temperature.
        """
        readings = []
        for _ in range(self.num_readings):
            readings.append(self.mlx.ambient_temperature)
            time.sleep(0.1)  # Optional: Add a short delay between readings
        return sum(readings) / self.num_readings

    def get_object_temperature(self):
        """Get the object temperature.

        Returns:
            float: Object temperature.
        """
        readings = []
        for _ in range(self.num_readings):
            readings.append(self.mlx.object_temperature)
            time.sleep(0.1)  # Optional: Add a short delay between readings
        return sum(readings) / self.num_readings


if __name__ == "__main__":
    # Test ADS1115Sensor
    ads_sensor = ADS1115Sensor()
    alcohol_value = ads_sensor.read_alcohol_concentration()
    pulse_detected = ads_sensor.check_pulse()
    print("Alcohol Concentration:", alcohol_value)
    print("Pulse Detected:", pulse_detected)

    # Test MLX90614
    mlx_sensor = MLX90614()
    ambient_temp = mlx_sensor.get_ambient_temperature()
    object_temp = mlx_sensor.get_object_temperature()
    print("Ambient Temperature:", ambient_temp)
    print("Object Temperature:", object_temp)
