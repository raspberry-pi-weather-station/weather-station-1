#!/usr/bin/python
import Adafruit_DHT
import json
import time
import os

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

os.system('touch /home/pi/weather_station/weather-station-1/.lock')
json_file = open('/home/pi/weather_station/weather-station-1/sensors.json','r')
file_contents = json_file.read()
json_data = json.loads(file_contents)

json_data['temperature'] = temperature
json_data['humidity'] = humidity
date_time = time.ctime();
json_data['date']['pretty'] = date_time
json_data['date']['day'] = date_time.split(' ')[2]
json_data['date']['weekday'] = date_time.split(' ')[0]
json_data['date']['month'] = date_time.split(' ')[1]
json_data['date']['time'] = date_time.split(' ')[3]
json_file.close()

data = json.dumps(json_data)
json_file = open('sensors.json', 'w')
json_file.write(data)
json_file.close()
print "Temperature data written"
os.system('rm /home/pi/weather_station/weather-station-1/.lock')
exit(0)
