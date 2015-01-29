#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()
birthdate = form.getvalue("birthdate")
hobby = form.getvalue("hobby")

print """Content-type:text/html

"""
if birthdate:
    print "Birthdate: " + birthdate
if hobby:
    print "Hobby: " + hobby

print """
<form method="post" action="page2.py">
<p>Name</p>
<textarea name="name" cols="40" rows="1"></textarea>
<p>Family</p>
<textarea name="family" cols="40" rows="1"></textarea>
<br/>
<input type="submit" value="Submit">
</form>"""
