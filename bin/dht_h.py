#!/usr/bin/python

import os

humidity_file = "/tmp/dht.humidity"

if not os.path.isfile(humidity_file):
    print "0"
    exit(0)

file = open(humidity_file, 'r')
humid = file.read()
file.close()
print "{}".format(humid),
