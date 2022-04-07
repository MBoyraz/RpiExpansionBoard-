#GPIO library for developing GPIO commands in Raspberry Pi programming
import RPi.GPIO as GPIO 
#Time library to develop time commands in Raspberry Pi programming
import time

# to use Raspberry Pi BCM pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(17, GPIO.OUT)

# blink GPIO17 5 times
for i in range(0,5):
	blink(17)


def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(2)
	return

GPIO.cleanup()