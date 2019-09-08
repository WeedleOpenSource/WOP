
#include <wiringPi.h>
#include <stdio.h>

typedef unsigned char uchar;
typedef unsigned int uint;

#define     ADC_CS    0
#define     ADC_CLK   1
#define     ADC_DIO   2
#define  JoyStick_Button  3

#define UP			1
#define DOWN		2
#define LEFT   	 	1
#define RIGHT		2



uchar get_ADC_Result(uchar xyVal)
{
	uchar i;
	uchar dat1=0, dat2=0;

	digitalWrite(ADC_CS, 0);

	digitalWrite(ADC_CLK,0);
	digitalWrite(ADC_DIO,1);	delayMicroseconds(2);
	digitalWrite(ADC_CLK,1);	delayMicroseconds(2);
	digitalWrite(ADC_CLK,0);

	digitalWrite(ADC_DIO,1);    delayMicroseconds(2); 
	digitalWrite(ADC_CLK,1);	delayMicroseconds(2);
	digitalWrite(ADC_CLK,0);

	if(xyVal == 'x'){
		digitalWrite(ADC_DIO,0);	delayMicroseconds(2); 
	}
	if(xyVal == 'y'){
		digitalWrite(ADC_DIO,1);	delayMicroseconds(2); 
	}
	digitalWrite(ADC_CLK,1);	
	digitalWrite(ADC_DIO,1);    delayMicroseconds(2);
	digitalWrite(ADC_CLK,0);	
	digitalWrite(ADC_DIO,1);    delayMicroseconds(2);
	
	for(i=0;i<8;i++)
	{
		digitalWrite(ADC_CLK,1);	delayMicroseconds(2);
		digitalWrite(ADC_CLK,0);    delayMicroseconds(2);

		pinMode(ADC_DIO, INPUT);
		dat1=dat1<<1 | digitalRead(ADC_DIO);
	}
	
	for(i=0;i<8;i++)
	{
		dat2 = dat2 | ((uchar)(digitalRead(ADC_DIO))<<i);
		digitalWrite(ADC_CLK,1); 	delayMicroseconds(2);
		digitalWrite(ADC_CLK,0);    delayMicroseconds(2);
	}

	digitalWrite(ADC_CS,1);

	pinMode(ADC_DIO, OUTPUT);
	
	return(dat1==dat2) ? dat1 : 0;
}

int main(void)
{
	uchar xFlag, yFlag;
	uchar xVal = 0, yVal = 0, bVal = 0;

	if(wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !");
		return -1; 
	}

	pinMode(ADC_CS,  OUTPUT);
	pinMode(ADC_CLK, OUTPUT);
	pinMode(JoyStick_Button, INPUT);

	pullUpDnControl(JoyStick_Button, PUD_UP);

	while(1)
	{
		xFlag = 0;
		yFlag = 0;
		xVal = get_ADC_Result('x');
		if(xVal == 0)
		{
			xFlag = UP; //up	
		}
		if(xVal == 255)
		{
			xFlag = DOWN; //down
		}

		yVal = get_ADC_Result('y');
		if(yVal == 0)
		{
			yFlag = LEFT; //left
		}
		if(yVal == 255)
		{
			yFlag = RIGHT; //right
		}

		bVal = digitalRead(JoyStick_Button);
		if(bVal == 0)
		{
			printf("Button is pressed !\n");
		}
		
		switch(xFlag)
		{
			case UP: 
				printf("up\n"); 
				break;
			case DOWN: 
				printf("down\n"); 
				break;
			default:
				break;
		}
		
		switch(yFlag)
		{
			case LEFT: 
				printf("left\n"); 
				break;
			case RIGHT: 
				printf("right\n"); 
				break;
			default:
				break;
		}
		delay(200);
	}

	return 0;
}
