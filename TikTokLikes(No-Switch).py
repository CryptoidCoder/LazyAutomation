import time
import sys
import digitalio
import board
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False #turn off the led

def doubleclick():
    #print("Double Clicked")
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.1)
    mouse.click(Mouse.LEFT_BUTTON)
    
def scroll(scroll):
    #print("Scrolling")
    mouse.move(wheel=scroll)
    time.sleep(3)

def flashinbuiltLED():
    led.value = True
    time.sleep(0.5)
    led.value = False

    
#main:
while True: #always repeat
    time.sleep(0.1) #wait for video to load
    doubleclick() #doubleclick (like)
    scroll(-7) #scroll towards you (next vid will be below)
    flashinbuiltLED() #Flash the LED to show a video has been liked

    
print("Script Ended")
    
    
    
    


