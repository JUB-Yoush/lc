from collections import deque 
#https://leetcode.com/problems/word-ladder/
'''
one letter changes at a time?
I'd change one letter and then check if that letter exists in the word list?
no because we need to work our way to the end word
treat every word as a node? it's a graph?
form adjacency list using words (each one is bi-directional)
preform bfs to find shortest path
'''

class Solution:
	def ladderLength(self, beginWord: str, endWord: str, wordList):
		wordlen = len(wordList[0])
		wordList.append(beginWord)
		adj_list = {}
		for word in wordList:
			adj_list[word] = []
		
		# make edges (check if one word is one letter off from another)
		for word in wordList:
			for otherword in wordList:
				if word == otherword: continue
				# they're one letter off
				if len(set(word).intersection(set(otherword))) == wordlen -1:
					adj_list[word].append(otherword)
		
		queue = deque()
		visited = set()
		visited.add(beginWord)

		min_distance = 0
		distance = 1
		queue.append(beginWord)
		# if it has no edges and it's not the final word then it's not in our route
		while queue:
			for i in range(len(queue)):
				word = queue.popleft()
				for edge in adj_list[word]:
					if edge not in visited:
						visited.add(edge)
						queue.append(edge)
					if edge == endWord:
						return distance +1
			distance+= 1
		return 0

print(Solution.ladderLength(None,'a','c',['b','c']))
		


				


