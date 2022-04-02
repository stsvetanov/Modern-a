#!/usr/bin/env python

import cgi
import cgitb
import os

cgitb.enable()

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()

if "post" not in form:
    print("<h1>The text area was empty.</h1>")
else:
    text = form["post"].value
    print("<h1>Text from text area:</h1>")
    # result = os.system(f"python hi.py")
    # print(result)
    print(cgi.escape(text))