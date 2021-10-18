#!/usr/bin/python37all
import cgi
data = cgi.FieldStorage()
selectedLED = data.getvalue('option')
LEDvalue = data.getvalue('slider')

print('Content-type: text/html\n\n')
print('<html>')

print('<form action="/cgi-bin/Lab4cgi.py" method="POST">')
print('<input type="radio" name="option" value="LED 1"> LED 1 <br>')
print('<input type="radio" name="option" value="LED 2"> LED 2 <br>')
print('<input type="radio" name="option" value="LED 3"> LED 3 <br>')

print('<input type="range" name="slider" min ="0" max="100" value ="LEDvalue"/><br>')

print("selection = " + selectedLED + '<br>')
print("LEDslider = " + LEDvalue + '<br>')