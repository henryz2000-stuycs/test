#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========


# =================================================
# ==== LOOK AT FIRST FILE FOR IN-LINE COMMENTS ====
# =================================================

"""
Henry Zheng
IntroCS2 pd8
HW#61 -- Knock Knock!
2016-06-08
"""

# =================================================
# ==== LOOK AT FIRST FILE FOR IN-LINE COMMENTS ====
# =================================================

import cgi
import cgitb
import hashlib
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

def hidepass():
    #ans = ""
    #perimeter = 0
    keys = query.keys()
    password1 = hashlib.sha224()
    password1.update(query["password"].value)
    return password1.hexdigest()
    #L = []
    #for k in keys:
    #    perimeter += float(query[k].value)
    #    L += [float(query[k].value)]
    #if not isTri(L):
    #    return "ERR: Not a triangle"
    #else:
    #    ans += "Perimeter = " + str(perimeter) + "<br>"
    #    semiperimeter = perimeter/2.0
    #    s = semiperimeter
    #    area = (s*(s-L[0])*(s-L[1])*(s-L[2]))**(1.0/2.0)
    #    ans += "Area = " + str(area)
    #    return ans

def add(filename, data):
    inStream = open(filename,'a')
    inStream.write(data + "\n")
    inStream.close()
    return filename

def read(filename):
    readfile = open(filename,'r')
    readfile = readfile.readlines()
    return readfile

def namesL(L):
    names = read(L)
    users = []
    accounts = []
    for subL in names:
        x = subL.strip()
        accounts.append(x)        
    #for password2 in accounts:
        #space = password2.find(' ')
        #users.append(password2[:space])
    return accounts

def getUser():
    username = query['username'].value
    return username

def final():
    users = namesL("users.txt")
    if str(getUser() + " " + hidepass()) in users:
        return "Logged in! Click <a href='home.html'>here</a> to continue!"
    else:
        #users.append(getUser())
        #data = getUser() + " " + hidePass()
        #add('users.txt',data)
        return "Wrong info! Please try again <a href='login.html'>here</a>.\
<br> If you meant to create an account, press <a href='create.html'>here</a>."


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title> Login </title></head></html>\n"
htmlStr += "<body>"

# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
#htmlStr += "<h3>Perimeter and Area</h3>"
#htmlStr += "<h4>Data Input:</h4>"
#htmlStr += str( FStoD() )
htmlStr += "<h4>Data Output:</h4>"
htmlStr += final()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

htmlStr += "</body></html>"


print htmlStr
