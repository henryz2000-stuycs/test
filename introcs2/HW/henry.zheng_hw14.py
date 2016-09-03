#Henry Zheng
#IntroCS2 pd8
#HW14 -- Repetition two ways
#2016-03-14

#1.
def factR(n):
    if n<=1:       #when n=0 or n=1, the answer is always 1
        return 1
    else:          #multiplies n by the recursive function of factR(n-1) to create a factorial function
        return n*factR(n-1)

print factR(0)     #should be 1
print factR(1)     #should be 1
print factR(2)     #should be 2
print factR(3)     #should be 6
print factR(4)     #should be 24

#2.
def factW(n):
    ans=1          #sets up the answer if n=0 or n=1; also sets up while loop
    while n>1:
        ans=ans*n  #multiplies current ans by n
        n=n-1      #sets n to n-1 so that factorial could work
    return ans     #returns current answer

print factW(0)     #should be 1
print factW(1)     #should be 1
print factW(2)     #should be 2
print factW(3)     #should be 6
print factW(4)     #should be 24
