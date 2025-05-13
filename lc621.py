from enum import unique
import heapq
from collections import Counter

# https://leetcode.com/problems/task-scheduler/
"""
heap problem?
use a hashmap and try to space them out evenly?
keep count of how many were used and time till last one?
we'd have too increment it every time though, would be slow
greedy works aparently, greedy is kind of fake though. but who cares
what would greedy be? just pick the least recently used instruction?
check the position from the top of the stack?
    we're only checking the first n values of the stack though.
sort them so we can figure out order

AAABBB
AB_AB_AB
we don't need proof
I don't think maintaining a stack is nessicary
use a heap?
push value onto stack, once it reaches the top it's ready to be used?
decrementing a cooldown would be slow
if A is at the end of the queue and the queue is n long then that means A was last used n ago
every task has the same cooldown, which makes the problem much eaiser

"""


class Solution:
    def leastInterval(self, tasks, n) -> int:
        tasks.sort()
        task_unqiue = list(set(tasks))
        task_count = dict(Counter(tasks))
        queue = []
        # add every unique task to the queue,
        for i, task in enumerate(task_unqiue):
            queue.append(task)
            task_count[task] -= 1
            if task_count[task] == 0:
                del task_count[task]
                queue[i] = "_"

        cycles = len(queue)

        while task_count:
            # skip idles
            if queue[0] == "_":
                queue.pop(0)
                cycles += 1
                continue

            if len(queue) - 1 >= n:
                task_count[queue[0]] -= 1

                if task_count[queue[0]] == 0:
                    del task_count[queue[0]]
                    queue.pop(0)
                    queue.append("_")
                else:
                    queue.append(queue.pop(0))
                cycles += 1
            else:
                queue.append("_")

        return cycles
