#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the LED GPIO number
LED = 17

# Set the LED GPIO pin as an output
GPIO.setup(LED, GPIO.OUT)

# Turn the GPIO pin on
GPIO.output(LED,True)

# Wait 5 seconds
time.sleep(5)

# Turn the GPIO pin off
GPIO.output(LED,False)
