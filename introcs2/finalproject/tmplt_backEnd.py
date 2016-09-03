#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

"""
Team Blue - Alison Lee, Henry Zheng
IntroCS2 pd8
HW#56 -- Going Formal
2016-05-31
"""

import cgi
import cgitb
#cgitb.enable()  #diag info --- comment out once full functionality achieved
query = cgi.FieldStorage()

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def areaCGI():
    ans = ""
    perimeter = 0
    keys = query.keys()
    L = []
    for k in keys:
        perimeter += float(query[k].value)
        L += [float(query[k].value)]
    if len(L) != 3:
        return "ERR: Not a triangle"
    else:
        ans += "Perimeter = " + str(perimeter) + "<br>"
        semiperimeter = perimeter/2.0
        s = semiperimeter
        area = (s*(s-L[0])*(s-L[1])*(s-L[2]))**(1.0/2.0)
        ans += "Area = " + str(area)
        return ans
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title> Perimeter and Area of Triangle </title></head></html>\n"
htmlStr += "<body>"

# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
htmlStr += "<h3>Perimeter and Area</h3>"
htmlStr += "<h4>Data Input:</h4>"
htmlStr += str( FStoD() )
htmlStr += "<h4>Data Output:</h4>"
htmlStr += areaCGI()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

htmlStr += "</body></html>"


print htmlStr
