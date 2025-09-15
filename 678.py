"""
count number of left and right brackets
if even, any * is empty
if odd, can we use any * to fill in?
as long as we start with a opening ( it should be solvable
count from left to right
if closed is ever more than open and there not enough wilds to make up the difference, we're cooked
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
                                    count ={"(":0,")":0,"*":0,}
        good = True
        for c in s:
            
                                    

