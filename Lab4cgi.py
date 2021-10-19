#!/usr/bin/python37all
import cgi
import json

# get data from html form
dataFromhtml = cgi.FieldStorage()
selectedLED = dataFromhtml.getvalue('option')
LEDvalue = dataFromhtml.getvalue('slider')

# save data for background code with json
data2send = {"selection":selectedLED, "slider":LEDvalue}
with open('Lab4pwm.txt', 'w') as f:
  json.dump(data2send,f)

# display updated page with most recent selection, resubmit form 
print('Content-type: text/html\n\n')
print('<html>')

print('Previous selection: Led ' + selectedLED + ' at a brightness of ' + LEDvalue + '%' + '<br>')
print('<br>')

# present radio options to pick LED for control
print('Choose LED' + '<br>')
print('<form action="/cgi-bin/Lab4cgi.py" method="POST">')
print('<input type="radio" name="option" value="1"> LED 1 <br>')
print('<input type="radio" name="option" value="2"> LED 2 <br>')
print('<input type="radio" name="option" value="3"> LED 3 <br>')
print('<br>')

# present slider to change brightness of chosen LED
print('Change brightness of chosen LED' + '<br>')
print('0% <input type="range" name="slider" min ="0" max="100" value ="LEDvalue"/> 100% <br>')
print('<br>')

# submit selections
print('<input type="submit" value="Submit">')
print('</form>')
print('</html>')