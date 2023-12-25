class Solution:
	def simplifyPath(path: str) -> str:
		folders = path.split('/')
		folder_stack = []
		canon_path = '/'

		for folder in folders:
			if folder == "..":
				if len(folder_stack) > 0: 
					folder_stack.pop()
				continue
			if folder == '.' or folder == '':
				continue
			folder_stack.append(folder)
   
		for folder in folder_stack:
			canon_path += f"{folder}/"

		if canon_path[-1] == '/' and len(canon_path) > 1:
			canon_path = canon_path[:-1]
		return canon_path

print(Solution.simplifyPath("/a/./b/../../c/"))