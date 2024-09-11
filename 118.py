#https://leetcode.com/problems/pascals-triangle/description/
"""
we're making a new number for every in between value
"""
class Solution:
    def generate(self, numRows):
        output = []
        output.append([1])
        for _ in range(numRows-1):
            prevRow = output[-1]
            row = []
            l = -1
            r = 0
            prevRow.append(0)
            for _ in range(len(prevRow)):
                value = prevRow[l] + prevRow[r]
                l+=1
                r+=1
                row.append(value)
            prevRow.pop()
            output.append(row)
        return output

print(Solution.generate(None,5))