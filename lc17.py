# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
'''
return all: backtracking
make choice for first non-letter
backtrack and make other choice
once no numbers left append to output
'''

class Solution:
	def letterCombinations(self, digits: str):
		mapping = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
		output = []
		if digits == "": return []
		def choice(curr_string,i):
			if i == len(curr_string):
				output.append(''.join(curr_string))
			else:
				for letter in mapping[curr_string[i]]:
					number = curr_string[i]
					curr_string[i] = letter
					choice(curr_string,i+1)
					curr_string[i] = number
		choice(list(digits),0)
		return output

print(Solution.letterCombinations(None,'23'))

			
