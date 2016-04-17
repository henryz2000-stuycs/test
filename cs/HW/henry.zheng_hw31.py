#Henry Zheng
#IntroCS2 pd8
#HW#31 -- Stat-tastic
#2016-04-14

#1.
def meanList(nums):
    sumnums = 0  #sum of numbers in the list (starts at 0)
    numnums = 0  #number of numbers in the list (starts at 0)
    for x in nums:
        sumnums += x  #adds each number to the sumnums
        numnums += 1  #adds 1 for each number in the list
    return float(sumnums) / float(numnums)  #returns the mean by dividing sum of numbers by the number of numbers

print meanList([0,1,2,3])  #should be 1.5
print meanList([68,69,70])  #should be 69

#2.
def medList(nums):
    nums = sorted(nums)  #sorts numbers
    numnums = 0  #number of numbers in the list (starts at 0)
    for x in nums:
        numnums += 1  #adds 1 for each number in the list
    if numnums % 2 != 0:  #if number of numbers in list is odd
        numnums /= 2  #gets the index of the middle term
        return nums[numnums]  #returns the median
    else:  #if number of numbers in list is even
        summeds = 0  #sum of middle two numbers (starts at 0)
        numnums /= 2  #gets the index of the higher middle term
        summeds += nums[numnums] + nums[numnums - 1]  #adds the higher middle term and the lower middle term to the summeds
        return float(summeds) / float(2)  #finds the mean of these two medians

print medList([0,1,2,3])  #should be 1.5
print medList([3,4,5])  #should be 4
print medList([15,24,36,8,16])  #should be 16
print medList([15,24,36,8,16,12])  #should be 15.5


def medchallenge(nums):
    if len(nums) % 2 != 0:  #if number of numbers in list is odd
        while len(nums) > 1:  #until there is only 1 remaining number
            nums.remove(min(nums))  #removes minimum number
            nums.remove(max(nums))  #removes maximum number
        return nums[0]  #returns that number (median)
    else:  #if number of numbers in list is even
        while len(nums) > 2:  #until there are 2 remaining numbers
            nums.remove(min(nums))  #removes minimum number
            nums.remove(max(nums))  #removes maximum number
        return meanList(nums)  #returns the mean of the last 2 remaining numbers

print medchallenge([0,1,2,3])  #should be 1.5
print medchallenge([3,4,5])  #should be 4
print medchallenge([15,24,36,8,16])  #should be 16
print medchallenge([15,24,36,8,16,12])  #should be 15.5

#3.
def barGraphify(nums):
    ind = 0  #starts off index at 0
    for x in nums:
        print str(ind) + ": " + x*"="  #prints the index, a colon, and then the number of bars in that index
        ind += 1  #adds one to index to continue on the list

barGraphify([0,1,2,3])
#should be
#0: 
#1: =
#2: ==
#3: ===
barGraphify([1,0,3,2])
#should be
#0: =
#1: 
#2: ===
#3: ==
