# Henry Zheng
# IntroCS2 pd8
# HW10 -- Visiting Old Friends
# 2016-03-08

import math

# 1.
def areaCirc(r):
    return math.pi*r**2  #uses area of a circle formula area=pi*r^2

print areaCirc(1)  #should be 3.14159265359
print areaCirc(3)  #should be 28.2743338823
print areaCirc(5)  #should be 78.5398163397

# 2.
def areaWasher(radInner,radOuter):
    return math.pi*radOuter**2 - math.pi*radInner**2  #takes the area of the outer circle and subtracts the area of the inner circle

print areaWasher(0,2)   #should be 12.5663706144
print areaWasher(3,5)   #should be 50.2654824574
print areaWasher(6,10)  #should be 201.06192983

# 3.
def sumOfSquares(a,b):
    return a**2 + b**2

print sumOfSquares(0,0)  #should be 0
print sumOfSquares(1,2)  #should be 5
print sumOfSquares(4,5)  #should be 41
