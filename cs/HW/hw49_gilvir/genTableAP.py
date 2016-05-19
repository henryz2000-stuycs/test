#!/usr/bin/python
print "Content-type:text/html\n\n"
"""
Team Public Relations -- Gilvir Gill, Henry Zheng, Director of Public Relations
IntroCS2 pd8
HW# -- Correlation Is Not Causation
2016-05-16
"""

"""
The dataset we chose was the dataset of AP results. We chose this because it was interesting and it contained NYCDOE school codes :P

Our plan for establishing a correlation between its data and our SAT data is to divide the number of exams with a score of 3+
by the number of total exams taken for the AP data. Then, we will compare this to the SAT data by looking at the top percentage
and the top average SAT scores for the high schools in the city and see if there is a correlation.

Our progress so far was finding and choosing the dataset of AP results, and developing a plan to establish a correlation between the AP data and our SAT data.
We also copied over our code from the SAT data and started replacing the names of some files to correspond to the AP data instead of the SAT data.
"""

"""
Problems:
1. Commas in the name-- This was dealt with by just removing them from the names using string slicing, because replace wasn't working properly and other methods may be too intensive.
2. Getting mean/max/mode information-- Copy functions from old homeworks, make a list with added up all scores and put it in an unordered list at the top.
"""
#helpers
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
#-----------------#

#uses the buckets we created and then parallel lists to figure out the value.
def modeLB(nums):
    buckets = crtBuckets(nums) #defines buckets as an empty dictionary.
    mode = maxPos(buckets.values()) #the index of the mode based on the keys is equal to the index of highest number in the bucket valeus
    return int(buckets.keys()[mode]) #return the indexth item of the list of keys
# 1. meanList. Basically, adds up all numbers in the sum, then divides it by the total number. This is done using a for loop to get the sum of the list, by adding each element to a state variable.
def meanList(nums):
    sum_list = 0.0 #This is the variable that holds the total. Starts as float so average can be floated.
    for num in nums:
        sum_list += num
    ans = sum_list/len(nums)
    if ans == int(ans):
        ans = int(ans)
    return ans

# 2. medList. Returns the median of the list by first finding the middle elements, and using a while loop based function to locate the medians by counting down from their location.
#minpos function used for indexes from a few assignments ago
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
    return (num_elements+1)/2.0 #returns the location of the median. If you have a list with 7 elements, it returns 4-1, which is 3.

def nth_smallest(L,n,is_even):
    counter = n
    if is_even:
        counter -=1 #if its even, account for the double case by starting at a lower counter.
    ans = []
    while counter > 0:
        ans = [L.pop(minPos(L))]
        counter -= 1
    if is_even: #if even, then add the current smallest number, which would be next element in the list.
        ans += [L.pop(minPos(L))]
    return ans


def medList(nums):
    index = median_index(nums)
    if int(index) != index: #if the median_index happened to have a .5, then add a lower and upper bound. If the median index happened to be 4.5, make it account for both 4 and 5
        return meanList(nth_smallest(nums,index,True))
    else:
        return meanList(nth_smallest(nums,index,False))



#opening and reading the csv file.
def readL(filename):
    inStream = open(filename,'r')
    data = inStream.readlines()
    inStream.close()
    return data

data = readL('dataAP.csv')
def TableListGen(lines): #generates a table by while looping through
    list = []
    for line in lines:
        index = line.find(", ")
        while ', ' in line:
            if index != -1:
                line = line[:index]+line[index+1:] #removes the commas.
        list.append(line.split(','))
    return list


data = TableListGen(data)
#genTable- generates a table with html, taking a the list in the same list format
def genTable(table):
    #first thing to do is for each element, split into a list.
    string = '<table border="1"> \n'
    for row in table:
        string += '<tr>\n'
        for column in row:
            string += '<td>%s</td>\n' % (column)
        string += "</tr>\n"
    string += "</table>"
    return string

#makes a list of added totals for each school:

def getColumns(L,n):
    totals_list = []
    for element in L[1:]:
        if element[3] != 's' and element[4] != 's':
            totals_list.append(int(element[n]))
    return totals_list



total_list = getColumns(data,3)
threeplus_list = getColumns(data,4)
intro = """ This viewer is a summary of all the SAT scores of New York City from 2012, using python to turn a csv file
into an HTML table. It also provides the mean, median, mode, high, and low for the total scores. The file first generates
a 2D list with the column row set up matching the csv table, then uses list indecies to perform different
operations on the list to retreive statistical information, which is then printed on the top. Old school percent placeholders are used to substitute in the data.
"""
total_list = """
<ul> Total Exams Taken:
<li>Mean: %s</li>
<li>Median: %s</li>
<li>High: %s</li>
<li>Low: %s</li>
<li>Mode: %s</li>
</ul>
""" % (meanList(total_list), medList(total_list), max(total_list), min(total_list), modeLB(total_list))
threeplus_list = """
<ul> Number of Exams with Scores 3+:
<li>Mean: %s</li>
<li>Median: %s</li>
<li>High: %s</li>
<li>Low: %s</li>
<li>Mode: %s</li>
</ul>
""" % (meanList(threeplus_list), medList(threeplus_list), max(threeplus_list), min(threeplus_list), modeLB(threeplus_list))





html = '<html> \n <body>' + '\n' + intro + total_list + threeplus_list + genTable(data) + '\n' + '</body> \n </html>'
print html


write_to = open('statsAP.html','w')

write_to.write(html)

write_to.close()
