#https://leetcode.com/problems/house-robber/
'''
iconic leetcode
it's a dp problem
I'm not exactly sure how though 
bf:
- start at 0 and at 1
- get the sum of all odd and all even houses
- pick the larger sum?
where is the repeated work?
pick house, then add that house with the max you can get from not that houses neighbors 
memoize by making the key of the cache a list of the indexes of houses?
{[0,2,4]:10} for example
lets try making it without memoization then adding it afterwards

pick a house
calculate the sum of that houses value + all the houses you can get that aren't attached
123134
1x3134
1x3x34
1x3x3x
check at house
find remaining houses
loop until empty
check house
if > max_sum then update
pop house

'''
# 	WHAT
class Solution:
	def rob(self, nums: List[int]) -> int:
		rob1,rob2=0,0
		for n in nums:
			temp = max(n+rob1,rob2)
			rob1 = rob2
			rob2 = temp
		return rob2
      

				
				


			


