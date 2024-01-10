#https://leetcode.com/problems/min-cost-climbing-stairs/
'''
at every step I can climb the n+1 step or the n+2 step
if n+2 or +1 is out of bounds, then I can reach the top
[10,15,20]
climb 15 then climb oob, only paid 15
return the lower cost of n+1 and n+2
oob is 0
base case:
	- if there is no steps then I pay 0 and go up
	- if there is only 1 step left I can go up 2 and pay 0
	- if there are 2 steps left then I can pick the cheaper between the two 
	- 3 steps is where the fun begins
	- I would need to caculate the costs of current step price + the steps afterwards
	- unlike house robber there are no gaps to consider, just cost min(n + [n+1:],n+[n+2:])

[1,100,1,1,1,100,1,1,100,1]
pick 1, then pick value 1 or two higher that is the lowest between them
how many values would we have to manage?
okay for this one we can use an array 
but what would go in the array?
we'd need to calculate the minimum amount of money we'd need to spend
[10,15,20,10,5]
at every step we pick the lower between the next two values
[10,20,99]
keep track of sum if we went 1 and sum if we went 2
sum1 = 10
sum2 = 20
temp = min()
start at the top
cacluate the cost from the top step and the top-1 step
store those values then calcualte the previous two
'''

'''
we're so back
base case. there is 1 step
you can start at step [1] and pay nothing
I don't think there will ever be 1 step
2 steps
you pick the lower between the two steps
and then from there going to n+1 or n+2 would be the top

3 steps is where more then one decision is made
[10,15,20,0]
I could either start at 10 or 15
what would influence that decision
the total cost of the current step + all my future options
in the climb stairs problem just take the last two and sum them up

'''

class Solution:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		dp = [0] * 2
		for c in reversed(cost):
			curr_cost = c + min(dp[0],dp[1])
			dp[0] = dp[1]
			dp[1] = curr_cost
		return min(dp[0],dp[1])
			



