"""
okay question dont seem to hard
only returning length of array... smells like dp
get the longest subarray from each value?
including value rather
to include i to i+1's subarr we'd have to check if i+1 and i+2's comp is diff then i and i+1 comp?
we need to figure out if we can include a value into an existing subarray
so it's 1+ i+1s IF it can fit?
4 possible end types
> < = or nothing because it's the 0th or nth value
we need to record the starting and ending comparitor of every possible subarray starting at a value
the first and last ones are what dictate when a subarray starts or ends
loop over all values
just slide the window dude
"""


class Solutionbad:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        def get_comparitor(l, r):
            if l < 0 or r > len(arr) - 1:
                return "oob"
            if arr[l] > arr[r]:
                return ">"
            if arr[l] < arr[r]:
                return "<"
            if arr[l] == arr[r]:
                return "="

        def compare_comparitors(c1, c2):
            if c1 == "<" and c2 == ">":
                return True
            if c1 == ">" and c2 == "<":
                return True
            if c1 == "oob" and c2 != "=":
                return True
            if c1 != "=" and c2 == "oob":
                return True
            return False

        prevcomparitor = "oob"
        comparitor = ""
        record = 0
        curr = 0
        L = 0
        R = 1
        while R < len(arr):
            comparitor = get_comparitor(R - 1, R)
            if compare_comparitors(comparitor, prevcomparitor):
                curr += 1
            else:
                record = max(record, R - L)
                L = R
            prevcomparitor = comparitor
            R += 1

        return record


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - 1 + 1)
                r += r - 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""
        return res
