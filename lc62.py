#fake dp :pensive:
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		cache = {}
		def step(m,n):
			if n == 1 or m == 1:
				cache[(m,n)] = 1
				return cache[(m,n)]
			if (m,n) in cache:
				return cache[(m,n)]	
			cache[(m,n)] = step(m-1,n) + step(m,n-1)
			return cache[(m,n)]	
		step(m,n)
		return cache[(m,n)]
		