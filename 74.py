# https://leetcode.com/problems/search-a-2d-matrix/description/
"""
iterate over 0th value of each row
if row[i][0] is greater than target, then the value would have to be in row[i-1][0]
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binsearch(arr):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < target:
                    low = mid + 1
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    return True
            return False

        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] < target:
                if matrix[mid][-1] > target:
                    return binsearch(matrix[mid])
                low = mid + 1
            elif matrix[mid][0] > target:
                # if matrix[mid][-1] < target:
                #     return binsearch(matrix[mid])
                high = mid - 1
            else:
                return True
        return False


print(
    # Solution.searchMatrix(None, [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    Solution.searchMatrix(None, [[1, 3]], 3)
)
