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
#import config.readweedleAdjustment

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
    print("#### IN WEEDLE ADJUSTMENT CLIMATE  ####")
    print "#######################################"
    try:
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
        print "##############################################"
        print ("#### STARTING WEEDLE ADJUSTMENT CLIMATE  ####")
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
        
#### READ CLIMATE IN BOX        
        airTemperature = sensations.readAirTemperature()
        #airTemperature = sensations.readTemperature()
        airHumidity = sensations.readAirHumidity()
        #airHumidity = -100
#        soilHumidity40 = sensations.readSoilHumdity40()
#        soilHumidity55 = sensations.readSoilHumdity55()
#        soilHumidity70 = sensations.readSoilHumdity70()
#        soilHumidity85 = sensations.readSoilHumdity85()
        luminosity = sensations.readLuminosity()
        #co2 = sensations.readCO2()
        co2 = -100


## CHECK POINT RESULT 

####  TEMPERATURE
        
##Air Temperature first check
        if airTemperature == -100:
            airTemperature = sensations.readAirTemperature()
            print "\/\/\/\/\/\/\/\/"
            print "#### ALERT FAILED AIR TEMPERATURE ONCE"
            print "\/\/\/\/\/\/\/\/"

## if fails again set the Weedle Temperature    
        if airTemperature == -100:
            airTemperature = Wtemperature
            print "\/\/\/\/\/\/\/\/"
            print "#### ALERT FAILED AIR TEMPERATURE TWICE - SET WEEDLE CLIMATE DEFAULT - NO RUN TEMPERATURE"
            print "\/\/\/\/\/\/\/\/"

#####  AIR HUMIDITY
            
##Air Humidity first check
        if airHumidity == -100:
            airHumidity = sensations.readAirHumidity()
            print "\/\/\/\/\/\/\/\/"
            print "##### ALERT FAILED AIR HUMIDITY ONCE"
            print "\/\/\/\/\/\/\/\/"

## if fails again set the Weedle Humidity    
        if airHumidity == -100:
            airHumidity = Whumidityair
            print "\/\/\/\/\/\/\/\/"
            print "##### ALERT FAILED AIR HUMIDITY TWICE - SET WEEDLE CLIMATE DEFAULT  - NO RUN AIR HUMIDITY"
            print "\/\/\/\/\/\/\/\/"


#####  SOIL HUMIDITY
            
##Air Humidity first check
#        if (soilHumidity40 == -100 and soilHumidity55 == -100
#        and soilHumidity70 == -100 and soilHumidity85 == -100):
#            soilHumidity40 = sensations.readSoilHumdity40()
#            soilHumidity55 = sensations.readSoilHumdity55()
#            soilHumidity70 = sensations.readSoilHumdity70()
#            soilHumidity85 = sensations.readSoilHumdity85()
#            print "\/\/\/\/\/\/\/\/"
#            print "##### ALERT FAILED SOIL HUMIDITY ALL ONCE"
#            print "\/\/\/\/\/\/\/\/"
        
#        soilHumidity = 0
        

## if fails again set the Weedle SOIL Humidity    
#        if (soilHumidity40 == -100 and soilHumidity55 == -100
#        and soilHumidity70 == -100 and soilHumidity85 == -100):
#            soilHumidity = Whumiditysoil
#            print "\/\/\/\/\/\/\/\/"
#            print "##### ALERT FAILED SOIL HUMIDITY ALL TWICE - SET WEEDLE CLIMATE DEFAULT - NO RUN SOIL HUMIDITY"
#            print "\/\/\/\/\/\/\/\/"


### Calculate soilHumidity
        
#        if soilHumidity40 == 1:
#            soilHumidity = 1
#        
#        if soilHumidity55 == 1:
#            soilHumidity = 1
#        
#        if soilHumidity70 == 1:
#            soilHumidity = 1
#        
#        if soilHumidity85 == 1:
#            soilHumidity = 1
  
#        if soilHumidity == -100:
            ## SET DEFAULT
