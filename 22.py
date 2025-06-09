"""
rules for well formed paren
- right can never be more than left
- right and left must equal n
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def helper(r, l, curr: str):
            # base case
            if r == n and l == n:
                res.append(curr)
                return

            # can only add right when added all lefts
            if l == n:
                curr += ")"
                helper(r + 1, l, curr)

            # if equal only add left
            elif l == r:
                curr += "("
                helper(r, l + 1, curr)

            # add right or left
            elif r < l and l < n:
                curr += "("
                helper(r, l + 1, curr)
                curr = curr[:-1]
                curr += ")"
                helper(r + 1, l, curr)

        helper(0, 1, "(")
        return res


print(Solution.generateParenthesis(None, 3))
