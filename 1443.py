"""
path from root to apple will take (path - root) * 2 seconds
return time to collect apples in subtree l and stree r
if single node is apple then it takes two seconds
dosen't actually sumerize the time properly
"""
class Solution:
    def minTime(self, n, edges, hasApple):
        adj_list = [[] for i in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
        def checkApples(n):
            nonlocal hasApple
            nonlocal adj_list
            if adj_list[n] != []:
                if adj_list[n][1] != None:
                    return checkApples(adj_list[n][0]) + checkApples(adj_list[n][1])
                else:
                    return checkApples(adj_list[n][0])

            if hasApple[n] and n != 0:
                return 2
            else:
                return 0

            if n == 0:
                return total

        return checkApples(0)

print(Solution.minTime(None,7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False]))