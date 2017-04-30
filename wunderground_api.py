import requests
import json

# get the response from the website in terms of the page
page = requests.get('http://api.wunderground.com/api/ff746853c458d7e8/forecast/q/IN/Bangalore.json')

# parse the json page to dictionary
parsed = json.loads(page.text)

# extracting only useful information from the parsed and stripping the rest
parsed = parsed['forecast']['simpleforecast']['forecastday']

# making a new empty dixtionary to store the information (using only metric notations)
data = {}


day_list = ['today','day+1','day+2','day+3']

i = 0
for day in day_list :
    data[day] = {} # to make a nested dictionary
    data[day]['temperature'] = parsed[i]['high']
    data[day]['humidity'] = parsed[i]['avehumidity'] # Average Humidity
    data[day]['pop'] = parsed[i]['pop'] # probability of precipitation
    data[day]['condition'] = parsed[i]['conditions']
    data[day]['wind'] = {}
    data[day]['wind']['speed'] = parsed[i]['avewind']['kph'] # Wind speed in kmph
    data[day]['wind']['dir'] = parsed[i]['avewind']['dir'] # Wind direction
    data[day]['qpf'] = parsed[i]['qpf_allday'] # measure of rain

    # Day and date information of the collection
    data[day]['date'] = {}
    data[day]['date']['day'] = parsed[i]['date']['day']
    data[day]['date']['month'] = parsed[i]['date']['month']
    data[day]['date']['monthname'] = parsed[i]['date']['monthname']
    data[day]['date']['pretty'] = parsed[i]['date']['pretty']
    data[day]['date']['yday'] = parsed[i]['date']['yday']
    data[day]['date']['weekday'] = parsed[i]['date']['weekday']

    i = i + 1

file_data = json.dumps(data)
path = '/home/pi/weather_station/weather-station-1/wunderground.json'
output_file = open(path, 'w')
output_file.write(file_data)
output_file.close()
