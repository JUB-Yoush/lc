import string
def characterReplacement(s,k):
	count = dict(zip(string.ascii_uppercase, [0]*26)) 
	l = 0
	r = 0
	res = 0
	count[s[r]] += 1
	while r < len(s):
		window_size = r-l
		most_num = count[max(count, key=lambda q: count[q])]
		biggest_window = window_size - most_num
		if biggest_window <= k: # if valid window
			res = r-l
			r+= 1
			if r < len(s):
				count[s[r]] += 1
		else:
			l+=1
			count[s[l]] -=1
			res = r-l
	return res


print(characterReplacement('ABAB',2))