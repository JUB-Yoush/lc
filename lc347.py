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

    
    def bucketSortFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
         we map numbers as values of a hashmap that tell us the number of occurances each has
         this let's us only have to have as many keys as the length of the input array
        '''

        
        count = {}
        freq =[[] for i in range(len(nums)+1)] # make a 2d array with empty arrays the size of our input +1
        
        for n in nums:
            count[n] = 1 + count.get(n,0) # if n dosen't exist, it's 0, otherwise its +1
        
        for n,c in count.items(): # look over key-value pairs
            freq[c].append(n)

        res = []
        for i in range(len(freq) -1,0,-1): # from len -1 to 0, in decending order
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res