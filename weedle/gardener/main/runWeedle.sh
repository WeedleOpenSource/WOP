#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

/home/pi/weedle/gardener/main/main.py >> /home/pi/weedle/gardener/main/logs/runWeedle$DATE.log 2>&1
