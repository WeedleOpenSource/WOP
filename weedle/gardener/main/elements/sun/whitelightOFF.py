#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
#White light
RelayPinWhiteLight = 35

def action():
    try:
        print ('##### IN WHITE LIGHT OFF ####')
        GPIO.setmode(GPIO.BOARD)   # Numbers GPIOs by physical location
        GPIO.setwarnings(False)
        GPIO.setup(RelayPinWhiteLight, GPIO.OUT)
        print 'White Light OFF...'
        GPIO.output(RelayPinWhiteLight, GPIO.HIGH)
        time.sleep(2)
        
        logState = "/home/pi/weedle/gardener/main/config/weedleWhiteLight.init"
        with open(logState, "w+") as f:
            f.write('OFF')
            f.close()
        
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
  
def destroy():
    GPIO.output(RelayPinWhiteLight, GPIO.HIGH) 

if __name__ == '__main__':             # Program start from here
    try:
        action()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
