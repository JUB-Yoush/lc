class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash list
        # check if target - num exists in the hashmap
        for i,num in enumerate(nums):
            if nums.count(target-num) > 0 and nums.index(target-num) != i:
                return [nums.index(target-num),i]
        