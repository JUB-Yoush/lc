#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"""
loop from final value back to front
maintain a list of highest values for each index
that's the answer wait
[17,18,5,4,6,1]
[18,18,6,6,6,1]
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest = 0
        highest_list = [0] * len(arr) -1
        for i,num in reversed(enumerate(arr)):
            highest = max(highest,num)
            highest_list[i] = highest
        
        highest_list.pop(0)
        highest_list.insert(len(highest_list),-1)
        return highest_list
        
        
