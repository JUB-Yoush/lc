class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums)
        low = 0
        mid = len(nums) // 2

        while low <= high:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                low = mid + 1
                mid = (low + high) /2
            elif nums[mid] < target:
                high = mid - 1
                mid = (low + high) /2
        return -1
