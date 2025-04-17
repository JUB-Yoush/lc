"""
it's a bfs
we start at the first value, then we split based on the lowest and greatest
if it's a one, don't add the index to the queue
if it's oob, don't add
if we're at the limit, we win ayayaya
"""


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = []
        memo = set()
        queue.append(0)
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop()
                if curr == len(s) - 1:
                    return True
                for jump in range(minJump, maxJump + 1):
                    if (
                        curr + jump < len(s)
                        and s[curr + jump] != "1"
                        and curr + jump not in memo
                    ):
                        memo.add(curr + jump)
                        queue.append(curr + jump)
        return False
