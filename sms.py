from twilio.rest import TwilioRestClient
import urllib.request
import json
import time
from pprint import pprint as pp

with open('wunderground.json') as wun:
	data = json.load(wun)

weather = 1

date = str(data['date']['pretty'])
# cond = str(data['today']['condition'])
temp = str(data['temperature'])
hum = str(data['humidity'])
# pop = int(data['today']['pop'])
# qpf = int(data['today']['qpf']['in'])
# wind_sp = int(data['today']['wind']['speed'])
# wind_dir = str(data['today']['wind']['dir'])
pressure = str(data['pressure'])
slp = str(data['slp'])
altitude = str(data['altitude'])

while weather == 1:
	time.sleep(10)
	client = TwilioRestClient("AC38fb196a9ebf859f7b074ae33f2dfbbf", "75f58d9e614232d3506fbfd4975e62ab")
	client.messages.create(to="+919611519000", from_="+18572642104", body = "DATE: "+date+"Temperature: "+str(temp)+"Humidity: "+str(hum)+"Pressure:"+pressure+"Sea level pressure:"+slp+"Altitude:"+altitude+"message delivered from python script made by team WEATHER_STATION")
