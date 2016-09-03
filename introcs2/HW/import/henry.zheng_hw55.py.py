#!/usr/bin/python
print "Content-Type:text/html\n"
print ""

# Team Blue - Henry Zheng & Alison Lee
# IntroCS2 pd8
# HW55 -- Clever Genii, Inc.
# 2016-05-26

"""
0. The variable keys stores the list containing the side length variables (a, b, c)
1. The perimeter of the triangle is calculated by adding all the values that
   correspond to each element in keys
2. The values (side lengths) are stored in another list and they are used in
   Heron's formula
"""

import cgi
# import cgitb
# cgitb.enable()
query = cgi.FieldStorage()

def areaCGI() :
    perimeter = 0
    keys = query.keys()
    L = [ ]
    for k in keys:
        perimeter += float( query[ k ].value )
        L += [ float( query[ k ].value ) ]
    print "Perimeter = " + str( perimeter ) + "<br>"
    semiperimeter = perimeter / 2.0
    s = semiperimeter
    area = ( s * ( s - L[ 0 ] ) * ( s - L[ 1 ] ) * ( s - L[ 2 ] )) ** ( 1.0 / 2.$
    print "Area = " + str( area )

areaCGI()


