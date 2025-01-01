#https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
"""
goal is to make as many numbers the same as possible
relationship between numbers and difference between them
[1,2,4]
[[0,1,3][-1,0,2][-3,-2,0]]
we can only increment, so negative differences are worthless
sort differences by minimum size, apply k to smallest first
looping over each numbers relationship to another number is really slow
it's right angle triangle time (half of a square, still not good)
does hashing help
take the number with the mode lowest positive numbers?
consider biggest elements smaller than or equal to this value
[1,1,1,1,5,6,7,7] 9
[0,0,0,0,4,5,6,6]
...
[x,x,x,x,0,1,2,2]
[x,x,x,x,x,0,1,1]
nvm I'm dumb neetcode solution
"""

