from gpiozero import LED, Buzzer
import time

class Alarm:
    """Class for controlling alarm system with buzzer and LEDs."""
    
    def __init__(self, buzzer_pin=17, rled_pin=22, bled_pin=27):
        """Initialize Alarm with default pin configurations."""
        self.buzzer = Buzzer(buzzer_pin)
        self.red_led = LED(rled_pin)
        self.blue_led = LED(bled_pin)
        
        # Turn off buzzer and LEDs initially
        self.buzzer.off()
        self.red_led.off()
        self.blue_led.off()
        
    
    def activate_alarm(self, num_repeats=3):
        """Activate alarm by flashing red LED and sounding buzzer."""
        print("Activating alarm!")
        for _ in range(num_repeats):
            # Turn on buzzer and red LED
            self.buzzer.on()
            self.red_led.on()
            time.sleep(0.2)  # Buzzer and LED on for 0.2 seconds
            
            # Turn off buzzer and red LED
            self.buzzer.off()
            self.red_led.off()
            time.sleep(0.2)  # Buzzer and LED off for 0.2 seconds
    
    def signal_ok(self, num_repeats=1):
        """Signal OK by flashing blue LED and sounding buzzer."""
        print("Activating OK Signal")
        for _ in range(num_repeats):
            # Turn on buzzer and green LED
            self.buzzer.on()
            self.blue_led.on()
            time.sleep(0.1)  # Buzzer and LED on for 0.1 seconds
            
            # Turn off buzzer and green LED
            self.buzzer.off()
            self.blue_led.off()
            time.sleep(0.1)  # Buzzer and LED off for 0.1 seconds
    
    def blue_light(self):
        """Turn on blue LED."""
        print("Blue Light ON")
        self.blue_led.on()
    
    def red_light(self):
        """Turn on red LED."""
        print("Red Light ON")
        self.red_led.on()
    
    def buzzer_on(self):
        """Turn on buzzer."""
        print("Buzzer ON")
        self.buzzer.on()

if __name__ == "__main__":
    # Test Alarm
    my_alarm = Alarm()
    my_alarm.signal_ok(5)
