#!/usr/bin/env python

import cgi
import cgitb

cgitb.enable()

print("Content-type: text/html\n\n")

form=cgi.FieldStorage()

if "language" not in form:
    print("<h1>No option chosen</h1>")
else:
    text=form["language"].value
    print("<h1>The option chosen was:</h1>")
    print(text)