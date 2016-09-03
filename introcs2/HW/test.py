def numRealRoots(a,b,c):
    if b**2 - 4*a*c > 0:
        return 2
    elif b**2 - 4*a*c == 0:
        return 1
    else:
        return 0
    
print numRealRoots(1,2,3)
print numRealRoots(2,4,2)
print numRealRoots(1,3,2)

def quadSolver(a,b,c):
    if numRealRoots(a,b,c) == 0:
        print "no real roots"
    elif numRealRoots(a,b,c) == 1:
        print (-b + (b**2 - 4*a*c)**(1.0/2)) / 2*a
    else:
        print (-b + (b**2 - 4*a*c)**(1.0/2)) / 2*a , (-b - (b**2 - 4*a*c)**(1.0/2)) / 2*a
        
quadSolver(1,2,3)
quadSolver(1,4,4)
quadSolver(1,-2,-15)
