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

'''
use a real dp approach
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [] * len(n) +1
        starprev1 = 1
        starprev2 = 1
        for i in range(n-1):
            new_stair = starprev1 + starprev2
            temp = starprev2
            starprev2 = new_stair
            starprev1 = temp
        return starprev2

    
