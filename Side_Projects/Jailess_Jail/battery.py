import psutil

def get_battery_percentage():
    """Get the current battery percentage.

    Returns:
        int: Battery percentage if available, otherwise 100%.
    """
    battery = psutil.sensors_battery()
    if battery:
        return battery.percent
    else:
        # Return 100% if battery information is not available (e.g., when powered by a wall adapter)
        return 100

if __name__ == "__main__":
    # Test get_battery_percentage function
    battery_percentage = get_battery_percentage()
    print("Battery percentage:", battery_percentage)
