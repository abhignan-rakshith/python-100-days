import geopy.distance

class GeofenceChecker:
    """Class for checking if a given location is within a specified geofence."""
    
    def __init__(self, center_lat, center_lon, radius):
        """Initialize GeofenceChecker with center coordinates and radius.

        Args:
            center_lat (float): Latitude of the geofence center.
            center_lon (float): Longitude of the geofence center.
            radius (float): Radius of the geofence in kilometers.
        """
        self.center_lat = center_lat
        self.center_lon = center_lon
        self.radius = radius
        self.center_point = geopy.Point(latitude=center_lat, longitude=center_lon)

    def convert_coords(self, lat_str, lon_str):
        """Convert latitude and longitude strings to float values.

        Args:
            lat_str (str): Latitude string.
            lon_str (str): Longitude string.

        Returns:
            tuple: Latitude and longitude as float values.
        """
        return float(lat_str), float(lon_str)

    def is_within_geofence(self, target_lat_str, target_lon_str):
        """Check if a target location is within the geofence.

        Args:
            target_lat_str (str): Latitude of the target location.
            target_lon_str (str): Longitude of the target location.

        Returns:
            bool: True if the target location is within the geofence, False otherwise.
        """
        target_lat, target_lon = self.convert_coords(target_lat_str, target_lon_str)   
        target_point = geopy.Point(latitude=target_lat, longitude=target_lon)

        distance = geopy.distance.distance(self.center_point, target_point).km

        # Check if within radius in both north-south and east-west directions
        north_south_ok = abs(target_lat - self.center_lat) <= self.radius
        east_west_ok = abs(target_lon - self.center_lon) <= self.radius

        return distance <= self.radius and north_south_ok and east_west_ok


if __name__ == "__main__":
    # Test GeofenceChecker
    my_fence = GeofenceChecker(12.9261, 77.5974, 0.094)
    print(my_fence.is_within_geofence(12.9261, 77.5974))

    