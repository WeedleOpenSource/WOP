
#include <wiringPi.h>
#include <stdio.h>

#define RelayPin      16

int main(void)
{
	if(wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	pinMode(RelayPin, OUTPUT);
	while(1)
	{
			digitalWrite(RelayPin, HIGH);
			delay(500);
			digitalWrite(RelayPin, LOW);
			delay(500);
	}

	return 0;
}
