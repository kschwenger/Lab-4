#!/usr/bin/python37all
import cgi    
print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
print("selection = " + data.getvalue("option") + '<br>')
print("LEDslider = " + data.getvalue('slider') + '<br>')

"""
# sending data with jsom 
import json
selectedLED = data.getvalue('selection')
LEDvalue = data.getvalue('LEDslider')
data = {"selection":selectedLED, "LEDslider":LEDvalue}
with open('Lab4pwm.txt', 'w') as f:
json.dump(data,f)
"""