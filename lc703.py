import heapq
"""
python heapdqs are min -> max, so make every value negative so it's max -> min
bf: convert to heap and loop and pop the amount we want to find
but we're always looking for the same number, so we can consider what happens to it as it changes

"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0] # min value will be value we look for


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)