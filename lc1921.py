#https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
'''
iroically enough this problem seems like car fleet again?
it's similar
simple simulation, no decisions to make
brute force:
- fire weapon
- decrement all the distances based on speed
- repeat until monster reaches or all gone
'''
class Solution1:
    def eliminateMaximum(self, dist, speed):
        monsters_smoked = 0
        while monsters_smoked < len(dist):
            monsters_smoked += 1
            for i in range(monsters_smoked,len(dist)):
                dist[i] -= speed[i]
                if dist[i] == 0:
                    return monsters_smoked
        # can kill all monsters
        return len(dist)

print(Solution.eliminateMaximum(None,[1,1,2,3],[1,1,1,1]))

# time = distance / speed
class Solution:
    def eliminateMaximum(self,dist,speed):
        arrival_times = [] * len(dist)
        for i in range(len(dist)):
            arrival_times[i] = dist[i]/speed[i]
        arrival_times.sort()
        while len(arrival_times) != 0:





