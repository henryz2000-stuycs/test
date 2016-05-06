#!/usr/bin/python
print "Content-type:text/html\n"
print ""
print "<html>"
print "<style>"
print "pre {font-size: 150%; letter-spacing: 2px; text-align: center; line-height: 2; margin-top:250}"
print "</style>"

import random

punc = ["'","!","@","#","$","%","^","&",'"',"*","-","+","=","~"]

def face():
    print "<pre>"
    print " " + 5*(punc[random.randrange(len(punc))] + " ")
    print "   " + 2*(punc[random.randrange(len(punc))] + "   ")
    print 4*punc[random.randrange(len(punc))]
    print "</pre>"

print "</html>"
face()
