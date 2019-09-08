#include <wiringPi.h>
#include <stdio.h>

#define BtnPin    0
#define LedPin    4

int main(void)
{
	if(wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !\n");
		return -1; 
	}

	pinMode(BtnPin, INPUT);
	pinMode(LedPin, OUTPUT);

	while(1)
	{
		if(0 == digitalRead(BtnPin))
		{
			delay(10);
			if(0 == digitalRead(BtnPin)){
				while(!digitalRead(BtnPin));
				digitalWrite(LedPin, !digitalRead(LedPin));	
				printf("Button is pressed\n");	
			}
		}
	}

	return 0;
}
