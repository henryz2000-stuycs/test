import math

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


data = readL('hotspotdata.csv')
data = quickLinePatch(data)
liststuff = ListGen(data)
#print liststuff[0]
#print liststuff[635]
#print "Lengths:"
#print len(liststuff[0])
#print len(liststuff[635])
#print data[635]
dictstuff = ListToDict(liststuff)
#print dictstuff['635']
addDist(dictstuff,40.71794,-74.01392)


#for key in dictstuff:
#    print dictstuff[key]['Boro'] + ' ' + dictstuff[key]['Lat'] + ' ' + dictstuff[key]['Long_'] + "Distance: " + str(dictstuff[key]['Distance'])
print dictstuff[minDist(dictstuff)]
