import json
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