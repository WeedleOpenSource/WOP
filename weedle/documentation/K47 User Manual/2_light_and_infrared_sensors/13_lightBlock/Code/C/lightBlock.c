#include <wiringPi.h>
#include <stdio.h>

#define LightBreakPin     0
#define LedPin            4

int main(void)
{
	if(wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !");
		return -1; 
	}
	
	pinMode(LightBreakPin, INPUT);
	pullUpDnControl(LightBreakPin, PUD_UP);
	pinMode(LedPin,  OUTPUT);

	while(1)
	{
		if(digitalRead(LightBreakPin) == LOW)
		{
			printf("Be covered....\n");
			digitalWrite(LedPin, HIGH);     //led on
		}	
		else
		{
			digitalWrite(LedPin, LOW);		//led off	
		}
	}

	return 0;
}
