#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()
name = form.getvalue("name")
family = form.getvalue("family")

print """Content-type:text/html

"""
if name:
    print "Name: " + name
if family:
    print "Family: " + family

print """
<form method="post" action="page1.py">
<p>Birthdate</p>
<textarea name="birthdate" cols="40" rows="1"></textarea>
<p>Hobby</p>
<textarea name="hobby" cols="40" rows="1"></textarea>
<br/>
<input type="submit" value="Submit">
</form>"""
