#don't work lol
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

#works
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast =0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


# might as well be o(n^2)
class Solution:
    def findDuplicate(self,nums):
        fast = 0
        slow = 0
        while True:
            fast += 2
            slow += 1
            fast = fast % (len(nums)-1)
            slow = slow % (len(nums)-1)
            if nums[fast] == nums[slow] and fast != slow:
                return nums[fast]
            