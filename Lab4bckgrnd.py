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

# start duty cycles at 0
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

# continually run 
while True:
  # open saved json data from cgi code
  with open('Lab4pwm.txt', 'r') as f:
    data = json.load(f)

  # if the selection is LED 1, change the duty cycle to chosen slider value for LED 1
  if int(data['selection']) == 1:
    pwm1.ChangeDutyCycle(int(data['slider']))
    time.sleep(0.1)
  # if the selection is LED 2, change the duty cycle to chosen slider value for LED 2
  elif int(data['selection']) == 2:
    pwm2.ChangeDutyCycle(int(data['slider']))
    time.sleep(0.1)
  # if the selection is LED 3, change the duty cycle to chosen slider value for LED 3
  elif int(data['selection']) == 3:
    pwm3.ChangeDutyCycle(int(data['slider']))
    time.sleep(0.1)

GPIO.cleanup() # Clean up