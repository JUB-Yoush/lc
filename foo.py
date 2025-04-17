"""
check if graph has any cycles (cyclic prerequisites)
make adj list
go through every node in dfs
if prereqs are completed (or empty), pop
add to set, dfs on it's prerequisites
"""

"""
split string by / to make folders
push folders that aren't "." or "" to the stack
pop from the stack when it's ".."
re-assemble the canon path based on folder stack
remove trailing /
"""


class Solution:
    def simplifyPath(self, path):
        folders = path.split("/")
        dir_stack = []
        res = "/"
        for folder in folders:
            if folder == "." or "":
                continue
            if folder == "..":
                if len(dir_stack) > 1:
                    dir_stack.pop()
                continue
            dir_stack.append(folder)

        for folder in dir_stack:
            res += f"{folder}/"

        return res[:-1]
