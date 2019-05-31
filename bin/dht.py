#!/usr/bin/python

import os
import sys
import time
import Adafruit_DHT

temperature_file = "/tmp/dht.temperature"
humidity_file    = "/tmp/dht.humidity"
run_file         = "/tmp/dht-run.pid"

sensor = Adafruit_DHT.AM2302
pin = 22

def write_runpid():
    pid = os.getpid()
    str = '{}'.format(pid)
    file = open(run_file, 'w')
    file.write(str)
    file.close()

def read_runpid():
    file = open(run_file, 'r')
    str = file.read()
    file.close()
    return str

if os.path.isfile(run_file):
    pid = read_runpid()
    exe = "/proc/{}/exe".format(pid)
    if os.path.isfile(exe):
        exit(0)

write_runpid()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None:
        file = open(humidity_file, 'w')
        str = '{0:0.1f}\n'.format(humidity)
        file.write(str)
        file.close()
    
    if temperature is not None:
        file = open(temperature_file, 'w')
        str = '{0:0.1f}\n'.format(temperature)
        file.write(str)
        file.close()

    time.sleep(1)
