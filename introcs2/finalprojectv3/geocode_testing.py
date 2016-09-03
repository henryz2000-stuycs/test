#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

"""
Team Blue - Alison Lee, Henry Zheng
IntroCS2 pd8
HW#57 -- Formal Textification
2016-05-31
"""

import cgi
import cgitb
import urllib2
#import googlemaps
#from datetime import datetime
cgitb.enable()  #diag info --- comment out once full functionality achieved
query = cgi.FieldStorage()
#gmaps = googlemaps.Client(key='AIzaSyD7g6o2aIIo3ZlXtYbc4LjhcUaRizS1DKU')

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~


def areaCGI():
#    ans = ""
#    perimeter = 0
    #geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    #return geocode_resule
    address = "345 chambers st,new york, ny 10282"
    url="https://maps.googleapis.com/maps/api/geocode/xml?address=%s" % address
    response = urllib2.urlopen(url)
    latlong = response.read()
    return latlong
    maps = '''
<iframe
  width="900"
  height="500"
  frameborder="0" style="border:0"
  src="https://www.google.com/maps/embed/v1/place?key=AIzaSyDq-niy82jWRr3FZj3BE7FpyLiIeoLtO6w
&q='''+to1+'''"allowfullscreen>
</iframe>
'''
    return maps
#    return text
#    return keys
    #L = []
    #for k in keys:
        
#        perimeter += float(query[k].value)
#        L += [float(query[k].value)]
#    if len(L) != 3:
#        return "ERR: Not a triangle"
#    else:
#        ans += "Perimeter = " + str(perimeter) + "<br>"
#        semiperimeter = perimeter/2.0
#        s = semiperimeter
#        area = (s*(s-L[0])*(s-L[1])*(s-L[2]))**(1.0/2.0)
#        ans += "Area = " + str(area)
#        return ans
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title> Formal Textification </title></head></html>\n"
htmlStr += "<body><center>"

# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
htmlStr += "<h3>Formal Textification</h3>"
htmlStr += "<h4>Data Input:</h4>"
htmlStr += "<h4>Data Output:</h4>"
htmlStr += areaCGI()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

htmlStr += "</center></body></html>"


print htmlStr
