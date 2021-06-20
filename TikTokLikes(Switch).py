#you will need a switch plugged into the RPI Pico:
#pin5(3v3) -> switch -> GP10 & GP15
#if the switch is connected for GP10 then it will constantly run the autoliker
#whereas if it is connected for GP15 then it will exit
#(to restart just plug the Pico in again - making usre the switch is on the correct side)


import time
import sys
import digitalio
import board
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

switch1_pin = board.GP10
switch0_pin = board.GP15

switch1 = digitalio.DigitalInOut(switch1_pin)
switch0 = digitalio.DigitalInOut(switch0_pin)

switch1.direction = digitalio.Direction.INPUT
switch0.direction = digitalio.Direction.INPUT

switch1.pull = digitalio.Pull.DOWN
switch0.pull = digitalio.Pull.DOWN


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
while True:
    if switch1.value: #if switch in "ON" position:
        time.sleep(0.1) #wait for video to load
        doubleclick() #doubleclick (like)
        scroll(-7)
    

    if switch0.value: #if switch in "OFF" position:
        for i in range(3): #flash the led 3 times
            flashinbuiltLED()
            time.sleep(0.25)
            
        sys.exit() #exit
    
#sys.exit()

for i in range(3): #flash the led 3 times
    flashinbuiltLED()
    time.sleep(0.25)
    
print("Script Ended")
            
    
    
    
    

