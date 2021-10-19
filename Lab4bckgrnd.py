import json
import RPi.GPIO as GPIO
import time

# establish leds
led1 = 13
led2 = 26
led3 = 20

# gpio set up
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # ignore warnings due to multiple scripts at same time
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

# create PWM objects @ 100 Hz for leds
pwm1 = GPIO.PWM(led1, 100)
pwm2 = GPIO.PWM(led2, 100)
pwm3 = GPIO.PWM(led3, 100)

try:
  while True:
    with open('Lab4pwm.txt', 'r') as f:
      data = json.load(f)
      print("selected LED = " + str(data['selection']))
      print("LED value = " + str(data['slider']))
except KeyboardInterrupt: # if user hits ctrl-C
  print('\nExiting')
except Exception as e: # catch all other errors
  print('\ne')