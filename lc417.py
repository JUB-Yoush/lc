#https://leetcode.com/problems/pacific-atlantic-water-flow/
'''
the bf approach would be to check if very value at every position can reach both oceans
but there is some repeated work there, if there is a row [1,2,3,2,1] then when we find that 3 can make it to both, 
wait nvm
in that example 1 and 2 couldn't pass 3
if n can make it to an ocean then all the values it traversed can also make it to that ocean
we wouldn't need to check them
we can keep a set of all the values traversed, once the branch is able to make it to an ocean append it to a atlantic or pacific set
return the intersection of both sets (only the values that can atlantic and pacific)
brb blowing nose
damn my nose was full 
anyway 
yeah two sets
loop through every value, 
check if it's in either set
if it's not, we haven't checked at it before
although we'd want to have a generic checked list
because we could check somthing but only checked for one ocean 
so in the case we check a value
we recursivley try to navigate in all 4 direction, managing the values along the path
if we reach an ocean, append all values to that oceans set

go through each edge and append them to their sets
check for each value in that row if other values are able to 
'''
class Solution:
	def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
		ROWS, COLS = len(heights), len(heights[0])
		pacific,atlantic = set(),set()
		for c in range(COLS):
			pass

