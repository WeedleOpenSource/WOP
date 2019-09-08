#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>

#define  BUFSIZE  128

char Buff[256] = {0};

char* get_ds18b20_id(char *DirName)
{
	DIR *dirp = NULL;
	struct dirent *Filep = NULL;
	
	dirp = opendir(DirName);
	while(1)
	{
		Filep = readdir(dirp);
		strcpy(Buff, Filep->d_name);
		if(!strncmp(Buff, "28-", 3))
		{	
			return Buff;
		}		
	}
	
}

int main(void)
{
	float temp;
	int i, j, fd, ret;

	char buf[BUFSIZE];
	char tempBuf[5];
	char fileName[256] = {0};
	char Dir[256] = "/sys/bus/w1/devices/";
	char *ds18b20_id = NULL;
	
	ds18b20_id = get_ds18b20_id(Dir);
	strcpy(fileName, Dir);
	strcat(fileName, ds18b20_id);
	strcat(fileName, "/w1_slave");
	printf("filename is %s\n", fileName);
	while(1)
	{
		if((fd = open(fileName, O_RDONLY)) == -1)
		{
			perror("open device file error");
			return -1;
		}
		while(1)
		{
			ret = read(fd, buf, BUFSIZE);
			if(0 == ret)
			{
				break;	
			}
			if(-1 == ret)
			{
				if(errno == EINTR)
				{
					continue;	
				}
				perror("read()");
				close(fd);
				return -1;
			}
		}
		for(i=0;i<sizeof(buf);i++)
		{
			if(buf[i] == 't')
			{
				for(j=0;j<sizeof(tempBuf);j++)
				{
					tempBuf[j] = buf[i+2+j]; 	
				}
			}	
		}

		temp = (float)atoi(tempBuf) / 1000;

		printf("%.3f C\n",temp);
		
		sleep(1);
	
		close(fd);
	}

	return 0;
}
