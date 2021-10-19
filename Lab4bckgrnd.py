import json
import RPi.GPIO as GPIO
import time

# establish leds
led1 = 13
led2 = 26
led3 = 20

# gpio set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

# create PWM objects @ 100 Hz for leds
pwm1 = gpio.PWM(led1, 100)
pwm2 = gpio.PWM(led2, 100)
pwm3 = gpio.PWM(led3, 100)

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