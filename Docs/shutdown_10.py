# Python Program for termination of a Windows PC
import os

def shutdown_computer():
    try:
        os.system("shutdown /s /t 10")  # /s specifies shutdown, /t sets the time delay to 0 seconds
    except Exception as e:
        print(f"Error shutting down the computer: {e}")

def restart_windows():
    try:
        os.system("shutdown /r /t 5")
    except Exception as e:
        print(f"Error: {e}")
        
def sleep_mode():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

if __name__ == "__main__":
    command = input("Input system command: \n")
    match command:
        case 'h':
            print("OS is shutting down in 10s!")
            shutdown_computer()
        case 'r':
            print("OS is restarting in 5s!")
            restart_windows()
        case 's':
            print("SYSTEM sleeping")
            sleep_mode()
