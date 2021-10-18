#!/usr/bin/python37all
import cgi    
print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
print("selection = " + data.getvalue("option") + '<br>')
print("LEDslider = " + data.getvalue('slider') + '<br>')

print("""
<html> 
<form action="/cgi-bin/Lab4cgi.py" method="POST">
  <input type="radio" name="option" value="1" checked> LED 1 <br>
  <input type="radio" name="option" value="2"> LED 2 <br>
  <input type="radio" name="option" value="3"> LED 3 <br>
  <input type="range" name="slider" min ="0" max="100" value ="50"/><br>
  <input type="submit" value="Submit">
</form>
</html>
""")


# sending data with jsom 
import json
selectedLED = data.getvalue('selection')
LEDvalue = data.getvalue('LEDslider')
data = {"selection":selectedLED, "LEDslider":LEDvalue}
with open('Lab4pwm.txt', 'w') as f:
json.dump(data,f)
