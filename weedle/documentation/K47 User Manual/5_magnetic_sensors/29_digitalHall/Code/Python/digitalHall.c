#include <wiringPi.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

#define LedPin 4
#define SensorPin 0

int main(void)
{
	if(wiringPiSetup() == -1)
	{ 
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	pinMode(LedPin, OUTPUT);
	pinMode(SensorPin, INPUT);
	
	while(1)
	{
		if(digitalRead(SensorPin))
		{
			digitalWrite(LedPin, LOW);
		}
		else
		{
			digitalWrite(LedPin, HIGH);
		}
		delay(200);	
	}
	
	return 0;
}

