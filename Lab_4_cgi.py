#!/usr/bin/python37all
import cgi    
print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
print("selection = " + data.getvalue("option"))
print("LEDslider = " + data.getvalue('slider') + '<br>')

# sending data with jsom 
import json
selectedLED = data.getvalue('selection')
LEDvalue = data.getvalue('LEDslider')
data = {"selection":selectedLED, "LEDslider":LEDvalue}
with open('LEDpwm.txt', 'w') as f:
json.dump(data,f)