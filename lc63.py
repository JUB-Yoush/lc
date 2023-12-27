#https://leetcode.com/problems/unique-paths-ii/
'''
how do the rocks change our strategy?
check if m-1 or n-1 has a rock there
if so don't calculate it
so we'd need to calculate the right paths and down paths as different values?

'''
#fix it
class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid) -> int:
		cache = {}
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		def step(m,n):
			if obstacleGrid[m][n] == 1 and min(m,n)>0:
				cache[(m,n)] = 0
				return cache[(m,n)]
			if n == 1 or m == 1:
				cache[(m,n)] = 1
				return cache[(m,n)]
			if (m,n) in cache:
				return cache[(m,n)]	
			cache[(m,n)] = step(m-1,n) + step(m,n-1)
			return cache[(m,n)]	
		step(m,n)
		return cache[(m,n)]