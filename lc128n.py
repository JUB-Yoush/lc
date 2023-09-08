import heapq
def longestConsecutive(nums: list[int]) -> int:
	max_chain = 1 # a num by itself is a chain of 1
	heapq.heapify(nums)
	chain = 1
	lowest = heapq.heappop(nums)
	second_lowest = heapq.heappop(nums)

	while len(nums) > 0:
		if lowest == second_lowest - 1 or lowest == second_lowest:
			chain += 1
		else:
			max_chain = max(max_chain,chain)
			chain = 1
		lowest = second_lowest
		second_lowest = heapq.heappop(nums)
	
	max_chain = max(max_chain,chain)
	return max_chain

print(longestConsecutive([0,-1]))
        
