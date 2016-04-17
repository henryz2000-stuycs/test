#Henry Zheng
#IntroCS2 pd8
#HW#28 -- For vs. While
#2016-04-08

"""
# 1. WvF: Used for loop because not creating new list
# 2. WvF: Used while loop because needed to implement counter and use previous answers
# 3. WvF: Used for loop because gave output of all elements in a specific manner
"""

#1.
def rmNegatives(L):
    for x in L:
        if x < 0:  #if the element is negative
            L.remove(x)  #removes the element
    return L

print rmNegatives([5,4,3,2,1])  #should be [5,4,3,2,1]
print rmNegatives([5,-4,3,-2,1])  #should be [5,3,1]

#2.
def listFib(n):
	ans = [0,1]  #the beginning list
	if n <= 2:
		return ans[:n]
	counter = n
	while counter > 2:
		ans += [(ans[-1]+ ans[-2])]  #adds the last two numbers together to create the next number
		counter -= 1  #subtracts 1 from counter to get to next number
	return ans

print listFib(1)  #should be [0]
print listFib(2)  #should be [0,1]
print listFib(3)  #should be [0,1,1]
print listFib(4)  #should be [0,1,1,2]

#3.
def sentify(L):
    ans = ""
    for x in L:
        ans += x + " "  #adds each element with a space to the ans string
    return ans

print sentify(["this", "is", "how", "we", "do"])  #should be "this is how we do"
