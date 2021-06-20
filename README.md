# Lazy Automation

Random automation Things To help with your laziness


These are either designed as HID (to replicate a keyboard + mouse) OR a python file that you can just run and it will automate various things

If it is HID:
- You will need a [Raspberry Pi Pico](https://thepihut.com/products/raspberry-pi-pico):
- You will need to be running circuitpython on it with the [adafruit_hid](https://github.com/adafruit/Adafruit_CircuitPython_HID) modules added.
- You will need the correct cable / OTG adapters
-   This i will leave up to you; you need to get from micro USB (on the Pico) to whatever your phone inputs (USB Type-C, Micro USB, Anyting Else) - I suggest you get a Micro-USB -> USB-A Cable and then buy the appropriate USB-A OTG adapter.


## Index:

### TikTok Autoliker:
Are you tired of be a good friend, do you feel you just can't be bothered to go through your friends TikToks and endlessly give them likes?
Well i have the solution for you.

This script can just be renamed `code.py` - to run on boot, and then open TikTok go to Following, and plug the Pico into your device. 
Voila it will like every video.


### SnapChat SnapScorer:
Are you just straight fed up of keeping those streaks going?
Does it annoy you that your SnapScore isn't what it could be?

This script can just be renamed `code.py` - to run on boot, and then open snapchatg, and plug the Pico into your device. 
Voila it will send a gazillion message to the latest person you messaged/messaged you. your snapscore will skyrocket.

#### TODO:
- Add functionality to send a 'Streak' message at a certian time everyday, to certain people

