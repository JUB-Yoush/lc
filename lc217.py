class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for e in nums:
            if e in hash:
                return True
            hash.add(e)
        return False 