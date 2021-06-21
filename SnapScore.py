'''
Aim: Make my snapscore go up;

Reason; Why Not

Basis; a Snapscore goes up everytime you send a picture (not text only).

Method;
- open the top person on snapchat
- take a picture (this will be of whatever the camera sees - black/the ceiling)
- add text???
- send picture

- Repeat

'''

import time
import sys
import digitalio
import board
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS #be able to type

#declare what interface the usb_hid connection is
keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard) #setup the keyboard interface

button_pin = board.GP15

button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN


led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False #turn off the led




#other functions

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

def getbuttonstate():
    print("Get button state")
    if button.value:
        print("button pressed")
        return True    
    else:
        return False

def click():
    mouse.click(Mouse.LEFT_BUTTON)

def resetmouse():
    goto("bottom_right_corner")
    goto("centre")

#places:
#open chat tab
def openchat():
    time.sleep(1) #wait 1 second
    mouse.move(-1000,1000)#go to bottom left corner
    mouse.move(y=30)#move to the center of the button bar
    mouse.move(x=100)#move right a bit
    click()    

#open the spotlight tab
def openspotlight():
    time.sleep(1) #wait 1 second
    mouse.move(1000,1000) #go to the bottom right corner
    mouse.move(y=-20)#go up into the apps bottom corner not the screens bottom corner
    click()

#open the top chat
def open_top_person():
    openchat() #open the chat tab
    time.sleep(1) #wait 1 second
    mouse.move(-1000,-1000)#go to top left corner
    mouse.move(y=100)#go down a bit
    mouse.move(x=300) #go right a bit (so you open the chat not their profile)
    click()

#opens the camera in the top person chat
def open_camera_top_person():
    open_top_person() #open the chat with the top person
    time.sleep(1) #wait 1 second
    mouse.move(-1000,1000) #go to bottom left corner
    mouse.move(x=20) #go right a bit
    mouse.move(y=-20) #go up a bit
    click()
    
#take a picture for the top persons chat
def take_picture_top_person():
    open_camera_top_person() #opens the camera in the top persons chat
    time.sleep(1) #wait 1 second
    mouse.move(1000,1000) #go to the bottom right corner
    mouse.move(y=-100)#go up a bit
    mouse.move(x=-250)#go left a bit
    click()
    
def send_picture_top_person():
    take_picture_top_person()
    time.sleep(1) #wait 1 second
    mouse.move(1000,1000) #go to the bottom right corner
    mouse.move(y=-40)#go up into the apps bottom corner not the screens bottom corner
    click()
    time.sleep(1) #wait 1 seconds
    click()

def addtext(text):
    time.sleep(1) #wait 1 second
    mouse.move(1000,-1000)#go to top right corner
    mouse.move(y=40)#go down into the apps top corner not the screens top corner
    mouse.move(x=-15) #go to the left a little bit so that it is in the app
    click()
    time.sleep(1) #wait 1 second
    layout.write(text)
    goto("centre")
    click()
    

def send_picturemessage_top_person(message):
    take_picture_top_person()
    time.sleep(1) #wait 1 second
    addtext(message)
    goto("centre")
    click() #click the centre to exit the text menu
    
    
    mouse.move(1000,1000) #go to the bottom right corner
    mouse.move(x=-36) # move to the left slightly
    mouse.move(y=-38)#go up to the send button
    flashinbuiltLED()
    click()
    time.sleep(2) #wait 2 seconds
    click()
    
def keep_sending_picturemessage(message):
    #open camera
    time.sleep(1) #wait 1 second
    mouse.move(-1000,1000) #go to bottom left corner
    mouse.move(x=20) #go right a bit
    mouse.move(y=-20) #go up a bit
    click()
    
    #take picture
    time.sleep(1) #wait 1 second
    mouse.move(1000,1000) #go to the bottom right corner
    mouse.move(y=-100)#go up a bit
    mouse.move(x=-250)#go left a bit
    click()
    
    #add text
    time.sleep(1) #wait 1 second
    addtext(message)
    goto("centre")
    click() #click the centre to exit the text menu
    
    
    mouse.move(1000,1000) #go to the bottom right corner
    mouse.move(x=-36) # move to the left slightly
    mouse.move(y=-38)#go up to the send button
    flashinbuiltLED()
    click()
    time.sleep(2) #wait 2 seconds
    click()
    
    


#######################################

#goto predetermined places
def goto(place):

    #switch the camera from front to back or vice versa
    if place == "camera_switch":
        time.sleep(1) #wait 1 second
        mouse.move(1000,-1000)#go to top right corner
        mouse.move(y=40)#go down into the apps top corner not the screens top corner
        mouse.move(x=-15) #go to the left a little bit so that it is in the app
        click()
    
    #click top persons profile (only works once chat has been opened)
    elif place == "top_profile":
        time.sleep(1) #wait 1 second
        mouse.move(-1000,-1000)#go to top left corner
        mouse.move(y=100)#go down a bit
        mouse.move(x=20)
        click()
    
    #click top persons chat (only works once chat has been opened)
    elif place == "top_person":
        time.sleep(1) #wait 1 second
        mouse.move(-1000,-1000)#go to top left corner
        mouse.move(y=100)#go down a bit
        mouse.move(x=100)
        click()
        
        
####################################### 
    
    #go to various corners / centre (does not click for any - only goes to)
    
    elif place == "bottom_right_corner":
        time.sleep(1) #wait 1 second
        mouse.move(1000,1000)
        
    elif place == "top_left_corner":
        time.sleep(1) #wait 1 second
        mouse.move(-1000,-1000)#go to top left corner
        mouse.move(y=20)#go down into the apps top corner not the screens top corner
        
    elif place == "top_right_corner":
        time.sleep(1) #wait 1 second
        mouse.move(1000,-1000)#go to top right corner
        mouse.move(y=30)#go down into the apps top corner not the screens top corner
        mouse.move(x=5) #go to the left a little bit so that it is in the app
        
    elif place == "bottom_left_corner":
        time.sleep(1) #wait 1 second
        mouse.move(-1000,1000)
        
    elif place == "centre":
        time.sleep(1) #wait 1 second
        mouse.move(1000,1000) #go to the bottom right corner
        mouse.move(y=-350)#go up a bit
        mouse.move(x=-175)#go in a bit
    

  

def buttonactive():
    time.sleep(1) #wait 1 second
    if button.value:
        flashinbuiltLED()
        return True
        
    else:
        for i in range(3):
            flashinbuiltLED()
            time.sleep(1)
        sys.exit()

def checkexitbutton():
    time.sleep(1)
    if button.value:
        sys.exit()
    else:
        flashinbuiltLED()

if buttonactive():
    send_picturemessage_top_person("This is a Bot") #do the first one (this opens the chat)
    time.sleep(2) #wait 2 seconds between snaps
    keep_sending_picturemessage("This is also a bot") #this just uses the open chat
    botnum = 1
    time.sleep(2) #wait 2 seconds between snaps
    while True:
        keep_sending_picturemessage(f"This is bot #{botnum}") #this just uses the open chat
        botnum = botnum+1
        time.sleep(2) #wait 2 seconds between snaps
        checkexitbutton()
    


