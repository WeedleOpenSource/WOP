#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
import sys

#Hot Air
Relay1Pin = 36
#Cold Air
Relay2Pin = 32
#Water
Relay3Pin = 33
#White Light
Relay4Pin = 35
#Blue Light
Relay5Pin = 37
#Red Light 
Relay6Pin = 38


def startstop():
    
    
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setwarnings(False)
    print 'Weedle OFF...'

    GPIO.setup(Relay1Pin, GPIO.OUT)
    time.sleep(2)
    GPIO.output(Relay1Pin, GPIO.HIGH)
    time.sleep(2)
    GPIO.setup(Relay2Pin, GPIO.OUT)
    time.sleep(2)
    GPIO.output(Relay2Pin, GPIO.HIGH)
    time.sleep(2)
    #GPIO.setup(Relay3Pin, GPIO.OUT)
    #time.sleep(1)
    #GPIO.output(Relay3Pin, GPIO.HIGH)
    #time.sleep(2)
    GPIO.setup(Relay4Pin, GPIO.OUT)
    time.sleep(2)
    GPIO.output(Relay4Pin, GPIO.HIGH)
    time.sleep(2)
    GPIO.setup(Relay5Pin, GPIO.OUT)
    time.sleep(2)
    GPIO.output(Relay5Pin, GPIO.HIGH)
    time.sleep(2)
    GPIO.setup(Relay6Pin, GPIO.OUT)
    time.sleep(2)
    GPIO.output(Relay6Pin, GPIO.HIGH)
    
def initLight():
    try:
        currentDir = os.path.dirname(os.path.realpath(__file__))
        #DAY CONFIG
        blue = currentDir + "/" + "config/weedleBlueLight.init"
        red = currentDir + "/" + "config/weedleRedLight.init"
        white = currentDir + "/" + "config/weedleWhiteLight.init"

        if os.path.isfile( blue ):
            with open(blue, "r") as f:
                    blueState = f.read().split('\n')[0]
                    print "##  Read Weedle blueState:" + blueState
                    if blueState == 'ON':
                        GPIO.setup(Relay5Pin, GPIO.OUT)
                        GPIO.output(Relay5Pin, GPIO.LOW)
                        time.sleep(2)

        if os.path.isfile( red ):
            with open(red, "r") as f:
                    redState = f.read().split('\n')[0]
                    print "##  Read Weedle redState:" + redState
                    if redState == 'ON':
                        GPIO.setup(Relay6Pin, GPIO.OUT)
                        GPIO.output(Relay6Pin, GPIO.LOW)
                        time.sleep(2)

        if os.path.isfile( white ):
            with open(white, "r") as f:
                    whiteState = f.read().split('\n')[0]
                    print "##  Read Weedle whiteState:" + whiteState
                    if whiteState == 'ON':
                        GPIO.setup(Relay4Pin, GPIO.OUT)
                        GPIO.output(Relay4Pin, GPIO.LOW)
                        time.sleep(2)


        else:
            sys.exit("ERROR: Please make sure you have a file to init Light in %s" % currentDir)

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

                


 
def destroy():
    GPIO.output(RelayPin, GPIO.HIGH)
    #GPIO.cleanup()                     # Release resource

def configFile():
    # check if the config file exists if not create them with defaul
    try:
        currentDir = os.path.dirname(os.path.realpath(__file__))
        #DAY CONFIG
        dayTimeLineConfigFile = currentDir + "/" + "config/daytimeline.config"
        dayInterfaceLineConfigFile = currentDir + "/" + "config/dayintervaleline.config"
        
        #daytimeline file
#        if os.path.isfile( dayTimeLineConfigFile ):
#            print 'Day Time Line Config in place'
#        else:
#            with open(dayTimeLineConfigFile, "w") as f:
#                f.write('CALL ONCE weedleConfigUpdate.py')
#                f.close()   

        #dayIntervaleline file
#        if os.path.isfile( dayInterfaceLineConfigFile ):
#            print 'Day Intervale line Config in place'
#        else:
#            with open(dayInterfaceLineConfigFile, "w") as f:
#                f.write('CALL weedleAdjustment.py \n')
#                f.write('CALL weedleDiagnostic.py')
#                f.close()   


        #WEEDLE CONFIG
        weedleDayConfigFile = currentDir + "/" + "config/weedleDay.config"
        weedleAdjustmentConfigFile = currentDir + "/" + "config/weedleAdjustment.config"
        weedleClimateConfigFile = currentDir + "/" + "config/weedleClimate.config"
       
        #Weedle Day Config
#        if os.path.isfile( weedleDayConfigFile ):
#            print 'Weedle Day Config in place'
#        else:
#            with open(weedleDayConfigFile, "w") as f:
#                f.write('CALL ONCE weedleSunON.py \n')
#                f.write('CALL ONCE weedleSunOFF.py')
#                f.close()   

        # Weedle Adjustment Config
#        if os.path.isfile( weedleAdjustmentConfigFile ):
#            print 'Weedle Adjustment Config in place'
#        else:
#            with open(weedleAdjustmentConfigFile, "w") as f:
#                f.write("TO PUT DEFAULT")
#                f.close()   
    
        # Weedle Climate Config
#        if os.path.isfile( weedleClimateConfigFile ):
#            print 'Weedle Climate Config in place'
#        else:
#            with open(weedleClimateConfigFile, "w") as f:
#                f.write("TO PUT DEFAULT")
#                f.close()   

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

def init():
    #setup()
    try:
        startstop()
        initLight()
#        configFile()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
    


if __name__ == '__main__':             # Program start from here
    init()
    #initLight()
    #setup()
    #try:
    #    action()
    #    configFile()
    #except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    #    destroy()
