#!/usr/bin/python
print "Content-type:text/html\n\n"
"""
Henry Zheng
IntroCS2 pd8
HW47 -- CSV -> HTML
2016-05-15
"""


#opens the csv file
inStream = open('testdata.csv','r')  #opening and reading the csv file
data = inStream.readlines()  #splits into a list element (per line)
inStream.close()  #closes the csv file

"""
Problems:
1. Commas in the names of the school- dealt with by string slicing
2. Making helper functions - used old functions from past homeworks
"""

def isNum(n):
    if len(str(n)) != 3:
        return False
    else:
        return (ord(n[2]) > 47 and ord(n[2]) < 58)

#--------------------------------------------------------------------

#genTable- generates a table with html
def genTable(lines):
    string = '<table border="1"> \n'  #beginning of table
    sumall = 0
    index = 0
    frequency = 0
    
    for row in lines:
        row = row.replace(', ', ' ')
        row = row.replace('\n','')
        row = row.split(',')  #splits each element in the readlines list into sublists containing [column one value, column two value]
        #print row
        string += '<tr>\n'  #adds a row for each line in readlines
        for column in row:  #for each value in the sublist
            if isNum(column) and index != 2:
                sumall += int(column)
            index += 1
            string += '<td>' + column + '</td>\n'  #adds the data
        if sumall == 0 and frequency == 0:
            string += '<td>' + 'Average Total Score' + '</td>\n'
            frequency += 1
        elif sumall == 0:
            string += '<td>' + 's' + '</td>\n'
            frequency += 1
        else:
            string += '<td>' + str(sumall) + '</td>\n'
            frequency += 1
        sumall = 0
        index = 0
        string += "</tr>\n"  #closes the row after both column one and two values are inserted into table data tags

    string += "</table>"  #ends the table
    return string


#prints the html
html = '<html>\n<body>\n<center>' + '\n' + 'This is a list of the SAT scores of all of the high schools in NYC in 2012 in a table format, using a python script to read a csv file and converting it into HTML\n' + genTable(data) + '\n' + '</center>\n</body>\n</html>'  #adds the beginning and end of the html tags
print html  #prints the html to check to see if it works


#writes to the html file
write_to = open('table1.html','w')  #opens the html file in write state
write_to.write(html)  #writes the html into the file
write_to.close()  #closes the html
