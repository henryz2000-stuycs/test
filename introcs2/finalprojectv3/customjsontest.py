import urllib2
import json
jsontest = """{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "1600",
               "short_name" : "1600",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Amphitheatre Pkwy",
               "short_name" : "Amphitheatre Pkwy",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Mountain View",
               "short_name" : "Mountain View",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Santa Clara County",
               "short_name" : "Santa Clara County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "California",
               "short_name" : "CA",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "94043",
               "short_name" : "94043",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA",
         "geometry" : {
            "location" : {
               "lat" : 37.4224764,
               "lng" : -122.0842499
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 37.4238253802915,
                  "lng" : -122.0829009197085
               },
               "southwest" : {
                  "lat" : 37.4211274197085,
                  "lng" : -122.0855988802915
               }
            }
         },
         "place_id" : "ChIJ2eUgeAK6j4ARbn5u_wAGqWA",
         "types" : [ "street_address" ]
      }
   ],
   "status" : "OK"
}
"""
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=25219+82nd+rd'
response = urllib2.urlopen(url)
info = response.read()
info = info.replace('true','True') #changes the file to use python boolean format
exec "jsonDict =" + info
print jsonDict
print jsonDict["results"][0]['geometry']['location']['lat']
#for elem in json:
#    print elem
#    print "AYYLMAO"


#def jsonDict(T):
#    text = T #local variable that can be destroyed
#    if text[0] == '{': #if the current portion you are working with right now is a dictionary:
#        D = {}
#        while text.strip() != '':#while there is still data that has not been gone through:
#            spltlist = text.split(':',2) #split the text at first 2 semicolons, giving you 3 parts.
#            spltlist[2] = spltlist[1][spltlist[1].rfind(',')+1:] + spltlist[2] #removes the key of the next part from the split test
#            spltlist[1] = spltlist[1][:spltlist[1].rfind(',')]
#            D[spltlist[0].strip()] = spltlist[1].strip() #
#            if D[spltlist[0].strip()][0] in ['[','{']:
#                D[spltlist[0].strip()][0] = jsonDict(spltlist[1].strip()) #RECURSION
#            text = text[2].strip() #the text is now restricted to the parts that havnt been removed
#        elif text[0] == '[':
#            L = []
#            while len(text.split('{')) != 1: #while splitting at brackets doesnt equal 1, meaning there are no brackets left:
    #            text  = text.split('[',1) #splits the text once.
