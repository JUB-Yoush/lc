class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                seek = (x + y) * -1
                print(x, y, seek)
                if (
                    nums.count(seek) != 0
                    and i != j
                    and nums.index(seek) != i
                    and nums.index(seek) != j
                ):
                    if [x, y, nums.index(seek)] not in res:
                        res.append([x, y, nums.index(seek)])
                        print("value added")
        return res


print(Solution.threeSum(None, [-1, 0, 1, 2, -1, -4]))
