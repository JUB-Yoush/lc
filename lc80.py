#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''
two pointer solution because that's what the tag says lmfao
I need to remove when there is more then three of them
they're sorted
so when l and r point to the same number and there is a gap between them, 
the value in the middle is the same
push extra to end of array
how to move l and r?
in the case of 11199999999999999999999
l would pass 1s before matching w r
in the case we remove those values
1119999
xxlxrxx
they hit the middle before getting to any mathcing values
cringe
how to move them so they don't miss out on values???
problems to solve
- how do we know when there is more then 3 of a number: l and r are on them and there is a value in between 
	- how do we move l and r so that they'll line up on matching values?
	- we can't remember
- how to remove extras: pass values up array
- how do we then know there is only two after modification: l and r are next to each other 
	- and it's opposite siblings aren't pointing at that number
bf:
- check if the values i-1 and i-2 are the same number:
- then remove one and keep checking until it's false (no more then two of that num)
- array IS sorted
- so l = 0 r = len generally
- but matching values would be next to each other
- no start at l= 0 r = 0
- r goes up and checks when it's no longer equal to l
- get the distance between them (r-1-l)
- if the distance is more than 1 then there's a 3rd!!!
- while loop through and remove all the middle values
- move l up to r

111223|
lxxrxx|x
'''
class Solution1:
	def removeDuplicates(self, nums):
		nums.append(None)
		l = 0
		r = 0
		while r < len(nums) and nums[r] != None:
			if nums[l] == nums[r]:
				r += 1
			else:
				r = r-1 
				while (r - l) >=2:
					'''
					pick one of the values in between 
					make it None
					move to end
					'''
					extra_dupe = r-1
					nums.pop(extra_dupe)
					nums.append(None)
					r-= 1
				r+=1
				l = r
		count = 0
		for num in nums:
			if num != None:
				count+= 1
		return count

class Solution:
	def removeDuplicates(self, nums):
		l = 0
		r = 0
		while r < len(nums) and nums[r] != None:
			if nums[l] == nums[r]: 
				if (r-l) < 2:
					r += 1
				else: #remove extra as soon as we find it
					extra_dupe = r-1
					nums.pop(extra_dupe)
					nums.append(None)
					
			else:
				l = r
				
		count = 0
		for num in nums:
			if num != None:
				count+= 1
		return count
	
print(Solution.removeDuplicates(None,[1,1,1,1,2,2,2,3,3]))
