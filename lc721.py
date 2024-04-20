class Solution:
	def accountsMerge(self, accounts):
		users = {} #username: set(emails)

		for account in accounts:
			if account[0] not in users:
				users[account[0]] = set()
			for i in range(1,len(account)):
				users[account[0]].add(account[i])
			
		output = []

		for user,emails in users.items():
			output_subarry = []
			ouput_subarry.append(user)

			for email in emails:
				ouput_subarry.append(email)
			output.append(output_subarry)


		return output

'''
in this version, multiple people can have the same names
so we need to treat each email as a node and names as edges?
no
the other way around
emails are nodes
they're attatched to other nodes
do a dfs to find all neighbors, that's a whole account

find a name
if name not in set then it's a new person
collect all the emails
check if that email set and the existing email set have any overlap
if yes then merge
if no then new person


'''
class Solution:
	def accountsMerge(self, accounts):
		names_visited = set()
		output = {}
		for account in accounts:
			name = account[0]
			# if new name then add all values to set
			if account[0] not in names_visited:
				output[name] = set()
				for i in range(1,len(account)):
					output[name].add(account[i])
			else: #if existing name, collect all emails in this account, them compare to the set of existing emails.
				# merge if any overlapping values
				# store their name as namex x being an interger?



# graph sol
class Solution:
	def accountsMerge(self, accounts):
		adj_list = {} #email: [emails connected]
		for account in accounts:
			name = account[0]
			for i in range(1,len(account)):
				email = account[i]
				if (name,email) not in adj_list:
					adj_list[(name,email)] = []
				adj_list[(name,email)].append(email)

				pass