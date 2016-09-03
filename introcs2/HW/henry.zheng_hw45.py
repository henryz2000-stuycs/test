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
blacklist = ["the","is", "was", "his", "when", "so", "th", "made", "her", "an", "their", "with", "in", "had","then", "him", "at", "it", "on", "were", "for", "be", "to", "or", "our", "all", "not", "and", "of", "i", "a", "he", "as", "that", "have", "this", "but", "by", "they", "as", "we", "us", "day", "give", "most", "because", "never", "first", "work", "just", "no", "go"] #blacklists some of the most commonly occuring words in English

def wordtally(file_name):
    story = open(file_name,"r")
    storynew = story.read()
    storynew = storynew.lower()
    story.close()
    storynew = storynew.split(' ')
    ind = 0
    while ind < len(storynew):
        for x in punc:
            storynew[ind] = storynew[ind].strip(x)
        storynew[ind] = storynew[ind].strip('\n')
        ind += 1
    storynew = storynew[storynew.index('--header--'):storynew.index('--footer--')]
    starting_list = storynew #ensures that function isn't destructive to the starting list.
    buckets = {} #the buckets that will be returned at the end of the function
    while starting_list != []:
        key = starting_list.pop(0) #the key is equal to the first element in the list, which is then popped.
        if key in buckets.keys(): #if the key is in the list of keys, then increase its counter by 1. Else, define it as 1.
            buckets[key] += 1
        else:
            buckets[key] = 1
    delete = []
    for key in buckets:
        if key in blacklist:
            delete.append(key)
    for key in delete:
        del buckets[key]
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
def modeLB(nums):
    buckets = wordtally(nums) #defines buckets as an empty dictionary.
    mode = maxPos(buckets.values()) #the index of the mode based on the keys is equal to the index of highest number in the bucket valeus
    print '''<center>
This is a list of the top 30 most frequently occuring words (kinda repetitive from the title don'tcha think?) in
<a href="lit.txt">Lysistrata by Aristophanes.</a> 
<br>
<br>
This assignment entails isn't all too simple, and requires everal functions. First off we have the 'readfile' function, which, as based off of the name, <br>
reads the file. Then, after removing newlines and punctuation from the story, we use the wordtally function to create a dictionary that <br>
adds each word as a new key, and when the word is encountered again, adds a value of one to the key to mark down the frequency. The tablefy function <br>
then creates the tables with the 30 words of highest frequency in order, making a colum for word and a column for frequency. 
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
    num = 1
    while num != 30:
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
    print "</table>"

#test cases
#print wordtally("story.txt")
modeLB("lit.txt")
print "</center>"
print "</html>"

