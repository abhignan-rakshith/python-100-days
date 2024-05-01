import time
import threading
import subprocess
import psutil
from lcd import LCD
from WiFi import WIFI
from sms import SMSHandler
from serial.serialutil import SerialException
from alarm import Alarm
from quectel_gps import GPSDataHandler
from geofencing import GeofenceChecker
from speaker import LoudSpeaker
from mpu6050 import MPU6050Sensor
from ads1115 import ADS1115Sensor, MLX90614 
from IoT import DataSender, ImageSender
from voice_logging import SpeechRecognizer


# Objects Initialization
gps_handler = GPSDataHandler()
geo_fence = GeofenceChecker(12.9261, 77.5974, 0.094)
my_lcd = LCD()
my_wifi = WIFI()
my_alarm = Alarm()
my_sms = SMSHandler()
my_speaker = LoudSpeaker()
my_mpu6050 = MPU6050Sensor()
my_adc = ADS1115Sensor()
my_temp = MLX90614()
my_ts_image = ImageSender()
my_voice = SpeechRecognizer()

time.sleep(3)

# Global Variables
alcohol_first_run = True
alcohol_concentration = None
alcohol_measurement_interval = 1 * 60  # 15 minutes in seconds
last_alcohol_measurement_time = time.monotonic()
voice_logging_first_run = True
voice_logging_timer = 0
voice_logging_interval = 1 * 60  # 3 minutes in seconds
my_ts_data = None
wifi_connected = False


def scroll_lcd_left(message, content):
    """
    Scrolls the message on the LCD display from right to left.

    Args:
      message: The short message to display at the beginning (str).
      content: The longer content to be scrolled (str).
    """
    # Code for scrolling the message on LCD
    my_lcd.clear_lcd()
    str_pad = " " * 16
    my_long_string = str_pad + message
    my_lcd.display_lcd(f"{content}", 2, 6)
    for i in range (0, len(my_long_string)):
        lcd_text = my_long_string[i:(i+16)]
        my_lcd.display_lcd(lcd_text,1)
        time.sleep(0.06)
        my_lcd.display_lcd(str_pad,1)


