# needs DP, will return
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        cache[1] = 1
        cache[2] = 2
        def climb(n):
            if n <= 2:
                return n
            if n in cache:
                return cache[n]
            cache[n] = climb(n -1) + climb(n-2)
            return cache[n]
        climb(n)
        return cache[n]


print(Solution.climbStairs(None,2))

