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

#helper functions
def crtBuckets(nums):
    starting_list = nums #ensures that function isn't destructive to the starting list.
    buckets = {} #the buckets that will be returned at the end of the function
    while starting_list != []:
        key = str(starting_list.pop(0)) #the key is equal to the first element in the list, which is then popped.
        if key in buckets.keys(): #if the key is in the list of keys, then increase its counter by 1. Else, define it as 1.
            buckets[key] += 1
        else:
            buckets[key] = 1
    return buckets
def maxPos(L): #returns the index largest number in a list by itterating through it. The first number in the list is chosen if there are 2 equally small numbers.
    ans = 0 #start with number 1
    counter = ans+1
    last = len(L)-1 #the last element of the string
    while counter <= last: #iterate and clear the list one element at a time
        if L[ans] < L[counter]: #if the next number being iterated is more than the current min, set the answer to that number.
            ans = counter
        counter +=1
    return ans
#-----------------

#uses the buckets we created and then parallel lists to figure out the value.
def modeLB(nums):
    buckets = crtBuckets(nums) #defines buckets as an empty dictionary.
    mode = maxPos(buckets.values()) #the index of the mode based on the keys is equal to the index of highest number in the bucket valeus
    return int(buckets.keys()[mode]) #return the indexth item of the list of keys

#1. mean
def meanList(nums):
    sum_list = 0.0 #This is the variable that holds the total. Uses a float to end up with a correct mean.
    for num in nums:
        sum_list += num
    ans = sum_list/len(nums)
    if ans == int(ans):
        ans = int(ans)
    return ans

#2. median
def minPos(L): #returns the index smallest number in a list by itterating through it. The first number in the list is chosen if there are 2 equally small numbers.
    ans = 0 #start with number 1
    counter = ans+1
    last = len(L)-1 #the last element of the string
    while counter <= last: #iterate and clear the list one element at a time
        if L[ans] > L[counter]: #if the next number being iterated is less than the current min, set the answer to that number.
            ans = counter
        counter +=1
    return ans

def median_index(L):
    num_elements = len(L) #number of elements in the list.
    return (num_elements+1)/2.0 #returns the location of the median

def nth_smallest(L,n,is_even):
    counter = n
    if is_even:
        counter -=1 #if its even, use both the upper and the lower bound.
    ans = []
    while counter > 0:
        ans = [L.pop(minPos(L))]
        counter -= 1
    if is_even: #if even, then add the current smallest number, which would be next element in the list.
        ans += [L.pop(minPos(L))]
    return ans


def medList(nums):
    index = median_index(nums)
    if int(index) != index: #if the median_index happened to have a .5, then there are an even number of terms
        return meanList(nth_smallest(nums,index,True))
    else:
        return meanList(nth_smallest(nums,index,False))

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
    list = []
    
    for row in lines:
        row = row.replace(', ', ' ')
        row = row.replace('\n','')
        row = row.split(',')  #splits each element in the readlines list into sublists containing [column one value, column two value]
        #print row
        list.append(row)
        data = list
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

#stats
totals_list = []
for element in data[1:]:
    if element[3] != 's' and element[4] != 's' and element[5] != 's':
        totals_list.append(int(element[3])+int(element[4])+int(element[5]))

#prints the html
html = '<html>\n<body>\n<center>' + '\n' + '\
This is a list of the SAT scores of all of the high schools in NYC in 2012 in a table format\
, using a python script to read a csv file and converting it into HTML\n\
' + '<ul>\
' + '<li>Mean: ' + str(meanList(totals_list)) + '</li>\
' + '<li>Median: ' + str(medList(totals_list)) + '</li>\
' + '<li>Mode: ' + str(modeLB(totals_list)) + '</li>\
' + '<li>Low: ' + str(totals_list) + '</li>\
' + '<li>High: ' + str(totals_list) + '</li>\
' + genTable(data) + '\n' + '</center>\n</body>\n</html>'  #adds the beginning and end of the html tags
print html  #prints the html to check to see if it works


#writes to the html file
write_to = open('table2.html','w')  #opens the html file in write state
write_to.write(html)  #writes the html into the file
write_to.close()  #closes the html
