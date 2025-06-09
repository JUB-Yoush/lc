"""
at least two numbers
numbers must sum up to n
make numbers as square as possible
6*6 = 36
1*11 = 11
2*10 = 20
divide them as evenly as possible
3*3*3*3 = 81
wait square numbers???
mutliplying
7:
3 * 2 * 2 = 12
8:
4^2
2^4
9:

"""

"""
we recursivley break down numbers into two parts, 
and then we multiply them together with what was calculated previously
"""


# neet
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}

        def dfs(num):
            if num in dp:
                return dp[num]

            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]

        return dfs(n)


# neet
class Solutiondp:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}

        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num - 1]

        def dfs(num):
            if num in dp:
                return dp[num]

            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]

        return dfs(n)
