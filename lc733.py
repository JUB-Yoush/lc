class Solution:
	def floodFill(self,image,sr,sc,color):
		"""
		smells like recursion 
		recursivley check all 4 neighbours
		if not same int then skip
		else change to new interger
		"""
		prev_color = image[sr][sc]
	
		def checkNextTo(y,x):
			if 0 >x or x > len(image[0]) -1: return
			if 0 > y or y > len(image) -1: return
			if image[y][x] != prev_color:return
			image[y][x] = color
			checkNextTo(y+1,x)
			checkNextTo(y-1,x)
			checkNextTo(y,x+1)
			checkNextTo(y,x-1)
		checkNextTo(sr,sc)
		return image

answer = Solution()
print(answer.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))