#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''
move values in array without overwriting it
if checking for dupes then use a set
if elements are in increasing order then set isn't nessicary
if duplicate found then remove and shift all values to the left
k is size of set at the end
'''
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		unique_nums = set()
		for i,num in enumerate(nums):
			if nums[i] != None and i != 0 and nums[i-1] == nums[i]:
				# duplicate found
				nums[i] = None
				curr_num_index = i
				# if you aren't at the end of the list and there are numbers to your right, swap
				while curr_num_index+1 < len(nums) and nums[curr_num_index] != None:
					#swap values
					temp = nums[curr_num_index]
					nums[curr_num_index] = nums[curr_num_index+1]
					nums[curr_num_index+1] = temp
					curr_num_index += 1 # move to next number
		k = 0
		for num in nums:
			if num != None:
				k+= 1
		return k
			
# soln from leetcode
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:		
		j = 1
		for i in range(1,len(nums)):
			if nums[i] != nums[i-1]:
				nums[j] = nums[i]
				j += 1
		return j
