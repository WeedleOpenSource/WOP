#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
#Hot Air
RelayHotAir = 36
 
def action():
    try:
        
        print ('##### IN SUN OFF ####')
        GPIO.setmode(GPIO.BOARD)   # Numbers GPIOs by physical location
        GPIO.setwarnings(False)
        GPIO.setup(RelayHotAir, GPIO.OUT)
        print 'Hot Air OFF...'
        GPIO.output(RelayHotAir, GPIO.HIGH)
        time.sleep(2)
        #GPIO.cleanup()                     # Release resource
        
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
  
def destroy():
    GPIO.output(RelayHotAir, GPIO.HIGH) 

if __name__ == '__main__':             # Program start from here
    try:
        action()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

