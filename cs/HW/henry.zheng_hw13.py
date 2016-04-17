#Henry Zheng
#IntroCS2 pd8
#HW13 -- The Handoff
#2016-03-11

def discriminant(a,b,c):            #makes code for other functions easier to read
    return b**2 - 4*a*c

print discriminant(1,4,4)
print discriminant(1,-2,-15)

def numRealRoots(a,b,c):
    if discriminant(a,b,c) > 0:     #when discriminant is greater than 0, there are 2 real roots
        return 2
    elif discriminant(a,b,c) == 0:  #when discriminant is equal to 0, there is 1 double root
        return 1
    else:                           #when discriminant is less than 0, there are no real roots
        return 0
    
print numRealRoots(1,2,3)
print numRealRoots(2,4,2)
print numRealRoots(1,3,2)

def sqrt(x):                        #makes code for quadSolver easier to read
    return x**(1.0/2)

print sqrt(1)
print sqrt(64)

def quadSolver(a,b,c):
    if numRealRoots(a,b,c) == 0:    #can't solve a quadratic under real number system if there are no real roots
        print "no real roots"
    elif numRealRoots(a,b,c) == 1:  #if the number of real roots is equal to 1, that means that there is one double root, so both -b + and -b - would give the same solution
        print (-b + sqrt(discriminant(a,b,c))) / (2*a)
    else:                           #else, there must be two real roots, so we must print both -b + and -b - solutions
        print (-b + sqrt(discriminant(a,b,c))) / (2*a) , (-b - sqrt(discriminant(a,b,c))) / (2*a)
        
quadSolver(1,2,3)
quadSolver(1,4,4)
quadSolver(1,-2,-15)
