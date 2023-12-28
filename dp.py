def dpProblem(nums):
	dp = [] * len(nums) + 1
	dp[0] = 0 #fill in base cases
	dp[1] = nums[0] 
	for n in nums:
		# do some sort of calculation
		# only the top n values are relevant at a time (usually 2), so you could store those instead of managing everything
		pass
	return dp[-2] # 2nd last value has what we need?

     