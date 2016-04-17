#Henry Zheng
#IntroCS2 pd8
#HW26 -- Float Like a Butterfly, Sting Like a Bee
#2016-04-05

def minPos(L):
    newL = L  #copies L into another list to find the minNum
    minNum = newL[0]  #starts off minNum as the first value of the list
    newL = newL[1:]  #chops off first value because minNum has already taken the first number into account
    ind = 0  #starts off at first number
    while len(newL) > 0:  #goes until newL is gone
        if minNum > newL[0]:  #if there is a lower number than minNum
            minNum = newL[0]  #replaces minNum with newer minNum
        newL = newL[1:]  #continues onto next number
        while minNum != L[ind]:  #while loop to find the index of minNum
            ind += 1  #adds one to index until it reaches minNum
    return ind  #returns index of least value

print minPos([3])  #should be 0
print minPos([5,4,3,2,1])  #should be 4
