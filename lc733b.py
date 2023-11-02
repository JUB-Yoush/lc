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
			image[y][x] = color
			if y+1 < len(image[0]) -1 and image[y+1][x] == prev_color:
				checkNextTo(y+1,x)
			if y-1 > -1 and image[y-1][x] == prev_color:
				checkNextTo(y-1,x)
			if x+1 < len(image) -1 and image[y][x+1] == prev_color:
				checkNextTo(y,x+1)
			if x-1 > -1 and image[y][x-1] == prev_color:
				checkNextTo(y,x-1)
		checkNextTo(sr,sc)
		return image

answer = Solution()
print(answer.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))