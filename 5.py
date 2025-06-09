"""
they actually want the string, not just the len
sliding window seems relevant
we'll need to come up with a way to quickly determine if a string is a palindrome
it's at most o(n) to check that, so the solution would be around n^2?
palindromes can only have 2 chars added at a time
calculate a char, add 2 values, check it it's still palin
where do I start??????
start at middle
if m + 1 == m -1 then still palin
if NOT... not a palindrome anymore
bf: check for palindromes starting from every index
check starting from 1 and starting from 2
issues:
    - where tf do I start looking:
        - if s even, middle, if s odd:  middle 2
    - if it's no longer a palindrome where tf do I go
      - what information do I have to determine what value to check from next?
      - even if a value was used in a previous palin it could have been at the wrong offset
"""


# if the question was asking for len. I am stupid
# class SolutionInt:
#     def longestPalindrome(self, s: str) -> int:
#         longest = 0
#
#         def calculate_palin(start: int, end: int):
#             res = 0
#             while start - 1 > 0 and end + 1 < len(s) and s[start - 1] == s[end + 1]:
#                 res += 2
#                 start -= 1
#                 end += 1
#             return res
#
#         for i in range(len(s)):
#             longest = max(longest, calculate_palin(i, i))
#             longest = max(longest, calculate_palin(i, i + 1))
#
#         return longest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palin = ""

        def calculate_palin(start: int, end: int):
            res = s[start]
            if start != end and end < len(s) and s[start] == s[end]:
                res = s[start] + s[end]

            if end >= len(s) or s[start] != s[end]:
                return ""

            while start - 1 >= 0 and end + 1 < len(s) and s[start - 1] == s[end + 1]:
                res = s[start - 1] + res + s[end + 1]
                start -= 1
                end += 1
            return res

        for i in range(len(s)):
            res = calculate_palin(i, i)
            if len(res) > len(palin):
                palin = res

            res = calculate_palin(i, i + 1)
            if len(res) > len(palin):
                palin = res

        return palin


print(Solution.longestPalindrome(None, "aacabdkacaa"))
