#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
#Water
RelayPinRedLight = 38

def action():
    try:
        print ('##### IN RED LIGHT OFF ####')
        GPIO.setmode(GPIO.BOARD)   # Numbers GPIOs by physical location
        GPIO.setwarnings(False)
        GPIO.setup(RelayPinRedLight, GPIO.OUT)
        print 'Red Light OFF...'
        GPIO.output(RelayPinRedLight, GPIO.HIGH)
        time.sleep(2)
        
        logState = "/home/pi/weedle/gardener/main/config/weedleRedLight.init"
        with open(logState, "w+") as f:
            f.write('OFF')
            f.close()

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
        
  
def destroy():
    GPIO.output(RelayPinRedLight, GPIO.HIGH) 

if __name__ == '__main__':             # Program start from here
    try:
        action()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
