# GPIO library for developing GPIO commands in Raspberry Pi programming
import RPi.GPIO as GPIO 
# Time library to develop time commands in Raspberry Pi programming
import time

# to use Raspberry Pi BCM pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO input channel 
# Automation Expansion Board Inputs: BCM13, BCM19, BCM26
GPIO.setup(26, GPIO.IN)

# 

try: 
	while True:
		if GPIO.input(26):
			GPIO.output(17,GPIO.HIGH)
        else
        