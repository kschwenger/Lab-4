#!/usr/bin/python37all
import cgi
import json

# get data from html form
dataFromhtml = cgi.FieldStorage()
selectedLED = dataFromhtml.getvalue('option')
LEDvalue = dataFromhtml.getvalue('slider')

# save data with json
data2send = {"selection":selectedLED, "slider":LEDvalue}
with open('Lab4pwm.txt', 'w') as f:
  json.dump(data2send,f)

# display updated page, resubmit form
print('Content-type: text/html\n\n')
print('<html>')

print("Previous selection: " + selectedLED + "at " + LEDvalue + '<br>')
print('<br>')

print('<form action="/cgi-bin/Lab4cgi.py" method="POST">')
print('<input type="radio" name="option" value="1"> LED 1 <br>')
print('<input type="radio" name="option" value="2"> LED 2 <br>')
print('<input type="radio" name="option" value="3"> LED 3 <br>')

print('<input type="range" name="slider" min ="0" max="100" value ="LEDvalue"/><br>')

print('<input type="submit" value="Submit">')
print('</form>')
print('</html>')