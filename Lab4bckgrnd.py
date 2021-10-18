# reading data with jsom ahhhh
import json
with open('Lab4pwm.txt', 'r') as f:
data = json.load(f)
print("selected LED = " + str(data['selection']))
print("LED value = " + str(data['LEDslider']))