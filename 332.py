# class SolutionBad:
#     def findItinerary(self, tickets: list[list[str]]) -> list[str]:
#         adj_list = {}
#         # make adj_list
#         for ticket in tickets:
#             if ticket[0] not in adj_list:
#                 adj_list[ticket[0]] = []
#             adj_list[ticket[0]].append(ticket[1])
#
#         # sort lists of edges:
#         for key, value in adj_list.items():
#             value.sort()
#
#         def dfs(src):
#
#         pass

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs("JFK")

        return res[::-1]


print(
    Solution.findItinerary(
        None,
        [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ],
    )
)
