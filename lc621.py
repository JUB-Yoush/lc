import heapq
#https://leetcode.com/problems/task-scheduler/
'''
ik this is a heap problem but it seems like a queue of some kind could also work?
there is a non heap solution ofc but should I look for the heapish one?
the whole goal is to keep track of the last values called
have a queue of length n?
so call A
A get's loaded [A]
call B
B gets loaded [B,A]
idle because both are in queue [a,B]A #just use an a to represent null cuz it'll only be A-Z letters
A no longer in queue, can be called again
shifting everything up would be O(n)
and we'd do that n times so it'd be O(n^2)
how would a heap help?
newest elements would be on top?
adding elements would be o(logn)
we use a max heap to keep track of which number has the most instances left
loop through and add them all to the heap
then call the highest number
how to add keys and values to a heap?
let's ask neetcode man
I should review this
maybe I should make a site that lets you manage your leetcode progress
leetlist or somthing
and have it be so that it gives you recomended new problems as well as gets you to review old ones based on
- your level of understanding of the question and how long ago you did it
- it'll be based on the neetcode 150 list

'''
#neetcode soln
class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		count = Counter(tasks) # turns array into hashmap
		max_heap = [-cnt for cnt in count.values()]
		heapq.heapify(max_heap)

		time = 0
		q = deque() # pairs of [-count and idle_time]

		while max_heap or q:
			time += 1
			if max_heap:
				cnt = 1 + heapq.heappop(max_heap) # add 1 to decrement highest value bcuz negative
				if cnt:
					q.append([cnt,time + n])

			if q and q[0][1] == time:
				heapq.heappush(max_heap,q.popleft()[0])
		return time
