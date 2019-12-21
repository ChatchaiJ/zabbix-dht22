# Raspberry Pi's DHT22 Monitoring via Zabbix

Try to fix zabbix agent "item ... failed: first network error, wait for 15 seconds"

## Problem

Using Adafruit's DHT library on RaspberryPi to read temperature and humidity from
DHT22 could be delayed and cause zabbix agent to timeout. This cause zabbix server
to stop reading all others value it supposed to read. So instead of let that happen,
the value of temperature and humidity will be read by the 'daemon' dht.py instead
and store those values to files. Zabbix agent will get last valid values from those
files instead get them directly from sensor. This might return invalid temperature
and humidity back, but since both of these are unlikely to change rapidly, this
should not much a problem.

## Prerequsites
* python 2
* Adafruit DHT22 library

## Installing
* put zabbix\_conf/dht.conf in /etc/zabbix/zabbix\_agentd.conf.d
* bin/{dht.py,dht\_h.py,dht\_t.py} to /home/pi/bin
* add "0 * * * * /home/pi/bin/dht.py" to crontab
* restart zabbix\_agentd

## Author
* Chatchai Jantaraprim (https://github.com/chatchaij)

## License
This project is licensed under the MIT License