#            soilHumidity = Whumiditysoil 
#            print "\/\/\/\/\/\/\/\/"
#            print "##### ALERT FAILED SOIL HUMIDITY  - SET WEEDLE CLIMATE DEFAULT  - NO RUN SOIL HUMIDITY"
#            print "\/\/\/\/\/\/\/\/"


#####  LIMINOSITY
            
##Air Humidity first check
        if luminosity == -100:
            luminosity = sensations.readluminosity()
            print "\/\/\/\/\/\/\/\/"
            print "##### ALERT FAILED LUMINOSITY ONCE"
            print "\/\/\/\/\/\/\/\/"

## if fails again set the Weedle Humidity    
        if luminosity == -100:
            luminosity = Wluminosity
            print "\/\/\/\/\/\/\/\/"
            print "##### ALERT FAILED LUMINOSITY TWICE - SET WEEDLE CLIMATE DEFAULT  - NO RUN LUMINOSITY"
            print "\/\/\/\/\/\/\/\/"


#####  CO2

##CO2 first check
        if co2 == -100:
       #     co2 = sensations.readCO2()
            print "\/\/\/\/\/\/\/\/"
            print "##### ALERT FAILED CO2 ONCE"
            print "\/\/\/\/\/\/\/\/"

## if fails again set the Weedle Humidity    
        if co2 == -100:
            co2 = Wco2
            print "\/\/\/\/\/\/\/\/"
            print "##### ALERT FAILED CO2 TWICE - SET WEEDLE CLIMATE DEFAULT  - NO RUN CO2"
            print "\/\/\/\/\/\/\/\/"




        print "####################################"
        print "####     IN THE BOX CLIMATE     ###"
        print "####################################"
        print "## airTemperature = "+ str(airTemperature)
        print "## airHumdity = "+ str(airHumidity)
#        print "## soilHumdity40 = "+ str(soilHumidity40)
#        print "## soilHumdity55 = "+ str(soilHumidity55)
#        print "## soilHumdity70 = "+ str(soilHumidity70)
#        print "## soilHumdity85 = "+ str(soilHumidity85)
#        print "## soilHumdity = "+ str(soilHumidity)
        print "## luminosity = "+ str(luminosity)
        print "## co2 = "+ str(co2)
        print "####################################"

### LOG THE PULPSE
        currentDir = os.path.dirname(os.path.realpath(__file__))
        #GARDENER CONFIG
        #gardenerActions = currentDir + "/" + "logs/gardenerActions.log"
        gardenerActions = "/home/pi/weedle/gardener/main/logs/gardenerActions.log"
        with open(gardenerActions, "a") as f:
            f.write('PULSE|'+str(datetime.datetime.now())+"|"
                    +str(airTemperature)+"|"
                    +str(airHumidity)+ "|"
#                    +str(soilHumidity)+ "|"
#                    + str(soilHumidity)+"|"
                    + str(co2)+"|END_ACTION|\n")
            f.close()
 
        email = "/home/pi/weedle/gardener/main/logs/email.txt"
        with open(email, "w+") as f:
            f.write('Subject: PULSE\n\n'
                    +'PULSE|'+str(datetime.datetime.now())+"|"
                    +str(airTemperature)+"|"
                    +str(airHumidity)+ "|"
#                    +str(soilHumidity)+ "|"
#                    + str(soilHumidity)+"|"
                    + str(co2)+"|END_ACTION|\n")
            f.close()
        
 
        print "#######  ADJUSTMENT ACTIONS  #######"
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
        print ("####  WEEDLE ADJUSTMENT TEMPERATURE STARTING  ####")
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
     
        #airTemperature = 25
        
### CHECK TEMPERATURE
        if int(airTemperature) > int(WTemperature):
            print "////////////////////////////"
            print "=======   TOO HOT   ======"
            print "////////////////////////////"
            decrease = int(airTemperature) - int(WTemperature)
            print "=======   DECREASE OF --- " + str(decrease)
            print "////////////////////////////"
            adjustClimateTools.applyT2WAS('DECREASE',decrease)
            
        elif int(airTemperature) < int(Wtemperature):
            print "////////////////////////////"
            print "=======   TOO COLD  ======"
            print "////////////////////////////"
            increase = int(Wtemperature) - int(airTemperature)
            print "=======   INCREASE OF +++ " + str(increase)
            print "////////////////////////////"
            adjustClimateTools.applyT2WAS('INCREASE',increase)

        print "###################################################"
        print ("####  WEEDLE ADJUSTMENT TEMPERATURE COMPLETED ####")
        print "###################################################"

        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
           
