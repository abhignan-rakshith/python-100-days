import smbus
import time
import threading


class MPU6050Sensor:
    def __init__(self, bus_num=1, device_address=0x68):
        """
        Initialize the MPU6050 sensor object.

        Args:
            bus_num (int): The I2C bus number (default is 1 for Raspberry Pi).
            device_address (int): The I2C device address of the MPU6050 sensor.
        """
        self.bus = smbus.SMBus(bus_num)
        self.Device_Address = device_address

        # MPU6050 Registers
        self.PWR_MGMT_1 = 0x6B
        self.SMPLRT_DIV = 0x19
        self.CONFIG = 0x1A
        self.GYRO_CONFIG = 0x1B
        self.INT_ENABLE = 0x38
        self.ACCEL_XOUT_H = 0x3B
        self.ACCEL_YOUT_H = 0x3D
        self.ACCEL_ZOUT_H = 0x3F
        self.GYRO_XOUT_H = 0x43
        self.GYRO_YOUT_H = 0x45
        self.GYRO_ZOUT_H = 0x47

        # Initialize MPU6050 sensor
        self.MPU_Init()

        # Initialize shock detection thread
        self.shock_detected = False
        self.last_shock_time = None
        self.shock_threshold = 2  # Adjust based on sensitivity
        
        self.num_samples_shock = 10
        self.shock_thread = threading.Thread(target=self.detect_shock)
        self.shock_thread.daemon = True  # Set thread as daemon to run in the background
        self.shock_thread.start()

    def MPU_Init(self):
        """
        Initialize the MPU6050 sensor by configuring its registers.
        """
        self.bus.write_byte_data(self.Device_Address, self.SMPLRT_DIV, 7)  # Sample Rate
        self.bus.write_byte_data(self.Device_Address, self.PWR_MGMT_1, 1)  # Power Management
        self.bus.write_byte_data(self.Device_Address, self.CONFIG, 0)  # Configuration
        self.bus.write_byte_data(self.Device_Address, self.GYRO_CONFIG, 24)  # Gyro Configuration
        self.bus.write_byte_data(self.Device_Address, self.INT_ENABLE, 1)  # Interrupt Enable

    def read_raw_data(self, addr):
        """
        Read raw 16-bit data from the MPU6050 sensor.

        Args:
            addr (int): The register address to read from.

        Returns:
            int: The raw 16-bit sensor data.
        """
        high = self.bus.read_byte_data(self.Device_Address, addr)
        low = self.bus.read_byte_data(self.Device_Address, addr + 1)
        value = (high << 8) | low
        if value > 32768:
            value -= 65536
        return value

    def get_sensor_data(self, num_samples=10):
        """
        Get averaged sensor data over multiple readings.

        Args:
            num_samples (int): Number of samples to average.

        Returns:
            tuple: A tuple containing averaged accelerometer and gyroscope data.
        """
        accel_data = []
        gyro_data = []

        for _ in range(num_samples):
            acc_x = self.read_raw_data(self.ACCEL_XOUT_H)
            acc_y = self.read_raw_data(self.ACCEL_YOUT_H)
            acc_z = self.read_raw_data(self.ACCEL_ZOUT_H)
            gyro_x = self.read_raw_data(self.GYRO_XOUT_H)
            gyro_y = self.read_raw_data(self.GYRO_YOUT_H)
            gyro_z = self.read_raw_data(self.GYRO_ZOUT_H)

            # Collect raw sensor data
            accel_data.append((acc_x, acc_y, acc_z))
            gyro_data.append((gyro_x, gyro_y, gyro_z))
            time.sleep(0.01)  # Delay between readings

        # Calculate average sensor values
        accel_avg = [sum(axis) / num_samples for axis in zip(*accel_data)]
        gyro_avg = [sum(axis) / num_samples for axis in zip(*gyro_data)]
        return accel_avg, gyro_avg

    def get_average_accel_magnitude(self):
        """
        Calculate the average acceleration magnitude over multiple readings.

        Returns:
            float: The average acceleration magnitude in g units.
        """
        accel_sum = 0
        for _ in range(self.num_samples_shock):
            acc_x = self.read_raw_data(self.ACCEL_XOUT_H)
            acc_y = self.read_raw_data(self.ACCEL_YOUT_H)
            acc_z = self.read_raw_data(self.ACCEL_ZOUT_H)

            # Scale raw data to obtain acceleration in g units
            accel_x = acc_x / 16384.0
            accel_y = acc_y / 16384.0
            accel_z = acc_z / 16384.0

            # Calculate magnitude of acceleration vector
            accel_magnitude = (accel_x ** 2 + accel_y ** 2 + accel_z ** 2) ** 0.5
            accel_sum += accel_magnitude

            time.sleep(0.01)  # Delay between readings

        return accel_sum / self.num_samples_shock

    def detect_shock(self):
        """Continuously monitor for shocks and implement a reset timer."""
        shock_reset_timeout = 10  # Seconds

        while True:
            avg_accel_magnitude = self.get_average_accel_magnitude()

            # Check for shock and handle timer
            if avg_accel_magnitude > self.shock_threshold:
                self.shock_detected = True
                self.last_shock_time = time.time()
            elif self.shock_detected and self.last_shock_time is not None:
                time_since_shock = time.time() - self.last_shock_time
                if time_since_shock >= shock_reset_timeout:
                    self.shock_detected = False
                    self.last_shock_time = None
                    print("No shock detected for a while. Resetting shock state.")

            time.sleep(0.1)  # Adjust delay as needed

    def check_motion(self, accel_threshold=5, gyro_threshold=1, num_samples=10):
        """
        Check motion detection based on averaged sensor readings.

        Args:
            accel_threshold (float): Acceleration threshold for motion detection in g units.
            gyro_threshold (float): Gyroscope threshold for motion detection in degrees/second.
            num_samples (int): Number of samples to average.

        Returns:
            bool: True if motion is detected, False otherwise.
        """
        accel_avg, gyro_avg = self.get_sensor_data(num_samples)

        # Convert raw sensor data to physical units (g, degrees/second)
        Ax = accel_avg[0] / 16384.0
        Ay = accel_avg[1] / 16384.0
        Az = accel_avg[2] / 16384.0
        Gx = gyro_avg[0] / 131.0
        Gy = gyro_avg[1] / 131.0
        Gz = gyro_avg[2] / 131.0

        # Calculate magnitudes for easier comparison
        accel_magnitude = (Ax ** 2 + Ay ** 2 + Az ** 2) ** 0.5
        gyro_magnitude = (Gx ** 2 + Gy ** 2 + Gz ** 2) ** 0.5

        # Check if motion is detected
        motion_detected = accel_magnitude > accel_threshold or gyro_magnitude > gyro_threshold
        return motion_detected

    def is_shock_detected(self):
        """
        Check if a shock (large movement) is detected.

        Returns:
            bool: True if a shock is detected, False otherwise.
        """
        return self.shock_detected


if __name__ == "__main__":
    sensor = MPU6050Sensor()

    while True:
        motion_detected = sensor.check_motion()
        shock_detected = sensor.is_shock_detected()

        if motion_detected:
            print("Motion detected!")
        if shock_detected:
            print("Shock detected!")

        time.sleep(1)  