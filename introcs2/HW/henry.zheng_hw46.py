#!/usr/bin/python
print "Content-type:text/html\n"
print ""
print "<html>"
print "<style>"
print '''
table, th, td {
   border: 1px solid black;
   text-align: center;
}
'''
print "</style>"
"""
Team Whatever -- Michael Leyderman and Henry Zheng
IntroCS2 pd8
HW45 -- Text Analysis, Webified
2016-05-11
"""

"""
1. Step 1: Split up story by spaces into list. This will allow us to loop through the list and use the dictionary mode function written previously.
2. Step 2: Use dictionary mode function to create a value of 1 for each instance of a unique word. This will make it efficient.
3. Step 3: Add 1 value for each instance of each word (not including first one). This will increase each value until the end of the story when a mode can be found.
"""

#*******************************
#IGNORE ANYTHING BELOW THIS LINE
#*******************************

punc = ['.',',','!','?']

def readfile(file_name):
    story = open(file_name,"r")
    storynew = story.read()
    storynew = storynew.lower()
    story.close()
    storynew = storynew.split(' ')
    return storynew
def wordtally(file_name):
    ind = 0
    while ind < len(file_name):
        for x in punc:
            file_name[ind] = file_name[ind].strip(x)
        file_name[ind] = file_name[ind].strip('\n')
        ind += 1
    starting_list = file_name #ensures that function isn't destructive to the starting list.
    buckets = {} #the buckets that will be returned at the end of the function
    while starting_list != []:
        key = starting_list.pop(0) #the key is equal to the first element in the list, which is then popped.
        if key in buckets.keys(): #if the key is in the list of keys, then increase its counter by 1. Else, define it as 1.
            buckets[key] += 1
        else:
            buckets[key] = 1
    return buckets
def maxPos(L): #returns the index largest number in a list by itterating through it. The first number in the list is chosen if there are 2 equally small numbers.
    ans = 0 #start with number 1
    counter = ans + 1
    last = len(L) - 1 #the last element of the string
    while counter <= last: #iterate and clear the list one element at a time
        if L[ans] < L[counter]: #if the next number being iterated is more than the current min, set the answer to that number.
            ans = counter
        counter += 1
    return ans
def topN(nums):
    num = 1
    while num != 60:
        buckets[buckets.keys()[mode]] = 0
        mode = maxPos(buckets.values())
        num += 1
    while num != 90:
        if str(buckets.keys()[mode]) == "":
            buckets[buckets.keys()[mode]] = 0
            mode = maxPos(buckets.values())
        keys = buckets.keys()
        print "<tr>"
        print "<td>" + str(buckets.keys()[mode]) + "</td>"
        print "<td>" + str(buckets.values()[mode]) + "</td>"
        print "<td>" + str((float(buckets.values()[mode])/float(len(keys)))*100) + "</td>"
        print "</tr>"
        buckets[buckets.keys()[mode]] = 0
        mode = maxPos(buckets.values())
        num += 1
def tablefy(nums):
    buckets = wordtally(nums) #defines buckets as an empty dictionary.
    mode = maxPos(buckets.values()) #the index of the mode based on the keys is equal to the index of highest number in the bucket valeus
    print '''<center>
This is a list of the top 30 most frequently occuring words (kinda repetitive from the title don'tcha think?) in
<a href="story.txt">Lysistrata by Aristophanes</a>
<br>
<br>
<table>
<tr>
30 Most Frequently Occuring Words
</tr>
<tr>
<td>Words</td>
<td>Frequencies</td>
<td>Percentage (%)</td>
</tr>'''
    topN(nums)
    print "</table>"
def finalFreq(file_name):
    ans = readfile(file_name)
    ans = wordtally(ans)
    ans = tablefy(ans)
    return ans

#-------------------------
print finalFreq("lit.txt")
print "</center>"
print "</html>"

