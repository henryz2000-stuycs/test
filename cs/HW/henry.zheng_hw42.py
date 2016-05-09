"""
Team Public Relations -- Gilvir Gill and Henry Zheng, Director of Public Relations
IntroCS2 pd8
HW42 -- Mode
2016-05-05
"""

#1 modeLB(nums) uses dictionary and buckets.
#-----Helpers-----#
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


#0.
"""
Fixed inefficiences in fnction, using some ideas from Ryan Siu (thanks Ryan!)
1.  Convert into a list
2. Turn each name into a single string, in last-first order
3. Uses the last-first order to get the proper order, accounting for both first and last names, instead of just last names
3. Use pop on the minimum.
"""
def minPos(L): #returns the index smallest number in a list by itterating through it. The first number in the list is chosen if there are 2 equally small numbers.
    ans = 0 #start with number 1
    counter = ans+1
    last = len(L)-1 #the last element of the string
    while counter <= last: #iterate and clear the list one element at a time
        if L[ans] > L[counter]: #if the next number being iterated is less than the current min, set the answer to that number.
            ans = counter
        counter +=1
    return ans

def alphabetize(names):
    ans = ""
    names_list = names.split(',')
    #parallel lists with first and last names created with basic string splitting. No need for complicated helper functions (thanks Md!)
    last_first = [] #list of names in last,first order
    for num in range(0,len(names_list),2): #for every second index value (all the last names):
        last_first +=[names_list[num] + "," + names_list[num+1]] #creates the list of last,first names. The index of these is exactly half of the index of last names.
    while last_first != []:
        next_name = minPos(last_first)
        ans += names_list.pop(2*next_name +1) + ' ' + names_list.pop(2*next_name) + "\n" #joins the list of the first last order of the smallest number.
        del last_first[next_name]
    return ans[:-1]
#TEST CASES
print modeLB( [0,5,7,3,2,3] )
print modeLB( [0,5,7,3,7,3] )
print alphabetize("Wayne,Bruce,Kent,Clark,Parker,Peter")
print ""
print alphabetize("Wayne,Bruce,Kent,Clark,Bradberry,Moe,Bradberry,Ethan")
