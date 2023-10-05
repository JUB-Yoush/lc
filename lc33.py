def search(nums,target):
	l = 0
	r = len(nums) -1
	# l is always larger then r, if not then it's not cut anywhere and r is the max
	m = (l + r)//2
	while r > l:
		#if nums[m] > nums[r]: #if m < r then  cut is after m, move to m-r 
		if target > nums[m] or target < nums[r]:
			l = m
			m = (l + r)//2
			if nums[m] == target:
				return m
		if target < nums[m] or target > nums[l]:
			r = m
			m = (l + r)//2
			if nums[m] == target:
				return m
	return -1
	
print(search([4,5,6,7,0,1,2],3))