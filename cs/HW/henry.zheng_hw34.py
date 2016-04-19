#Henry Zheng
#IntroCS2 pd8
#HW34 -- Oh, Give Me a Home Where The Buffalo Roam
#2016-04-18

import random

#1.
def merge(L1,L2):
    ans = []
    combined = L1 + L2 #combines the two lists
    biggest = max(combined)
    for num in range(biggest + 1): #creates a list of biggest # elements (sorted)
        while num in combined:
            ans += [num]
            combined.remove(num)  #removes num in case it appears again
    return ans

a= [0,2,4,6,8]
b= [1,3,5,7]
print merge(a,b)  #should be [0, 1, 2, 3, 4, 5, 6, 7, 8]

#2.
def randList(n):
    nums = []
    while n > 0:
        nums.append(random.randrange(10)) #adds a random number between 0 and 9, inclusive
        n -= 1  #subtracts one to have n number terms
    return nums
print randList(3)  #with 3 terms. should be [?,?,?]

#3.
def randIPv4():
    return str(random.randrange(256)) + "." + str(random.randrange(256)) + "." + str(random.randrange(256)) + "." + str(random.randrange(256))

print randIPv4()  #should be ?.?.?.?
