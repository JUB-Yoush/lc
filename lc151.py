class Solution:
    def reverseWords(self, s: str) -> str:
            words = s.split()
            output = ""
            for i in range(len(words)):
                output += words[len(words)-1 - i]
                if i != len(words) -1:
                    output += " "
                    
            return output
        
'''
def wordflip2(s):
	index = 0
	words = []
	while r < len(s):
	curr_word = ''
	while s[r] != " " or r == len(s) -1:
		if r== "\" and r < len(s) -2 and s[r+1] == 'n'
			break
		curr_word += s[r]
		r+= 1	
		len(curr_word) > 0:
		words.append(curr_word)
		while s[r] == " " and r < len(s):
			r += 1
				output = ""
			for i in range(len(words)):
				output += words[len(words)-1 - i] 
			return output

'''