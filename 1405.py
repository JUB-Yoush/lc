"""
no more than 3 in a row
have to use the given amount of each
do a modulo thingy
use a heap?
pick the one with the most, add two of them
repeat for a different one
if there are less than two add the one
if there is only letter left to pick then add two of them
bf: backtracking

when is a string NOT happy:
    it dosen't use abc (trivial)
    it has 3 of a,b, or c in a row:
        check the previous two values -1 and -2 to make sure there are no triplets
    at most var x occurances of x:
        count how many are currently in the string, subtract from some variable

pick the higest value (if triplet wouldn't be formed)
subtract from variable
repeat
"""


# works
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""

        def get_choice_key():
            curr = ""
            for key, value in stock.items():
                if value > stock[curr] and (
                    len(res) < 2 or (len(res) >= 2 and res[-1] + res[-2] != key + key)
                ):
                    curr = key
            return curr

        stock = {"": 0, "a": a, "b": b, "c": c}
        choice_key = get_choice_key()
        while choice_key != "":
            stock[choice_key] -= 1
            res += choice_key
            choice_key = get_choice_key()

        return res


print(Solution.longestDiverseString(None, 1, 1, 7))