### CHECK AIR HUMIDITY             
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
        print ("####  WEEDLE ADJUSTMENT AIR HUMIDITY STARTING     ####")
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
       
        if int(airHumidity) > int(WHumidityAir):
            print "///////////////////////////////"
            print "======   AIR TOO HUMID  ======"
            print "///////////////////////////////"
            decrease = int(airHumidity) - int(WHumidityAir)
            print "======   DECREASE OF --- " + str(decrease)
            print "////////////////////////////"
            adjustClimateTools.applyHA2WAS('DECREASE',decrease)
            
        elif int(airHumidity) < int(Whumidityair):
            print "///////////////////////////////"
            print "=====    AIR TOO DRY   ======="
            print "///////////////////////////////"
            increase = int(Whumidityair) - int(airHumidity)
            print "=====    INCREASE OF  +++ " + str(increase)
            print "////////////////////////////"
            adjustClimateTools.applyHA2WAS('INCREASE',increase)
 
        print "#################################################"
        print ("####  WEEDLE ADJUSTMENT AIR HUMIDITY COMPLETED #####")
        print "#################################################"

        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"

### CHECK SOIL HUMIDITY             
#        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
#        print ("####  WEEDLE ADJUSTMENT SOIL HUMIDITY STARTING     ####")
#        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
       
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
 
#        print "######################################################"
#        print ("####  WEEDLE ADJUSTMENT SOIL HUMIDITY COMPLETED #####")
#        print "######################################################"


### CHECK LUMINOSITY             
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
        print ("####  WEEDLE ADJUSTMENT LUMINOSITY STARTING     ####")
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
       
        if int(luminosity) > int(WLuminosity):
            print "////////////////////////////"
            print "======   TOO MUCH LIGHT HUMID  ======"
            print "////////////////////////////"
            decrease = int(luminosity) - int(WLuminosity)
            print "======   DECREASE OF --- " + str(decrease)
            print "////////////////////////////"
            adjustClimateTools.applyL2WAS('DECREASE',decrease)
            
        elif int(luminosity) < int(Wluminosity):
            print "////////////////////////////"
            print "=====    NOT ENOUGHT LIGHT   ======="
            print "////////////////////////////"
            increase = int(Wluminosity) - int(luminosity)
            print "=====    INCREASE OF  +++ " + str(increase)
            print "////////////////////////////"
            adjustClimateTools.applyL2WAS('INCREASE',increase)
 
        print "######################################################"
        print ("####  WEEDLE ADJUSTMENT LUMINOSITY COMPLETED #####")
        print "######################################################"

### CHECK CO2             
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
        print ("####  WEEDLE ADJUSTMENT CO2 STARTING     ####")
        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
       
        if int(co2) > int(WCO2):
            print "////////////////////////////"
            print "======   TOO MUCH CO2   ======"
            print "////////////////////////////"
            decrease = int(co2) - int(WCO2)
            print "======   DECREASE OF --- " + str(decrease)
            print "////////////////////////////"
            adjustClimateTools.applyC2WAS('DECREASE',decrease)
            
        elif int(co2) < int(Wco2):
            print "////////////////////////////"
            print "=====    NOT ENOUGHT CO2   ======="
            print "////////////////////////////"
            increase = int(Wco2) - int(co2)
            print "=====    INCREASE OF  +++ " + str(increase)
            print "////////////////////////////"
            adjustClimateTools.applyC2WAS('INCREASE',increase)
 
        print "######################################################"
        print ("####  WEEDLE ADJUSTMENT CO2 COMPLETED #####")
        print "######################################################"


        print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
 

 
        print "################################################"
        print ("####  WEEDLE ADJUSTMENT CLIMATE COMPLETED #####")
        print "################################################"
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
        print "\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==\/\/<3==  "
  
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
