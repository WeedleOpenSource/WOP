#include <wiringPi.h>
#include <stdio.h>

#define TrackSensorPin    0
#define LedPin            4

int main(void)
{
	if(wiringPiSetup() == -1)
	{ 
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	pinMode(TrackSensorPin, INPUT);
	pinMode(LedPin,  OUTPUT);

	while(1)
	{
		if(digitalRead(TrackSensorPin) == LOW)
		{
			digitalWrite(LedPin, LOW);     
			delay(100);
		}	
		else
		{
			digitalWrite(LedPin, HIGH);
			delay(100);
		}
	}

	return 0;
}
