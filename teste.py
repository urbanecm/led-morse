#!/usr/bin/env python

import RPi.GPIO as  GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

GPIO.output(21, False)
time.sleep(60)
GPIO.output(21, True)