# Code for camera
def capture_image(filename="/home/pi/Pictures/thingspeak.jpg"):
    """Captures an image using libcamera-still and handles errors."""
    try:
        result = subprocess.run(["libcamera-still", "-o", filename], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Image capture failed: {e}")
        exit(1)  # Exit with an error code


def measure_alcohol():
    """
    Measures the alcohol concentration using the ADC sensor and displays it on the LCD.
    Also activates the alarm if the concentration exceeds a threshold.
    """
    global alcohol_concentration 
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Checking Alcohol", 1)
    my_lcd.display_lcd("Please Wait...", 2, 1)
    
    # Play sound indicating alcohol measurement
    my_speaker.play_alcohol()
    time.sleep(9)  # Wait for sound to finish playing

    # Read alcohol concentration from ADC
    alcohol_concentration = my_adc.read_alcohol_concentration() # thingspeak variable
    print(f"Alcohol Concentration: {alcohol_concentration}")

    # Update LCD display with alcohol concentration
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Alcohol level", 1, 2)
    my_lcd.display_lcd(f"{alcohol_concentration}", 2, 5)

    # Check if alcohol concentration exceeds threshold and activate alarm if necessary
    if alcohol_concentration > 15000:
        my_lcd.clear_lcd()
        my_lcd.display_lcd("High Alcohol", 1, 2)
        my_lcd.display_lcd("Concentration!!!", 2)
        my_alarm.activate_alarm(5)  # Activate alarm for 5 seconds
        
        
def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery:
        return battery.percent
    else:
    # Return 100% if battery information is not available (e.g., when powered by a wall adapter)
        return 100
        

def wifi_setup():
    """
    Establishes a Wi-Fi connection and initializes the DataSender object accordingly.

    Sets global variables:
    my_ts_data: The DataSender object for sending data to Thingspeak.
    wifi_connected: A boolean indicating whether Wi-Fi is connected.
    """
    global my_ts_data
    global wifi_connected
    ######################## WiFi code #######################
    connection = my_wifi.is_connected_to_wifi()
    if not connection:
        my_lcd.clear_lcd()
        my_lcd.display_lcd("WiFi not", 1, 5)
        my_lcd.display_lcd("Connected", 2, 4)
        my_alarm.activate_alarm()
        my_ts_data = DataSender(use_wifi=False)
        #raise Exception("WiFi not connected to RPI, please connect and try again.")
    else:
        my_lcd.clear_lcd()
        my_lcd.display_lcd("WiFi is", 1, 5)
        my_lcd.display_lcd("Connected", 2, 4)
        wifi_connected = True
        my_alarm.signal_ok(2)
        my_ts_data = DataSender(use_wifi=True)

    #my_ts_data.delete_channel_data() # Deleting channel data at init
    time.sleep(1)
    my_alarm.signal_ok(3)


def modem_auto_answer():
    """
    Sets the modem to automatically answer incoming calls after 2 rings.
    """
    ######################## Calling Setup Code #######################
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Setting MODEM", 1, 2)
    my_lcd.display_lcd("for auto answer", 2)

    print(gps_handler._send_at_command('ATS0=1')) # Auto answer after 2 rings
    print(gps_handler._send_at_command('AT+QAUDMOD=2')) # Audio mode set to handset
    print(gps_handler._send_at_command('AT+CLVL=3')) # Volume set to 3

    my_alarm.signal_ok(3)

    
#measure_alcohol() #Initial Alcohol Reading
time.sleep(2)
my_lcd.clear_lcd()
my_lcd.display_lcd("System starting!", 1)
my_lcd.display_lcd("Please Wait...", 2, 1)
time.sleep(2)

######################## MAIN CODE #######################
def main():
    """
    The main program loop that executes various functionalities like:
    - Reading SMS
    - Geo-fencing
    - Camera capture (based on SMS code)
    - Motion detection
    - Pulse and alcohol sensor readings
    - Temperature sensor readings
    - Battery level check
    - Uploading data to Thingspeak
    - Voice logging
    """
    global voice_logging_first_run
    global alcohol_first_run
    global last_alcohol_measurement_time
    global alcohol_measurement_interval
    global voice_logging_timer
    global voice_logging_interval


    ######################## Reading SMS code #######################
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Checking for SMS", 1)
    my_lcd.display_lcd("Please Wait...", 2, 1)
    time.sleep(2)

    latest_sms = ""
    sms_data = my_sms.read_latest_sms()
    if sms_data:
        message, content = sms_data
        print("Received SMS:", message, "-", content)

        if message == "Invalid SMS Code":
            print("Invalid SMS Code Received:", content)
            my_alarm.activate_alarm()
            my_lcd.clear_lcd()
            my_lcd.display_lcd("Invalid SMS", 1, 3)
            my_lcd.display_lcd("Code Received.", 2, 2)
        else:
            latest_sms = content # latest_sms variable is important to do some functions later on
            lcd_scroll_thread = threading.Thread(target=scroll_lcd_left, args=[message, latest_sms])
            lcd_scroll_thread.start()
            lcd_scroll_thread.join()
        my_sms.delete_all_sms()

    else:
        print("There is no SMS in buffer.")
        my_lcd.clear_lcd()
        my_lcd.display_lcd("There is no SMS", 1)
        my_lcd.display_lcd("in the buffer.", 2, 1)
        my_alarm.activate_alarm(1)
        time.sleep(1)

    my_alarm.signal_ok(3)

    ######################## GEO-Fencing code #######################
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Trying to get", 1, 2)
    my_lcd.display_lcd("GPS data...", 2, 4)

    try:
        gps_handler.setup_gps()

        gps_data_found = False
        gps_counter = 0
        while not gps_data_found:
            lat, longi = gps_handler.get_gps_data() # thingspeak variables
            if lat is not None and longi is not None:
                my_lcd.clear_lcd()
                my_lcd.display_lcd(f"{lat},{longi}", 1)
                # Geo-fencing code
                fence = 0
                if geo_fence.is_within_geofence(lat, longi):
                    print("Device is within the geofence.\n")
                    my_lcd.display_lcd("  Inside Fence", 2)
                    fence = 1 # thingspeak variable
                else:
                    print("Device is outside the geofence.\n")
                    my_lcd.display_lcd("  Outside Fence", 2)
                    my_alarm.activate_alarm(5)
                current_time = time.strftime("%H:%M:%S")
                print(f"Time: {current_time}\n")  # Display time
                # Check if latest_sms variable is MC303
                if latest_sms == 'MC303':
                    my_sms.send_sms(message=f"Lat: {lat}, Long: {longi},\nFence: {fence}, Time: {current_time}")
                print("-------------------------------------------------------")
                gps_data_found=True
                time.sleep(1)
            else:
                gps_counter += 1
                if gps_counter == 6:
                    print("Unable to get GPS data...\n Try again after moving the device close to window.")
                    my_lcd.clear_lcd()
                    my_lcd.display_lcd("Unable to find", 1, 1)
                    my_lcd.display_lcd("GPS, change pos", 2)
                    my_alarm.activate_alarm()
                    raise SystemExit

                print("QUECTEL Error: No GPS data found!")
                my_lcd.clear_lcd()
                my_lcd.display_lcd("  NO GPS DATA!  ", 1)
                my_lcd.display_lcd("waiting 15 sec..", 2)
                time.sleep(15)

    except SerialException:
        print("Fault with modem!")
        my_lcd.clear_lcd()
        my_lcd.display_lcd("Fault with modem!", 1)
        my_alarm.activate_alarm()
        raise SystemExit


    my_alarm.signal_ok(3)
    time.sleep(2)


    ######################## Camera_Code_Setup #######################
    camera_on = True
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Camera Capture", 1, 2)
    my_lcd.display_lcd("if code matches", 2, 1)
    if latest_sms == 'MC101':
        print("Point Camera to Surrounding")
        my_speaker.play_camera(latest_sms)
        capture_image()
        my_speaker.play_beep()
    elif latest_sms == 'MC202':
        print("Point Camera to Face")
        my_speaker.play_camera(latest_sms)
        capture_image()
        my_speaker.play_beep()
    else:
        camera_on = False
        print("No Valid Camera Code Found....")
        my_lcd.clear_lcd()
        my_lcd.display_lcd("No Valid Camera", 1)
        my_lcd.display_lcd("Code Found!", 2, 3)
        my_alarm.activate_alarm(1)

    my_alarm.signal_ok(3)


    ######################## Motion Detection code #######################
    is_moving = 0 # thingspeak variable

    my_lcd.clear_lcd()
    my_lcd.display_lcd("Detecting Motion", 1)
    my_lcd.display_lcd("Please Stand-By", 2, 1)
    print("Reading Data of Gyroscope and Accelerometer")
    time.sleep(2)

    # while True:
    #     motion_detected = my_mpu6050.check_motion()
    # 
    #     if my_mpu6050.is_shock_detected():
    #         print("Shock Detected! Alerting...")
    #         my_lcd.clear_lcd()
    #         my_lcd.display_lcd("Shock Detected", 1, 2)
    #         my_alarm.activate_alarm(2)
    #             
    #     # Checking for motion
    #     if motion_detected:
    #         print("Motion Detected!")
    #         my_lcd.clear_lcd()
    #         my_lcd.display_lcd("Motion Detected!", 1)
    #     else:
    #         print("Stationary")
    #         my_lcd.clear_lcd()
    #         my_lcd.display_lcd("Stationary", 1, 3)

    motion_detected = my_mpu6050.check_motion()

    if my_mpu6050.is_shock_detected():
        print("Shock Detected! Alerting...")
        my_lcd.clear_lcd()
        my_lcd.display_lcd("Shock Detected", 1, 2)
        my_alarm.activate_alarm(2)
            
    # Checking for motion
    if motion_detected:
        print("Motion Detected!")
        my_lcd.clear_lcd()
        my_lcd.display_lcd("Motion Detected!", 1)
        is_moving = 1
    else:
        print("Stationary")
        my_lcd.clear_lcd()
        my_lcd.display_lcd("Stationary", 1, 3)


    time.sleep(1)
    my_alarm.signal_ok(3)

    ######################## Pulse and Alcohol sensor code #######################
    is_pulse = 0 # thingspeak variable

    current_time = time.monotonic()

    my_lcd.clear_lcd()
    my_lcd.display_lcd("Capturing Pulse", 1)
    my_lcd.display_lcd("Alcohol readings", 2)


    if alcohol_first_run or current_time - last_alcohol_measurement_time >= alcohol_measurement_interval:
        print("---")
        measure_alcohol()
        alcohol_first_run = False
        last_alcohol_measurement_time = time.monotonic()
        
    for _ in range(10):
        pulse_detected = my_adc.check_pulse() #Thinkspeak Variable
        if pulse_detected:
            my_lcd.clear_lcd()
            my_lcd.display_lcd("A Pulse was", 1, 2)
            my_lcd.display_lcd("Detected!!!", 2, 3)
            print("A pulse was detected!")
            is_pulse = 1
            break
        else:
            my_lcd.clear_lcd()
            my_lcd.display_lcd("No Pulse was", 1, 2)
            my_lcd.display_lcd("Detected!!!", 2, 3)
            #print("No pulse detected!")
        time.sleep(0.1)
               
    time.sleep(1)
    my_alarm.signal_ok(3)

    ######################## Temperature sensor code #######################
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Reading Object", 1, 1)
    my_lcd.display_lcd("Temperature...", 2, 1)

    time.sleep(3)

    ambient_temp = my_temp.get_ambient_temperature()
    object_temp = my_temp.get_object_temperature() # thingspeak variable

    print("Ambient Temperature: {:.2f} °C".format(ambient_temp))
    print("Target Temperature: {:.2f} °C".format(object_temp))
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Ambient: {:.2f}".format(ambient_temp), 1)
    my_lcd.display_lcd("Object: {:.2f}".format(object_temp), 2)

    if object_temp < 33.0 or object_temp > 42.0:
        print("WARNING: Abnormal Object Temperature Detected!")
        my_alarm.activate_alarm(3)
        my_lcd.clear_lcd()
        my_lcd.display_lcd("WARNING:Abnormal", 1)
        my_lcd.display_lcd("Temperature...", 2, 1)
        
    #Check if latest_sms variable is MC404
    if latest_sms == 'MC404':
        my_sms.send_sms(message=f"Alcohol: {alcohol_concentration}, Pulse: {pulse_detected}\n Temperature: {round(object_temp, 2)}, Motion: {motion_detected}")
    time.sleep(1)
    my_alarm.signal_ok(3)

    ######################## Battery% Checking code #######################
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Checking Battery", 1)
    my_lcd.display_lcd("Percentage%...", 2, 2)

    time.sleep(1)

    battery_lvl = get_battery_percentage() # thingspeak variable
    print(battery_lvl)
    my_lcd.clear_lcd()
    my_lcd.display_lcd(f"Battery% : {battery_lvl}%", 1)

    if battery_lvl < 20:
        print("WARNING: Please plug-in the device for charging!")
        my_alarm.activate_alarm(3)
        my_lcd.clear_lcd()
        my_lcd.display_lcd("WARNING: Low", 1, 2)
        my_lcd.display_lcd("Battery Alert!!", 2, 1)
        
    time.sleep(1)
    my_alarm.signal_ok(3)


    ######################## Uploading Data to thingspeak #######################
    my_lcd.clear_lcd()
    my_lcd.display_lcd("Publishing Data", 1)
    my_lcd.display_lcd("to thingspeak", 2, 2)

    thingspeak_list = [fence, lat, longi, round(object_temp, 2), alcohol_concentration, is_moving, battery_lvl, is_pulse]
    my_ts_data.send_real_data(thingspeak_list)

    if camera_on and wifi_connected:
        my_ts_image.send_image()

    time.sleep(1)
    my_alarm.signal_ok(3)


    ######################## Voice Logging code #######################
    current_time = time.monotonic()
    
    # Inside the main function, before the voice logging code:
    if voice_logging_first_run or current_time - voice_logging_timer >= voice_logging_interval:
        print("---")
        # Code for voice logging goes here
        my_lcd.clear_lcd()
        my_lcd.display_lcd("Voice Logging", 1, 1)
        my_lcd.display_lcd("Please be ready!", 2)
        time.sleep(2)

        # Play Random Log message
        sleep_time = my_speaker.play_log()
        time.sleep(my_speaker.get_sleep_duration(sleep_time))

        my_lcd.clear_lcd()
        my_lcd.display_lcd("Voice Processing", 1)
        my_lcd.display_lcd("Waiting 30s", 2, 3)

        # Record and transcribe audio
        if wifi_connected:
            generated_text, found_keywords = my_voice.record_and_transcribe(sleep_time)

            if generated_text is not None:
                print("Generated text:", generated_text)
                if found_keywords:
                    print("Found keywords:", found_keywords)
                    my_lcd.clear_lcd()
                    my_lcd.display_lcd("Found a voice!", 1, 1)
                    my_lcd.display_lcd("voice log done.", 2)
                    my_alarm.signal_ok(2)
                else:
                    print("No keywords found.")
                    my_lcd.clear_lcd()
                    my_lcd.display_lcd("No Speech found!", 1)
                    my_lcd.display_lcd("Activate Alert!", 2)
                    my_alarm.activate_alarm(3)
            else:
                print("Recording and transcription failed.")

        my_alarm.signal_ok(2)
        time.sleep(2)
    
        # Set the flag back to False after the first run
        voice_logging_first_run = False
        # Reset the timer
        voice_logging_timer = time.monotonic()

    
    
if __name__ == "__main__":
    wifi_setup()
    modem_auto_answer()
    while True:
        main()