#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()
value1=form.getvalue("first") #value1=form["first"].value
value2=form.getvalue("last")
print "Content-Type:text/html"
print
print "<html><head><title> Test URL encoding </title></head><body> Hello, my name is %s %s"%(value1,value2)
print "</body></html>"
