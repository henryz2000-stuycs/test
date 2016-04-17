def sum3():
    x = 0
    ans = []
    while x*3 < 1000:
        ans += [3*x]
        x += 1
    return ans

print sum3()

def sum5():
    x = 0
    ans = []
    while x*5 < 1000:
        ans += [5*x]
        x += 1
    return ans

print sum5()

def total():
    ans = sum3() + sum5()
    for x in ans:
        if ans.count(x) > 1:
            ans.remove(x)
    return ans

print total()

print sum(total())
