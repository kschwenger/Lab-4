# reading data with json
import json
with open('Lab4pwm.txt', 'r') as f:
  data = json.load(f)
print("selected LED = " + str(data['selection']))
print("LED value = " + str(data['slider']))