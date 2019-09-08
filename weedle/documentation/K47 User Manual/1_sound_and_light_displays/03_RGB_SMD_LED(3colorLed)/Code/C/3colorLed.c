#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>

typedef unsigned char uchar;

#define LedPinRed    16
#define LedPinGreen  1
#define LedPinBlue   0

void ledInit(void)
{
	softPwmCreate(LedPinRed,  0, 100);
	softPwmCreate(LedPinGreen,0, 100);
	softPwmCreate(LedPinBlue, 0, 100);
}

uchar map(uchar val, uchar in_min, uchar in_max, uchar out_min, uchar out_max)
{
	uchar tmp = 0;
	tmp = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
	
	return tmp;
}

void ledColorSet(uchar r_val, uchar g_val, uchar b_val)
{
	uchar R_val, G_val, B_val;
	R_val = map(r_val, 0, 255, 0, 100);
	G_val = map(g_val, 0, 255, 0, 100);
	B_val = map(b_val, 0, 255, 0, 100);
	
	softPwmWrite(LedPinRed,   R_val);
	softPwmWrite(LedPinGreen, G_val);
	softPwmWrite(LedPinBlue,  B_val);
}

int main(void)
{
	int i;

	if(wiringPiSetup() == -1)
	{ 
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	ledInit();
	while(1)
	{
		ledColorSet(0xff,0x00,0x00);   //red	
		delay(1000);
		ledColorSet(0x00,0xff,0x00);  //green 
		delay(1000);
		ledColorSet(0x00,0x00,0xff);  //Blue 
		delay(1000);
		ledColorSet(0xff,0xff,0x00);  //yellow 
		delay(1000);
		ledColorSet(0xff,0x00,0xff);  //Magenta  
		delay(1000);
		ledColorSet(0x00,0xff,0xff);  //Cyan
		delay(1000);
	}

	return 0;
}
