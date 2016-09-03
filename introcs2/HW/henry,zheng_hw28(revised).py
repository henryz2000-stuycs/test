#Henry Zheng
#IntroCS2 pd8
#HW28 -- For vs. While (revised)
#2016-04-11

def rmNegatives(L):
    ind = 0  #starts off at the beginning of the list
    while ind < len(L):
        if L[ind] < 0:  #if that number is negative
            L = L[:ind]+ L[ind+1:] #sets L equal to all elements except for the index
        else:
            ind +=1  #goes onto next number
    print L  #instead of returning L

#didn't use .remove but instead modified L and just printed it

rmNegatives( [5,4,3,2,1] )  #should be [5,4,3,2,1]
rmNegatives( [5,-4,3,-2,1] )  #should be [5,3,1]
