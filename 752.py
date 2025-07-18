"""
brute force: generate all possible lock states, if we reach a deadend then we igore that branch
memoization?
we don't need to return the specific route, just the length
we don't need to show our work
given any number we need to figure out how many turns to reach another number (just check if goign up or down is faster)
we don't want to alternate numbers going up or down
would we go down but then up to avoid a deadend?
we could modify another value first to skip the deadend (thanks example!)

for any lock state there are 8 branches
you want to keep a data structure to manage states you've already been in, to prevent loops
once you reach a deadend, stop
use a bfs to calculate how many moves you've made
mod values by 10 when adding
when subtracting add 10 then mod 10
add deadends to the visit set so we can't visit them
"""

from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        visited = set()
        queue = deque()
        queue.append(["0000", 0])
        visited.add(deadends)

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
            return res

        while queue:
            lock, time = queue.popleft()
            if lock == target:
                return time
            for newlock in children(lock):
                if newlock not in visited:
                    visited.add(newlock)
                    queue.append([newlock, time + 1])
        return -1
