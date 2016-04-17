def makeprime():
    ans = [2]
    start = 3
    while len(ans) < 1000:
        if all(start % x != 0 for x in ans):
            ans += [start]
        start += 1
    return ans
    
print makeprime()

def reverse():
    test = makeprime()
    test.reverse()
    return test

print reverse()

def test1():
    for x in reverse():
        if 600851475143 % x  == 0:
            return x

print test1()
