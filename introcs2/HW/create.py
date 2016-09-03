#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

"""
Henry Zheng
IntroCS2 pd8
HW#61 -- Knock Knock!
2016-06-08
"""

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

def hidepass():  #encrypts the password
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

def add(filename, data):  #adds data to the filename, in this case "users.txt"
    inStream = open(filename,'a')
    inStream.write(data + "\n")
    inStream.close()
    return filename

def read(filename):  #reads the file
    readfile = open(filename,'r')
    readfile = readfile.readlines()
    return readfile

def namesL(L):  #gets the list of already created users
    names = read(L)
    users = []
    accounts = []
    for subL in names:
        x = subL.strip()
        accounts.append(x)       #gets usernames + space + passwords   
    for password2 in accounts:
        space = password2.find(' ')
        users.append(password2[:space])  #gets everything up to but not including the space (only usernames and not space nor passwords)
    return users

def getUser():  #gets username from query string
    username = query['username'].value
    return username

def final():  #combines all functions together into the final function
    users = namesL("users.txt")
    if getUser() in users:  #if username is already in the database
        return "That username is taken. Please try again.<br> <a href='create.html'>Back</a>\
<br>If you meant to login, click <a href='login.html'>here</a>."
    else:
        users.append(getUser())  #appends the username to the getUser() list
        data = getUser() + " " + hidepass()
        add('users.txt',data)  #adds the username + space + password to the database
        return "Congratulations! You've made an account.<br>Log In <a href='login.html'>here</a>."


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title> Create </title></head></html>\n"
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
