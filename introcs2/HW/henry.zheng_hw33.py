#Henry Zheng
#IntroCS2 pd8
#HW33 -- Bucket List
#2016-04-17

#1.
def maxPos(L):
    ans = 0 #starts off the answer at 0
    counter = 1 #starts counter off at 1
    last = len(L)-1 #the index of the last element of the string
    while counter <= last: #goes through the list
        if L[ans] < L[counter]: #if the # of times the number represented by counter is greater than current ans
            ans = counter  #updates answer
        counter +=1  #continues on the list
    return ans

def modeList(nums):
    counter = max(nums)  #determines the number of buckets
    buckets = []  #starts off buckets as an empty list
    while counter >= 0:
        buckets += [0] #adds buckets
        counter -= 1  #subtracts one from the total # of buckets left to be added
    for x in nums:
        buckets[x] += 1 #adds one to the corresponding bucket
    return maxPos(buckets) #returns the bucket that appears the most

print modeList([0,5,7,3,2,3])  #should be 3
print modeList([0,5,7,3,7,3])  #should be 3



#2. vBarGraphify. Takes non-negative integers and prints a set of vertical bars, using a while loop based off a subtracting counter that starts at the highest value.

def vBarGraphify(nums):
    counter = max(nums) #determines the highest height of the bar graph
    ans = ""
    while counter != 0:
        for x in nums:
            if x < counter:  #in order to start off with the tallest bars
                ans += "  " #if the number is less than the counter, add a blank and a space
            else:
                ans += "* " #if the number has the most, add a tick and a space
        ans += "\n" #to go onto the next line of the bar graph
        counter -= 1
    last = len(nums)-1  #highest number
    counter = 0  #starts number list off at 0
    while counter <= last:  #adds the bottom line
        ans += str(counter) + " "
        counter += 1  #continues on the numbers
    print ans

x = [0,1,2,3]
print x
vBarGraphify(x)
#should be
#      * 
#    * * 
#  * * * 
#0 1 2 3

x = [1,0,3,2]
print x
vBarGraphify(x)
#should be
#    *   
#    * * 
#*   * * 
#0 1 2 3 
