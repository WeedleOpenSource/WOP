
#include <wiringPi.h>
#include <stdio.h>

#define KnockPin      0
#define LedPin        4

int knockPinValue = -1;

int main(void)
{
	int knockValue = -1;
	if(wiringPiSetup() == -1)
	{ 
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	pinMode(KnockPin, INPUT);
	pinMode(LedPin,  OUTPUT);

	while(1)
	{
		knockValue = digitalRead(knockPin);
		knockPinValue = knockValue;
		delay(6);
		
		knockValue = digitalRead(knockPin);
		if(knockPinValue != knockValue)
		{
			printf("Detected knocking!\n");
			digitalWrite(LedPin, !digitalRead(LedPin));  	
		}	
	}
	return 0;
}

