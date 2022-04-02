#!/usr/bin/env python

import cgi
import cgitb
from weather_service import get_weather

cgitb.enable()

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()

if "post" not in form:
    print("<h1>The text area was empty.</h1>")
else:
    location = form["post"].value
    weather = get_weather(location)
    print(f"<h2>The weather in {location} is {weather}</h2>")