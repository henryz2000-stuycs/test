def fib():
    ans = [1,2]
    ind = 2
    while max(ans) < 4000000:
        ans += [ans[ind-1] + ans[ind-2]]
        ind +=1
    ans = ans[:-1]
    return ans

print fib()

def even():
    new = fib()
    ans = []
    for x in new:
        if x % 2 == 0:
            ans += [x]
    return ans

print even()

print sum(even())
