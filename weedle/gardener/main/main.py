#!/usr/bin/env python

import os
import sys
import time
from datetime import datetime
from datetime import timedelta
import initWeedle

from subprocess import call
from threading import Thread
from time import sleep

from command import Command

FIELD_SEPARATOR="|"

timeDictionary = {}

# Simple function to get and format the current time
def getTime():
    return datetime.now()

def convertTimeToString( time ):
    timeString = ""

    if ( time.hour < 10 ):
        timeString = "0"

    timeString = timeString + str(time.hour) + ":"

    if ( time.minute < 10 ):
        timeString = timeString + "0"

    timeString = timeString + str(time.minute)

    return timeString

def init():
    #initialized Weedle
    initWeedle.init()
    
    ### MANQUE A INITIALISER le dayTimeLine
    
    ### AUSSI il faut changer pour faire reload dans les ARRAY toutes actions apres 24H RUN....
    
    
    print "Initializing Weedle Day..."

    # Find out which directory we are in
    currentDir = os.path.dirname(os.path.realpath(__file__))

#    timeConfigFile = currentDir + "/" + "config/daytimeline.config"
    timeConfigFile = currentDir + "/" + "config/weedleDay.config"

    if os.path.isfile( timeConfigFile ):
        with open(timeConfigFile, "r") as f:
            for line in f:
                if ( line.startswith("#") == False ):
                    lineInfo = line.split(FIELD_SEPARATOR)
    
                    if ( len(lineInfo) != 2 and len(lineInfo) != 4 ):
                        print "There was an issue processing line: %s" % line
                        continue
    
                    # We create an empty array of commands if there is no array at all              
                    if ( lineInfo[0] not in timeDictionary):
                        timeDictionary[lineInfo[0]] = []

                    # Create an instance of the Command
                    if ( len(lineInfo) == 2 ):
                        command = Command(lineInfo[1].strip())
                    else:
                        command = Command(lineInfo[1].strip(), lineInfo[2].strip(), lineInfo[3].strip())

                    # Add it to the list of commands to execute at that time
                    timeDictionary[lineInfo[0]].append(command)
    else:
        sys.exit("ERROR: Please make sure you have a file called daytimeline.txt in %s" % currentDir)
                
    #intervalConfigFile = currentDir + "/" + "config/dayintervaleline.config"
    intervalConfigFile = currentDir + "/" + "config/weedleDayTask.config"
    if os.path.isfile( intervalConfigFile ):
        with open(intervalConfigFile, "r") as f:
            for line in f:
                if ( line.startswith("#") == False ):
                    lineInfo = line.split(FIELD_SEPARATOR)
                    if ( len(lineInfo) != 2 ):
                        continue

                    command = Command(lineInfo[1].strip())

                    # We start at midnight
                    startTime = getTime().replace(hour=0, minute=0, second=0, microsecond=0)

                    timeOffset = 0

                    #there is 1440 minutes in 24 hours
                    while timeOffset < 1440:
                        currentTime = startTime + timedelta(minutes=timeOffset)
                        currentTimeString = convertTimeToString(currentTime)
                        if ( currentTimeString not in timeDictionary):
                            timeDictionary[currentTimeString] = []
                        timeDictionary[currentTimeString].append(command)
                        timeOffset = timeOffset + int(lineInfo[0])

    print "Initialization complete."

def loop():
    while True:
        global currentTime
        currentTime = getTime()

        currentTimeString = convertTimeToString(currentTime)

        # Print the current time
        print "current time is: %s" % currentTimeString

        # Check if we have something to do  
        if ( currentTimeString in timeDictionary ):
            print "There are %i commands to trigger" % len(timeDictionary[ currentTimeString ])
            # We have some entries in the time dictionary
            # Iterate through all of them and trigger their commands
            for command in timeDictionary[ currentTimeString ]:
                print str(command)
                thread = Thread(target = command.run)
                thread.start()
        else:
            print "There are no command to trigger for current time: %s" % (currentTimeString)

        # Sleep until the next minute
        # Note that this WILL have issues if the command take more than a minute to run...
        timeAfterCommands = getTime()
        print "Main thread sleeping for %d seconds" % (60 - timeAfterCommands.second)
        sleep(60 - timeAfterCommands.second)


if __name__ == '__main__':
    init()
    
    try:
        loop()
    except KeyboardInterrupt: 
        print 'The end !'

