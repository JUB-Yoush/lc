"""
loop left to rigth
map symbol to values
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and symbol_map[s[i + 1]] > symbol_map[s[i]]:
                res += symbol_map[s[i + 1]] - symbol_map[s[i]]
            else:
                res += symbol_map[s[i]]
            i += 1
        return res
