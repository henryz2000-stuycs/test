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
import json
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
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
def getCoords():  #returns the map of the latitude/longitude of the user inputted address so far
    #keys = query.keys()
    #address = query["address"].value  #gets the address value
    #address = address.replace(' ',"+")  #replaces spaces in user inputted address value with +'s in order to comply with gmap's API
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyD7g6o2aIIo3ZlXtYbc4LjhcUaRizS1DKU" % address  #geocodes the address
    response = urllib2.urlopen(url)
    info = response.read() #these past few lines basically assign a json formatted file from google api to info
    info = json.loads(info)
    #lat = info["results"][0]['geometry']['location']['lat']
    #lng = info["results"][0]['geometry']['location']['lng']
    #return {'Long_': lng, 'Lat': lat}
    addressL = []
    for addresses in info["results"]:
        components = addresses["address_components"]
        fullAddress = ""
        for element in components:
            fullAddress += components[element]["long_name"] + " "
        addressL += fullAddress
    return addressL

print getCoords()
