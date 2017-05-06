import json
import Adafruit_CharLCD as LCD
import time
from datetime import datetime
import os

def clearLCD():
	lcd.message("                \n")
	lcd.message("                \n")

lcd_rs=25
lcd_en=24
lcd_d4=23
lcd_d5=17
lcd_d6=18
lcd_d7=22
lcd_backlight=4
lcd_columns=16
lcd_rows=2

lcd=LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows,lcd_backlight)

delay_time = 3

while True :
	lock_file = '/home/pi/weather_station/weather-station-1/.lock'

	if(not(os.path.isfile(lock_file))):
		json_file = open('/home/pi/weather_station/weather-station-1/sensors.json', 'r')
		json_data = json_file.read()
		data = json.loads(json_data)

		lcd.message('Time=' + data['date']['time'] + "\n")
		# lcd.message('Time=' + time.ctime())
		lcd.message(str('\nTemp={0:0.2f}*C\n'.format(data['temperature'])))

		time.sleep(delay_time)
		lcd.clear();
		lcd.message('Time=' + data['date']['time'] + "\n")
		lcd.message(str('\nHum={0:0.2f}%\n'.format(data['humidity'])))
	
		time.sleep(delay_time)
		lcd.clear();
		lcd.message('Time=' + data['date']['time'] + "\n")
		lcd.message(str('\nSLP={0:0.2f}Pa\n'.format(data['slp'])))
	
		time.sleep(delay_time)
		lcd.clear();
		lcd.message('Time=' + data['date']['time'] + "\n")
		lcd.message(str('\nPress={0:0.2f}Pa\n'.format(data['pressure'])))
	
		time.sleep(delay_time)
		lcd.clear();
		lcd.message('Time=' + data['date']['time'] + "\n")
		lcd.message(str('\nAlt={0:0.2f}\n'.format(data['altitude'])))
		time.sleep(delay_time)
		lcd.clear();
		json_file.close()

exit(0)
