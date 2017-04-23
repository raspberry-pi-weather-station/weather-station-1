import time
import json

data = {}
data['date'] = {}
date_time = time.ctime();
data['date']['pretty'] = date_time
data['date']['day'] = date_time.split(' ')[2]
data['date']['weekday'] = date_time.split(' ')[0]
data['date']['month'] = date_time.split(' ')[1]
data['date']['time'] = date_time.split(' ')[3]

# print(data['date']['pretty'])
# print(data['date']['day'])
# print(data['date']['month'])
# print(data['date']['weekday'])
# print(data['date']['time'])

data['temperature'] = 0
data['humidity'] = 0
data['pressure'] = 0
data['aqi'] = 0
data['altitude'] = 0
data['uvindex'] = 0

json_file = open('sensors.json', "w")
json_data = json.dumps(data)
json_file.write(json_data)
json_file.close()
