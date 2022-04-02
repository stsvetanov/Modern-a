#!/usr/bin/env python3

from analysis import calculate
import cgi
import cgitb
cgitb.enable()

input_data = cgi.FieldStorage()

print('Content-Type: text/html') # HTML is following
print()                         # Leave a blank line
print('<h1>Addition Results</h1>')
try:
  area = int(input_data["area"].value)
except:
  print('<output>Sorry, the script cannot turn your inputs into numbers (integers).</output>')
  raise SystemExit(1)

result = calculate(area)
print(f'<output>Predicted price for house with area {area} is {result}</output>')