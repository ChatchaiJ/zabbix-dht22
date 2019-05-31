#!/usr/bin/python

import os

os.environ['PYTHON_EGG_CACHE'] = '/tmp/python-eggs' 

import sys
import Adafruit_DHT

sensor = Adafruit_DHT.AM2302
pin = 22
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and humidity < 100:
    print('{0:0.1f}'.format(humidity))
