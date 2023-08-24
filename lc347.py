class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # turn list to set
        # make new dict based on set count length
        # match the key and iterate the value
        # return the higest value, remove the highest value
        # do this k times

        uniqueNums = set(nums)
        hashmap = {}
        output= [0] * k
        for num in uniqueNums:
            hashmap[num] = 0
        
        for num in nums:
            hashmap[num] += 1
        
        for i in range(k):
            output[i] = max(hashmap, key=hashmap.get)
            del hashmap[output[i]]
        
        return output
            