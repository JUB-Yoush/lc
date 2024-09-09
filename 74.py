# https://leetcode.com/problems/search-a-2d-matrix/description/
"""
search left side
if l is smaller and r is greater then the l array would have target
pass in that row into binsearch
"""
class Solution(object):
    def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        high = len(matrix)
        low = 0
        mid = (high+low)//2
        target_arr_index = None
        while low <= high:
            mid = (low+high)//2
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                target_arr_index = mid
                break
            elif matrix[mid][0] > target and matrix[mid][-1] > target:
                high = mid -1
            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                low = mid +1
        if target_arr_index == None:
            return False

        nums = matrix[target_arr_index]
        high = len(nums)
        low = 0
        mid = len(nums) // 2

        while low <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return False


print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
