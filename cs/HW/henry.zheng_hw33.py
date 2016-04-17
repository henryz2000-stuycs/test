def vBarGraphify(nums):
    ind = 0
    ans = "\n"
    while sum(nums) > 0:
        if nums[ind] == 0:
            ans += " "
        if nums[ind] > 0:
            ans += "*  "
            nums[ind] -= 1
        if ind == len(nums) - 1:
            ans += "\n"
            ind = 0
        else:
            ind += 1
    ans += "0 1 2 3"
    print ans

vBarGraphify([0,1,2,3])
vBarGraphify([1,0,3,2])
