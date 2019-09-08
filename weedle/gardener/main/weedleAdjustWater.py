import RPi.GPIO as GPIO
import time
import datetime
import math
import os
import sys

import elements.water.waterON
import elements.water.waterOFF
import elements.air.hotairON
import elements.air.hotairOFF
import elements.air.airON
import elements.air.airOFF

import config.readweedleClimate
import config.readweedleAdjustment

import sensations.readAirTemperature
import sensations.readCO2
import sensations.readSmellTemperature

import adjustClimateTools.applyT2WAS
import adjustClimateTools.applyHA2WAS
import adjustClimateTools.applyHS2WAS
import adjustClimateTools.applyC2WAS

water = "0"
air = "0"
sun = "0"

if __name__ == '__main__':             # Program start from here
    
    print "#######################################"
    print("#### IN WEEDLE ADJUSTMENT WATER  ####")
    print "#######################################"
    try:
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
        print "##############################################"
        print ("#### STARTING WEEDLE ADJUSTMENT WATER  ####")
        print "##############################################"
         
#### READ CLIMATE FROM CONFIG
#### HIGH        
        WTemperature = config.readweedleClimate("WTemperature")
        WHumidityAir = config.readweedleClimate("WHumidityAir")
        WHumiditySoil = config.readweedleClimate("WHumiditySoil")
        WCO2 = config.readweedleClimate("WCO2")
        WLuminosity = config.readweedleClimate("WLuminosity")
        print "####################################"
        print "######   WEEDLE CLIMATE HIGH  ######"
        print "####################################"
        print "## WTemperature = "+ WTemperature
        print "## WHumidityAir = "+ WHumidityAir
        print "## WHumiditySoil = "+ WHumiditySoil
        print "## WCO2 = "+ WCO2
        print "## WLuminosity = "+ WLuminosity
        print "####################################"

#### LOW        
        Wtemperature = config.readweedleClimate("Wtemperature")
        Whumidityair = config.readweedleClimate("Whumidityair")
        Whumiditysoil = config.readweedleClimate("Whumiditysoil")
        Wco2 = config.readweedleClimate("Wco2")
        Wluminosity = config.readweedleClimate("Wluminosity")
        print "####################################"
        print "######    WEEDLE CLIMATE LOW  ######"
        print "####################################"
        print "##  Wtemperature = "+ Wtemperature
        print "##  Whumidityair = "+ Whumidityair
        print "##  Whumiditysoil = "+ Whumiditysoil
        print "##  Wco2 = "+ Wco2
        print "##  Wluminosity = "+ Wluminosity
        print "####################################"
        
#### READ WATER IN BOX        
        soilHumidity40 = sensations.readSoilHumdity40()
        soilHumidity55 = sensations.readSoilHumdity55()
        soilHumidity70 = sensations.readSoilHumdity70()
        soilHumidity85 = sensations.readSoilHumdity85()


## CHECK POINT RESULT 

####  TEMPERATURE
        


#####  SOIL HUMIDITY
            
##Air Humidity first check
        if (soilHumidity40 == -100 and soilHumidity55 == -100
        and soilHumidity70 == -100 and soilHumidity85 == -100):
            soilHumidity40 = sensations.readSoilHumdity40()
            soilHumidity55 = sensations.readSoilHumdity55()
            soilHumidity70 = sensations.readSoilHumdity70()
            soilHumidity85 = sensations.readSoilHumdity85()
            print "\/\/\/\/\/\/\/\/"
            print "##### ALERT FAILED SOIL HUMIDITY ALL ONCE"
            print "\/\/\/\/\/\/\/\/"
        
        soilHumidity = 0
        

## if fails again set the Weedle SOIL Humidity    
        if (soilHumidity40 == -100 and soilHumidity55 == -100
        and soilHumidity70 == -100 and soilHumidity85 == -100):
            soilHumidity = Whumiditysoil
            print "\/\/\/\/\/\/\/\/"
            print "##### ALERT FAILED SOIL HUMIDITY ALL TWICE - SET WEEDLE CLIMATE DEFAULT - NO RUN SOIL HUMIDITY"
            print "\/\/\/\/\/\/\/\/"


### Calculate soilHumidity
        
        if soilHumidity40 == 1:
            soilHumidity = 1
        
        if soilHumidity55 == 1:
            soilHumidity = 1
        
        if soilHumidity70 == 1:
            soilHumidity = 1
        
        if soilHumidity85 == 1:
            soilHumidity = 1
  
        if soilHumidity == -100:
            ## SET DEFAULT
            soilHumidity = Whumiditysoil 
            print "\/\/\/\/\/\/\/\/"
            print "##### ALERT FAILED SOIL HUMIDITY  - SET WEEDLE CLIMATE DEFAULT  - NO RUN SOIL HUMIDITY"
            print "\/\/\/\/\/\/\/\/"





        print "####################################"
        print "####     IN THE BOX WATER        ###"
        print "####################################"
        print "## soilHumdity40 = "+ str(soilHumidity40)
        print "## soilHumdity55 = "+ str(soilHumidity55)
        print "## soilHumdity70 = "+ str(soilHumidity70)
        print "## soilHumdity85 = "+ str(soilHumidity85)
        print "## soilHumdity = "+ str(soilHumidity)
        print "####################################"

### LOG THE PULPSE
        currentDir = os.path.dirname(os.path.realpath(__file__))
        #GARDENER CONFIG
        #gardenerActions = currentDir + "/" + "logs/gardenerActions.log"
        gardenerActions = "/home/pi/weedle/gardener/main/logs/gardenerWaterActions.log"
        with open(gardenerActions, "a") as f:
            f.write('PULSEWATER|'+str(datetime.datetime.now())+"|"
                    +str(soilHumidity)+"|END_ACTION|\n")
            f.close()
 
        email = "/home/pi/weedle/gardener/main/logs/email.txt"
        with open(email, "w+") as f:
            f.write('Subject: PULSE\n\n'
                    +'PULSEWATER|'+str(datetime.datetime.now())+"|"
                    +str(soilHumidity)+"|END_ACTION|\n")
            f.close()
        
 
        print "#######  ADJUSTMENT ACTIONS  #######"

### CHECK SOIL HUMIDITY             
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
        print ("####  WEEDLE ADJUSTMENT SOIL HUMIDITY STARTING     ####")
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
       
#        if int(soilHumidity) > int(WHumiditySoil):
#            print "////////////////////////////"
#            print "======   SOIL TOO HUMID  ======"
#            print "////////////////////////////"
#            decrease = int(soilHumidity) - int(WHumiditySoil)
#            print "======   DECREASE OF --- " + str(decrease)
#            print "////////////////////////////"
#            adjustClimateTools.applyHS2WAS('DECREASE',decrease)
            
#        elif int(soilHumidity) < int(Whumiditysoil):
#            print "////////////////////////////"
#            print "=====    TOO DRY   ======="
#            print "////////////////////////////"
#            increase = int(Whumiditysoil) - int(soilHumidity)
#            print "=====    INCREASE OF  +++ " + str(increase)
#            print "////////////////////////////"
#            adjustClimateTools.applyHS2WAS('INCREASE',increase)

        adjustClimateTools.applyHS2WAS('INCREASE',13)
 
        print "######################################################"
        print ("####  WEEDLE ADJUSTMENT SOIL HUMIDITY COMPLETED #####")
        print "######################################################"



        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
 

 
        print "################################################"
        print ("####  WEEDLE ADJUSTMENT WATER COMPLETED #####")
        print "################################################"
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
  
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
