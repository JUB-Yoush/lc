#https://leetcode.com/problems/sort-an-array/
'''
insertion sort:
loop through the entire array from l - r
j = i
while j > -1 and num[j] > num[i] # out of order
swap j n i values
'''
class Solution1:
	def sortArray(self,nums):
		for i in range(1,len(nums)):
			j = i-1
			while j >= 0 and nums[j+1] < nums[j]:
				temp = nums[j+1]
				nums[j+1] = nums[j]
				nums[j] = temp
				j-= 1
		return nums

#nvm we need merge sort
#maintain the array throughout so it's good w space complexity
'''
split the array indexes in half
if s and e (start and end) are 1
re-construct the arrays
'''
class Solution:
	def sortArray(self,nums):
		def mergesort(nums,s,e):
			if e-s +1 <= 1:
				return nums
			#middle index of the array
			m = (s + e) //2
			
			mergesort(nums,s,m)
			mergesort(nums,m+1,e)
			merge(nums,s,m,e)

		def merge(nums,s,m,e):
			

			nums_pos = s
			l_pos = 0
			r_pos = 0
			while l_pos < len()

			



	
sol = Solution			
print(sol.sortArray([5,2,3,1]))