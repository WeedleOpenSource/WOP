#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
#Hot Air
RelayAir = 32

def action():
    try:
        print ('##### IN AIR ON ####')
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        GPIO.setwarnings(False)
        GPIO.setup(RelayAir, GPIO.OUT)
        print 'Air ON...'
        GPIO.output(RelayAir, GPIO.LOW)
        #time.sleep(2)
        #GPIO.cleanup()                     # Release resource

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

def destroy():
    GPIO.output(RelayAir, GPIO.HIGH)

if __name__ == '__main__':             # Program start from here
    try:
        action()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()


