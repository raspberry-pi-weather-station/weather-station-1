import Adafruit_BMP.BMP085 as BMP085
import json

sensor = BMP085.BMP085()
pressure = sensor.read_pressure()
alt=float(sensor.read_altitude())
slp=float(sensor.read_sealevel_pressure())

json_file = open('sensors.json','r')
file_contents = json_file.read()
json_data = json.loads(file_contents)

json_data['pressure'] = pressure
json_data['altitude'] = alt
json_data['slp'] = slp
json_file.close()

data = json.dumps(json_data)
json_file = open('sensors.json', 'w')
json_file.write(data)
json_file.close()