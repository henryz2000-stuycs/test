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
    keys = query.keys()
    address = query["address"].value  #gets the address value
    address = address.replace(' ',"+")  #replaces spaces in user inputted address value with +'s in order to comply with gmap's API
    url="https://maps.googleapis.com/maps/api/geocode/xml?address=%s" % address  #geocodes the address
    response = urllib2.urlopen(url)
    latlong = response.read()
    latlong = latlong.strip()
    lat = ET.fromstring(latlong).find('result/geometry/location/lat')  #retrieves the latitude from the xml parse
    lng = ET.fromstring(latlong).find('result/geometry/location/lng')  #retrieves the longitude from the xml parse
    return {'Long': lng, 'Lat': lat}




def getMap(lat,lng):
    coord = str(lat) + ',' + str(lng)  #combines the two into a latitude,longitude pair
    maps = '''
<iframe
  width="900"
  height="500"
  frameborder="0" style="border:0"
  src="https://www.google.com/maps/embed/v1/place?key=AIzaSyDq-niy82jWRr3FZj3BE7FpyLiIeoLtO6w
&q='''+coord+'''"allowfullscreen>
</iframe>
'''  #embeds the map within the website of the latitude,longitude pair
    return maps


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






# ========= DATAPROCCESSING FUNCTIONS  =========== #
def readL(filename):
    inStream = open(filename,'r')
    data = inStream.readlines()
    inStream.close()
    return data

def quickLinePatch(lines):
    newlines = [lines[0]]
    for num in range(1,len(lines),2): #for lines 1,3,5,etc.
        newlines.append(lines[num]+lines[num+1])
    return newlines
#Turns data into a 2D list.
def ListGen(lines):
    list = []
    for line in lines:
        line = line.replace('""', "15NfzYl2Yw") #replace double quotes which reprsent quotation marks within a quote  with a string
        line = line.split('"') #split every line into parts with and without quotes, then loop through those blocks in the next part:
        counter = 0
        newline = []
        for quote_block in line:
            if counter % 2 == 0: #if it is outside of a quotation mark:
                if quote_block == ',':
                    quote_block = "L4hkE0NNLY"
                if quote_block != '' and quote_block[-1] == ',' and quote_block != ',': #if it ends or starts with a comma remove the comma
                    quote_block = quote_block[:-1]
                if quote_block != '' and quote_block[0] == ',' and quote_block != ',':
                    quote_block = quote_block[1:]
                quote_block = quote_block.split(',') #split it into columns based on commas
            else:
                quote_block = quote_block.replace("15NfzYl2Yw", '""')
                quote_block = [quote_block] #else if it's a quote just add it in the list to append to.
            for column_item in quote_block:
                if column_item != "L4hkE0NNLY":
                    newline.append(column_item)
            counter += 1
        list.append(newline[:-1]) #append all but the last element, which is just a newline anyways
    return list
# takes 2D list and turns into a list of dictionaries

def ListToDict(L):
    #define an empty dictionary to be populated
    D = {}
    for row in L[1:]: #for every row after the header row:
        D[row[0]] = {}
        for num in range(1,len(L[0])): #for every element in the header row except the first one:
            (D[row[0]])[L[0][num]] = row[num]
    return D


def distance(sx,sy,ex,ey): #gives the distance between two points using the haversine formula
    lateral_distance = sx-ex
    longitudal_distance = sy-ey
    a = math.sin(math.radians(lateral_distance/2))**2 + math.cos(math.radians(sx)) * math.cos(math.radians(ex)) * math.sin(math.radians(longitudal_distance/2))**2
    c = 2 * math.atan2((a**0.5 ),(1-a**0.5))
    d = 3959 * c
    return d
#adds distance to starting point to all elements of the dictionary
def addDist(dict,sx,sy):
    for hotspot in dict:
        lati = dict[hotspot]['Lat']
        longi = dict[hotspot]['Long_']
        #print lati
        #print longi
        dict[hotspot]['Distance'] = distance(sx,sy,float(lati),float(longi))



def minDist(D): #returns the key of the dictionary element with the lowest "Distance" value
    objects = D.keys()
    values = D.values()
    distances = [] #list of distances parallel to the values and objects
    for dct in values:
        distances.append(float(dct['Distance']))
    return objects[(distances.index(min(distances)))] #return the object id of the object with the lowest distance value

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

data = readL('hotspotdata.csv')
data = quickLinePatch(data)
listHotspots = ListGen(data)
dictHotspots = ListToDict(listHotspots)
coords = getCoords() # {'Long_': longcoord, 'Lat': 'lat coord'}
print coords
addDist(dictHotspots,float(coords['Lat']),float(coords['Long_']))
closest = minDist(dictHotspots) #returns the object id (the key) of the closest hotspot














# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ========
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!!
htmlStr += '<html><head><title> Handy Hotspot v0.1 </title><link rel="icon" href="logo1.gif"></head></html>\n'
htmlStr += "<body><center>"

# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
htmlStr += "<h3>Handy Hotspot v0.1</h3>"
htmlStr += "<h4>Data Input:</h4>"
htmlStr += str( FStoD() )
htmlStr += "<h4>Data Output:</h4>"
htmlStr += getMap(closest['Lat'], closest['Long_'])
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

htmlStr += "</center></body></html>"


print htmlStr

#LEGAL JIBBER JABBER
#Handy Hotspot isn't endorsed by Google Inc. and doesn't reflect the views or opinions of Google Inc.
#or anyone officially involved in producing or managing Google Maps. Google Maps and Google Inc. are trademarks
#or registered trademarks of Alphabet, Inc.
