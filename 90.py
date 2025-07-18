class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        subsets = set()
        nums.sort()

        def pick(i, picks: list[int]):
            if set(picks) not in subsets:
                subsets.add(tuple(picks))
            if i == len(nums):
                return
            picks.append(nums[i])
            pick(i + 1, picks)
            picks.pop()
            pick(i + 1, picks)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            pick(i + 1, picks)

        pick(0, [])
        return list(subsets)


print(Solution.subsetsWithDup(None, [1, 2, 2]))
