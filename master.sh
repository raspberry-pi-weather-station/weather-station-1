#!/bin/bash

python /home/pi/weather_station/weather-station-1/display.py &
while true 
do
	python /home/pi/weather_station/weather-station-1/dht11.py
	python /home/pi/weather_station/weather-station-1/bmp.py
	python /home/pi/weather_station/weather-station-1/wunderground_api.py
	sleep 5
done
