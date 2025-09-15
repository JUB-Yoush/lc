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


def balls(n):
    return bin(n).count("1") + n.bit_length() - 1


print(balls(28))
print(balls(7))
