class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        made = set()
        def helper(curr,remaining):
            if len(curr) == len(nums):
                tuplecurr = tuple(curr)
                if tuplecurr not in set():
                    set.add(tuplecurr)
                    output.append(curr.copy())
                return
            looper = remaining.copy()
            for num in looper:
                curr.append(num)
                remaining.remove(num)
                helper(curr,remaining)
                curr.remove(num)
                remaining.append(num)
        helper([],nums.copy())
        return output
        