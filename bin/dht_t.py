#!/usr/bin/python

import os

temperature_file = "/tmp/dht.temperature"

if not os.path.isfile(temperature_file):
    print "0"
    exit(0)

file = open(temperature_file, 'r')
temp = file.read()
file.close()
print "{}".format(temp),
