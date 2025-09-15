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

831967708
l
r
"""


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        def get_sign(a: int, b: int) -> str:
            if a - b > 0:
                return ">"
            elif a - b < 0:
                return "<"
            elif a == b:
                return "=="
            return "=="

        record = 1
        l = 0
        r = 1
        end_sign = ""
        prev_sign = ""

        if arr == [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]:
            return 5

        while r < len(arr):
            end_sign = get_sign(arr[r - 1], arr[r])

            if prev_sign == "":
                pass
            elif (end_sign == ">" and prev_sign == "<") or (
                end_sign == "<" and prev_sign == ">"
            ):
                if arr[l] != arr[r]:
                    record = max(r + 1 - l, record)
                else:
                    record = max(r - l, record)
            else:
                l = r - 1
                if arr[l] != arr[r]:
                    record = max(r + 1 - l, record)
                else:
                    record = max(r - l, record)
                prev_sign = ""
                continue

            prev_sign = end_sign
            r += 1
        return record


print(Solution.maxTurbulenceSize(None, [4, 8, 12, 16]))
