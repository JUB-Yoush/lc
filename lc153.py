def findMin(nums):
	l = 0
	r = len(nums) -1
	# l is always larger then r, if not then it's not cut anywhere and r is the max
	if r > l:return r # not cut edge case
	m = (l + r)//2
	while r != l:
		if nums[m] > nums[r]: #if m < r then  cut is after m, move to m-r 
			l = m
			m = (l + r)//2
			if num[m-1] > nums[m]:
				return nums[m]
		if nums[m] < nums[r]:
			r = m
			m = (l + r)//2
			if num[m-1] > nums[m]:
				return nums[m]
	return nums[m]
	
print(findMin([3,4,5,1,2]))