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

the solution:
if we decide to rob the first house, we can rob all houses from 2-n (not the 1th house)
or we can skip the first house and rob the [1] house
we'll pick whichever one gives us the most money
max = (arr[0] + arr[2:n],arr[1:n])
in a base case of two houses, [1,2]
we can chose to rob first house and everything afterwards (there is nothing)
or pass on house one and iterate on next house
next house is two 
returns two 
two is greater than one so max returns 2
in the case [1,2,3,1]
you can pick 1, and [3,1]
	- you can pick 1 + 3
	- or pick 1 + rob([1])
	
or pick [2,3,1]

wait nvm
let's walk though a test case using the neetcode soln

rob1 = 0
rob2 = 1
temp = max(rob1,rob2) == 1

for n in nums


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
	
				


			


