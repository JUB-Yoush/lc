def findDuplicate(nums) -> int:
    t:int = 0
    h:int = 0
    firstloop = True
    num:int = 0
    foundnum:bool = False
    while (not foundnum):
        t += 1
        if t == len(nums): t = 0
        if nums[t] == nums[h] and t != h:
            num = nums[t]
        # wrap to avoid going out of bounds
        h += 2
        if h == len(nums): h = 0
        if h == len(nums) +1: h = 1
        if nums[t] == nums[h] and t != h:
            num = nums[t]
            foundnum = True
    return num


print(findDuplicate([3,1,3,4,2]))