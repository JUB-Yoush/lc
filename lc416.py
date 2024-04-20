#https://leetcode.com/problems/partition-equal-subset-sum/
'''
group the numbers in any way I want to
sort the array 
have a sum as an interger
loop and decrement
if leftsum == right sum return true, if leftsum > rightsum before == then false
nlogn time, n space
not dp'ey
just worried about t or f, not the actual subsets
so proving that one could be possible works
every additional number would need to be equal to the existing sum 
or the sum of all extra values would eventually need to match the sum of the values that last were even
but how do I check if values were even to begin with?

'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool: