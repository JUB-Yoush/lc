#https://leetcode.com/problems/trapping-rain-water/
'''
first hard.
based on intuition, what do I know:
- i'll need two pointers
- rain always picks the lower of two values
- it's like the squares question kinda
- I need to keep track of all values i think
- it's about changes in elevation
- having a u shape leads to water collection
- so it's about calculating the dips in elevation from the highest values

LAW:
- if the next value is lower, you collected at least (you - next) rain
- you collect rain so long as all the values are less than (you)
- x is the value before the dip
- have pair pointers 
- r go up and if not lower then l follows
- if r is lower then add diff to rain count
- repeat until r is equal to l
- then move r to match l
0,1,0,2,1,0,1,3,2,1,2,1
x,l,x,x,x,x,x,x,x,x,x,x
x,r,x,x,x,x,x,x,x,x,x,x
'''

'''
has the issue of assuming all u's will be closed
I'll need to:
- pair pointers with l and r
- when you find a dip, while loop through w r until you find another height that can match l
- if there is one, then loop back over and collect rain?

- lr pointers
- if r is less than l, loop through until a height of at least equal to l is found again
- if so, we collected the rain from then to there
- collect that rain and move l back to r
'''
class Solution1:
	def trap(self, height):
		l,r=0,0
		water = 0
		while r < len(height)-1:
			if height[r+1] >= height[l]:
				r += 1
				l = r
			else:
				r += 1
				potential_water = 0
				is_basin = True
				while height[r] < height[l]:
					potential_water += (height[l] - height[r])
					r+= 1
					if r == len(height):
						is_basin = False
						break
				if is_basin:
					water += potential_water 
					l = r
				else:
					l+=1
					r = l
		return water

# wow my solution was absolutley off
class Solution1:
	def trap(self, height):
		l,r = 0,len(height) -1
		left_max, right_max = height[l], height[r]
		res = 0
		while l<r:
			if left_max < right_max:
				l+= 1
				left_max = max(left_max,height[l])
				res += left_max - height[l]
			else:
				r -=1
				right_max = max(right_max,height[r])
				res += right_max - height[r]
			return res
		


print(Solution.trap(None,[4,2,3]))