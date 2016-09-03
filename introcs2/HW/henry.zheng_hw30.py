# Team Hangry - Tahseen Chowdhury, Kaia Tien, Henry Zheng
# IntroCS2 pd8 
# HW30 -- Removal three ways
# 2016-04-13

"""
POP: 
syntax: L.pop() or L.pop(3)
behavior: It takes a element out of a list, as specified by the index [in the parameter] and then returns the element. If there is no parameter, it returns and removes the last element of said list.
------------------------------------------------------------------------
REMOVE:
syntax: L.remove("TEAMHANGRY")
behavior: Removes the first occurence of the parameter in a list. If there is no occurence of parameter, then there is an error.
------------------------------------------------------------------------
DEL:
syntax: del L[ind] or del L[starting_index:ending_index]
behavior: Removes an item from a list based on the index parameter.
------------------------------------------------------------------------
TeamHangry prefers .remove for use in rmNegatives() because .pop returns elements that are taken out, which we do not want, and del deletes elements given a specific index, while we only want to delete negative numbers.
"""

def rmNegatives(L):
    for x in L:  #goes through every element of the list
        if x < 0:  #if element is negative
            L.remove(x)  #removed from list
    print L

rmNegatives([1,2,3,-5,6,7,8,-9])  #should be [1,2,3,6,7,8]
