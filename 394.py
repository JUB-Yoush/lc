import re


class Solution:
    def decodeString(self, s):
        opening_index = None
        last_word = 0
        digit = None
        res = ""
        for i, c in enumerate(s):
            if c == "[":
                print(f"digit {s[last_word:i]}")
                digit = int(s[:i])
                opening_index = i
            if c == "]":
                last_word = i + 1
                word = s[opening_index + 1 : i]
                res += word * digit
                print(res)
                s = s[i + 1]
                print(s)
        return res
