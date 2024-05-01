import wireless

class WIFI:
    """Class for managing Wi-Fi connection."""

    def __init__(self):
        """Initialize WIFI object."""
        self.wifi = wireless.Wireless('wlan0')

    def is_connected_to_wifi(self):
        """Check if the device is connected to a Wi-Fi network.

        Returns:
            bool: True if connected, False otherwise.
        """
        current_network = self.wifi.current()
        return bool(current_network)

if __name__ == "__main__":
    my_wifi = WIFI()
    print(my_wifi.is_connected_to_wifi())
