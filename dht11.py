#!/usr/bin/python
import Adafruit_DHT
import json

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

json_file = open('sensors.json','r')
file_contents = json_file.read()
json_data = json.loads(file_contents)

json_data['temperature'] = temperature
json_data['humidity'] = humidity
json_file.close()

data = json.dumps(json_data)
json_file = open('sensors.json', 'w')
json_file.write(data)
json_file.close()
