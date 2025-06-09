"""
oh dear
okay so we need to figure out the correct route of tranformations to make to make target appear in the list
I can take any triplet and update it's value to be the max of itself + a different one
how could I represent this as a graph...
okay I don't think so because it dosen't make the merged value go away, that's the problem?
values cannot change, they can only swap places.
if I'm looking for 222 and 122 and 225 exist then no because no 2 in 3rd spot
converting to hashmap would be n * 3
1. check if the correct number exists in each index
2. check if the values next to the correct number are not greater than the other targets
3. secret thrid case??? or is that it.
"""


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        hastarget = [[], [], []]
        # fill map
        for i, triplet in enumerate(triplets):
            target_indexes = []
            for j in range(3):
                if triplet[j] > target[j]:
                    target_indexes = []
                    break
                if triplet[j] == target[j]:
                    target_indexes.append(j)

            if target_indexes == []:
                continue
            for k in target_indexes:
                hastarget[k].append(i)

        return (
            len(hastarget[0]) != 0 and len(hastarget[1]) != 0 and len(hastarget[2]) != 0
        )
