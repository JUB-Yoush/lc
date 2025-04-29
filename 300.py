# longest subsequence at n is the longest subsequence where the final value is less than n +1
#
class Solution:
    def lengthOfLIS(self, nums):
        subseqs = [-1] * len(nums)
        highest = 1

        def helper(i) -> int:
            # cache
            nonlocal highest
            current_max = 1
            if subseqs[i] != -1:
                return subseqs[i]

            for j in range(i, len(nums)):
                if nums[j] > nums[i] and j > i:
                    current_max = max(current_max, helper(j) + 1)
            subseqs[i] = current_max
            highest = max(highest, subseqs[i])

            return subseqs[i]

        for i in range(len(nums)):
            helper(i)

        return highest


sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
