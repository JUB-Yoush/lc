class Solution:
    def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()  # sort array, skip duplicates to prevent duplicates in the output set

        # edge cases
        if len(nums) < 3:
            return []
        if nums[0] > 0:
            return []

        output = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            b = i + 1
            c = len(nums) - 1
            while b < c:
                if a + nums[b] + nums[c] == 0:
                    output.append([a, nums[b], nums[c]])
                    b += 1
                    while nums[b] == nums[b - 1] and b < c:  # skup duplicates
                        b += 1
                if a + nums[b] + nums[c] > 0:
                    c -= 1
                if a + nums[b] + nums[c] < 0:
                    b += 1
        return output


print(threeSum([-1, 0, 1, 2, -1, -4]))
