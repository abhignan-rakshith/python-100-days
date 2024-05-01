import I2C_LCD_driver

class LCD:
    """Class for controlling an I2C LCD display."""
    
    def __init__(self):
        """Initialize the LCD display."""
        try:
            self.LCD = I2C_LCD_driver.lcd()
        except OSError as e:
            if e.errno == 121:
                print("LCD Error: Remote I/O Error. Check LCD connection.")
                raise SystemExit("LCD initialization failed.")  # Terminate execution
    
    def display_lcd(self, text, line=1, pos=0):
        """Display text on the LCD display.

        Args:
            text (str): The text to display.
            line (int, optional): The line number on the LCD. Defaults to 1.
            pos (int, optional): The starting position on the line. Defaults to 0.
        """
        self.LCD.lcd_display_string(f"{text}", line, pos)
        
    def clear_lcd(self):
        """Clear the LCD display."""
        self.LCD.lcd_clear()
        
if __name__ == "__main__":
    # Test the LCD class
    my_LCD = LCD()
    my_LCD.display_lcd(text="Hello World")
