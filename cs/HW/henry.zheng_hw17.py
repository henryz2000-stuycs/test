#Henry Zheng
#IntroCS2 pd8
#HW17 -- 000 000 111
#2016-03-17

def bondify(name):
    n=0                            #essentially the subscript. 0 starts off the search at the first character
    while name[n] != " ":          #whenever the number at the index called is not the space between the first and last name, it adds one to the index and runs the function continuously until it gets to the space
        n+=1
    n+=1                           #adds one to the final answer of n in order to not include the space in the beginning of our answer
    return name[n:] + ", " + name  #returns "last_name, full_name"

print bondify("James Bond")        #should be "Bond, James Bond"
print bondify("Henry Zheng")       #should be "Zheng, Henry Zheng"
print bondify("Bondify Test")      #should be "Test, Bondify Test"
