from twilio.rest import TwilioRestClient
import urllib.request
import json
import time
from pprint import pprint as pp

with open('wunderground.json') as wun:
	data = json.load(wun)

weather = 1

date = str(data['today']['date']['pretty'])
cond = str(data['today']['condition'])
temp = int(data['today']['temperature']['celsius'])
hum = int(data['today']['humidity'])
pop = int(data['today']['pop'])
qpf = int(data['today']['qpf']['in'])
wind_sp = int(data['today']['wind']['speed'])
wind_dir = str(data['today']['wind']['dir'])

while weather == 1:
	time.sleep(10)
	client = TwilioRestClient("AC38fb196a9ebf859f7b074ae33f2dfbbf", "75f58d9e614232d3506fbfd4975e62ab")
	client.messages.create(to="+918770969372", from_="+18572642104", body = "DATE: "+date+"Condition: "+cond+"Temperature: "+str(temp)+"Humidity: "+str(hum)+"Wind speed: "+str(wind_sp)+"Wind direction: "+wind_dir+"Probablity of Precipitation:"+str(pop)+"Rainfall measured in inches:"+str(qpf)+ "message delivered from python script made by team WEATHER_STATION")
