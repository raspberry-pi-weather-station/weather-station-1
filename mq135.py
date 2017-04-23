# the sensor has to be connected to pin 1 for power, pin 6 for ground
# and pin 7 for signal(board numbering!).
 
import time, sys
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)
pin = 7
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
def action(pin):
    print('Sensor detected action!')
    return
 
GPIO.add_event_detect(pin, GPIO.RISING)
GPIO.add_event_callback(pin, action)
 
try:
    while True:
        print('alive')
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
