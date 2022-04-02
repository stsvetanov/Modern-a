import serial
import time
import pyautogui

serial_port = serial.Serial("com5", 9600)
time.sleep(2)

# while True:
#     pyautogui.hotkey('space')
#     time.sleep(4)


while True:
    incoming = str(serial_port.readline())

    print(incoming)

    incoming.strip()
    print(incoming)

    if "play" in incoming:
        pyautogui.hotkey('space')

