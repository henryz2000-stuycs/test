#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

"""
Team Public Relations - Gilvir Gill, Henry Zheng
IntroCS2 pd8
FINAL PROJECT
END OF SEMESTER
"""

import math
import cgi
import cgitb
import urllib2
from xml.etree import ElementTree as ET
#import googlemaps
#from datetime import datetime
cgitb.enable()  #diag info --- comment out once full functionality achieved
query = cgi.FieldStorage()
#gmaps = googlemaps.Client(key='AIzaSyD7g6o2aIIo3ZlXtYbc4LjhcUaRizS1DKU')
#google maps is hereby referred to as gmaps



# ~~~~~~~~~~~~~~~ Settings ~~~~~~~~~~~~~~~ #
printed_info = ['SSID', 'Location', 'City', 'Type', 'Provider', 'Location_T', 'Remarks']

def ulElements(D): #returns an unordered html list of info from the dictionary using the settings in printed_info global
    html = '<ul> \n'
    for infotype in printed_info:
        html += '<li>%s: %s</li> \n' % (infotype, D[infotype])
    html += '</ul>'
    return html

    


# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~


def getCoords():  #returns the map of the latitude/longitude of the user inputted address so far
    #keys = query.keys()
    #address = query["address"].value  #gets the address value
    #address = address.replace(' ',"+")  #replaces spaces in user inputted address value with +'s in order to comply with gmap's API
    url="https://maps.googleapis.com/maps/api/geocode/xml?address=%s" % address  #geocodes the address
    response = urllib2.urlopen(url)
    latlong = response.read()
    return latlong
    #latlong = latlong.strip()
    #lat = (ET.fromstring(latlong).find('result/geometry/location/lat')).text  #retrieves the latitude from the xml parse
    #lng = (ET.fromstring(latlong).find('result/geometry/location/lng')).text  #retrieves the longitude from the xml parse
    #return {'Long_': lng, 'Lat': lat}


print getCoords()
