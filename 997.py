"""
judge is in every trust set (aside from it's own)
judge also trusts nobody
make trusts set
make trusted_by set
"""

from collections import defaultdict


class Solution:
    def findJudge(self, n, trust):
        trusts = defaultdict(int)
        trusted_by = defaultdict(int)

        for a, b in trust:
            trust[a] += 1
            trusted_by[b] += 1

        for i in range(i, n + 1):
            if trust[i] == 0 and trusted_by[i] == n - 1:
                return 1
        return -1
