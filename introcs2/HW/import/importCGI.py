#!/usr/bin/python
print "Content-type:text/html\n\n"

"""
Henry Zheng
IntroCS2 pd8
HW#53 -- GET Some Computation Done
2016-05-25
"""

import cgi
import cgitb
cgitb.enable()
query = cgi.FieldStorage()
'''
print query
print query.keys()

for k in query.keys():
    print k + " : " + query[k].value
'''

def areaCGI():
    perimeter = 0
    keys = query.keys()
    L = []
    for k in keys:
        perimeter += float(query[k].value)
        L += [float(query[k].value)]
    print "Perimeter = " + str(perimeter) + "<br>"
    semiperimeter = perimeter/2.0
    s = semiperimeter
    area = (s*(s-L[0])*(s-L[1])*(s-L[2]))**(1.0/2.0)
    print "Area = " + str(area)

areaCGI()
'''
def area():
    query = query.split('&')
    if len(query) != 3:
        print "ERR: Not a triangle"
    for sidelength in query:
        sidelength = sidelength.split("=")
        if sidelength[0] == "a":
            a = float(sidelength[1])
        if sidelength[0] == "b":
            b = float(sidelength[1])
        if sidelength[0] == "c":
            c = float(sidelength[1])
    perimeter = a+b+c
    print "Perimeter = " + str(perimeter) + "<br>"
    semiperimeter = perimeter/2.0
    s = semiperimeter
    area = (s*(s-a)*(s-b)*(s-c))**(1.0/2.0)
    print "Area = " + str(area)
    
area()
'''

